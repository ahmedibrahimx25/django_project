from django.urls import path
from .views import ProcessList, ProcessDetail

urlpatterns = [
    path("", ProcessList.as_view(), name="process_list"),
    path("api/<str:pk>/", ProcessDetail.as_view(), name="process_detail"),
]