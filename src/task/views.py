from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Process
from .serializers import ProcessSerializer

class ProcessList(generics.ListAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    
class ProcessDetail(generics.RetrieveAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer