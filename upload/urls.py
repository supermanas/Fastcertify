from django.urls import path
from .views import upload_docs,searchforum

urlpatterns = [
    path('',upload_docs,name="uploading"),
    path('search/',searchforum,name="searchforum"),

]