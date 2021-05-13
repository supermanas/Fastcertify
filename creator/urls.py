from django.urls import path
from .views import mark1,teacherawards,teachercontribution,studentawards,studentcontribution,custom,viewer,faq

urlpatterns = [
    path('<str:pk><str:lines>',mark1,name="mark1"),
    path('student-contribution/',studentcontribution,name="student-contribution"),
    path('Teacher-contribution/',teachercontribution,name="Teacher-contribution"),
    path('student-awards/',studentawards,name="student-awards"),
    path('teacher-awards/',teacherawards,name="teacher-awards"),
    path('custom/',custom,name="custom"),
    path('viewer/(?P<pk>\d+)/$',viewer,name="viewer"),
    path('question/',faq,name="faq"),

]