from django.urls import path
from .views import home,contacts,helping,aboutus

urlpatterns = [
    path('',home,name="home"),
    path('contacts/',contacts,name='contacts'),
    path('help/',helping,name="help"),
    path('about/',aboutus,name="aboutus")
]