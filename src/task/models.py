import uuid

from django.db import models


def generate_process_id():
    return str(uuid.uuid4())


class Process(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=generate_process_id)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title