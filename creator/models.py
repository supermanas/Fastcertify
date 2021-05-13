from django.db import models
import datetime
from upload.models import events,file_upload,years
# Create your models here.


class filemaker(models.Model):
    eventName = models.ForeignKey(events,on_delete=models.CASCADE,default=1,verbose_name='event name')
    eventYear = models.IntegerField(verbose_name='year of the event',choices = years,null=True,default=2021)
    filed = models.DateTimeField(auto_now_add=True)
    xaxis = models.IntegerField(verbose_name='Name x-axis ',default=0)
    yaxis = models.IntegerField(verbose_name='Name y-axis',default=0)
    thickness = models.PositiveIntegerField(default=2,verbose_name="thickness for the name")
    date = models.CharField(max_length=100,default=datetime.date.today())
    date_xaxis = models.IntegerField(verbose_name='Date x-axis', default=0)
    date_yaxis = models.IntegerField(verbose_name='Date y-axis' ,default=0)
    datethick = models.IntegerField(verbose_name="thickness for the date")



    def __str__(self):
        return str(self.filed)

class emailonly(models.Model):
    lines = models.IntegerField()
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=400)
    cc = models.CharField(max_length=100,null=True,blank=True)
    bcc = models.CharField(max_length=100,null=True,blank=True)