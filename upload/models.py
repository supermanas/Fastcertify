from django.db import models
# Create your models here.

event_type_list = (
    ('technical','technical'),
    ('cultural','cultural'),
    ('sports','sports'),

)

event_organizers = (
    ('Computer society of India','Computer society of India'),
     ('Matrix club','Matrix club'),
      ('ACM Student chapter','ACM Student chapter') ,
       ('bits n bytes','bits n bytes'),
        ('IEEE','IEEE') ,
         ('C2S2','C2S2') ,
          ('Epic student club','Epic student club'),
          ('mechstein club','mechstein club') ,
           ('ASME','ASME'),
            ('water society','water society') ,
             ('NSS','NSS') ,
             ('NCC','NCC')

)

image_type = (
    ('student contribution','student contribution'),
    ('teacher contribution','teacher contribution'),
    ('student awards','student awards'),
    ('teacher awards','teacher awards'),
    ('custom','custom'),
    ('events','events')
)

years = (
    ('2000','2000'),
    ('2001','2001'),
    ('2002','2002'),
    ('2003','2003'),
    ('2004','2004'),
    ('2005','2005'),
    ('2006','2006'),
    ('2007','2007'),
    ('2008','2008'),
    ('2009','2009'),
    ('2010','2010'),
    ('2011','2011'),
    ('2012','2012'),
    ('2013','2013'),
    ('2014','2014'),
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027'),
    ('2028','2028')
)


class events(models.Model):
    event_name = models.CharField(max_length=100,verbose_name='name of the event',null=True)
    event_type = models.CharField(max_length=15,choices=event_type_list,default='technical',verbose_name='event type',null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    event_team = models.CharField(max_length=30,choices=event_organizers,verbose_name='Team organising',null=True)


    def __str__(self):
        """
        this is the part which will return
        """
        return self.event_name

class file_upload(models.Model):
    eventName = models.ForeignKey('events',on_delete=models.CASCADE,default=1,verbose_name='event name')
    eventYear = models.IntegerField(verbose_name='year of the event',choices = years,null=True)
    fileupload = models.FileField(upload_to='csv')

    def __str__(self):
        return str(self.eventName)+" "+str(self.eventYear)

class Photo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    types = models.CharField(max_length=100,choices=image_type,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)