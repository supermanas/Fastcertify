from django.shortcuts import render,HttpResponse,redirect
from upload.models import Photo
from .models import filemaker,emailonly
from upload.models import events,file_upload
from django.http import JsonResponse
from .forms import maker,emailform
from datetime import datetime
from fastcertify import settings
from django.contrib.auth.decorators import login_required
import pandas as pd
import cv2 as cv
from django.core.mail import EmailMessage


# Create your views here.
@login_required
def mark1(request,pk,lines):
    if request.method == 'GET':
        return render(request,'creator/mark.html')

@login_required
def studentcontribution(request):
    img = Photo.objects.filter(types='student contribution')
    context = {'img':img}
    return render(request,'creator/studentcontribution.html',context)

@login_required
def teachercontribution(request):
    img = Photo.objects.filter(types='teacher contribution')
    context = {'img':img}
    return render(request,'creator/teachercontribution.html',context)
@login_required
def studentawards(request):
    img = Photo.objects.filter(types='student awards')
    context = {'img':img}
    return render(request,'creator/studentawards.html',context)
@login_required
def teacherawards(request):
    img = Photo.objects.filter(types='teacher awards')
    context = {'img':img}
    return render(request,'creator/teacherawards.html',context)
@login_required
def custom(request):
    img = Photo.objects.all()
    context = {'img':img}
    return render(request,'creator/custom.html',context)

@login_required
def viewer(request,pk):
    ma=pk
    if 'lines' in request.session:
        sr = int(request.session['lines'])

    if 'subject' in request.session:
        subject = request.session['subject']
    if 'message' in request.session:
        message = request.session['message']

    asper=[]
    for x in range(0,sr):
        asper.append('a'+ str(x))
    print(asper)
    adict={}
    resting=[]
    empty = 0

    if request.method=='POST':
        if request.POST.get("submit"):
            eid = request.POST.get("eventName")
            ename = events.objects.get(id=eid)
            year = request.POST.get("eventYear")
            thickness = int(request.POST.get("thickness"))
            date = request.POST.get("date")
            datexaxis = int(request.POST.get("date_xaxis"))
            dateyaxis = int(request.POST.get("date_yaxis"))
            datethick = int(request.POST.get("datethick"))
            fname = file_upload.objects.get(eventName__event_name=ename,eventYear=year)
            cssv = fname.fileupload.name
            img = Photo.objects.get(id=pk)
            template_path = 'media/'+img.image.name
            details_path = cssv
            output_path = 'media/pictures/'
            font_size = 1
            font_color = (0,0,0)
            coordinate_y_adjustment = request.POST.get("yaxis")
            coordinate_x_adjustment = request.POST.get("xaxis")
            df = pd.read_csv('media/'+cssv,usecols=[0,1])
            for ind in df.index:
                certi_name = df['Name'][ind]
                certi_email = df['Email'][ind]
                img = cv.imread(template_path)
                font = cv.FONT_HERSHEY_COMPLEX_SMALL
                text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]
                text_x = int(coordinate_x_adjustment)
                text_y = int(coordinate_y_adjustment)
                cv.putText(img, certi_name,(text_x ,text_y ),font, font_size,font_color, thickness)
                cv.putText(img,date,(datexaxis,dateyaxis),font,font_size,font_color,datethick)
                for i in asper:
                    texter = request.POST.get("a"+i)
                    xcordinate = int(request.POST.get("b"+i))
                    ycordinate = int(request.POST.get("c"+i))
                    thicker = int(request.POST.get("d"+i))
                    cv.putText(img, texter ,(xcordinate ,ycordinate ),font, font_size,font_color, thicker)

                certi_path = output_path + certi_name + '.png'
                print(certi_path)
                cv.imwrite(certi_path,img)
                img_data = open(certi_path,'rb').read()
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [certi_email])
                mail.attach(certi_name,img_data,'image/png')
                mail.send()

            context = {
                'img':img,
                'path':'/'+certi_path
            }
            del request.session['lines']
            del request.session['subject']
            del request.session['message']

            return render(request,"creator/submitted.html")
        else:

            eid = request.POST.get("eventName")
            ename = events.objects.get(id=eid)
            year = request.POST.get("eventYear")
            thickness = int(request.POST.get("thickness"))
            date = request.POST.get("date")
            Color = request.POST.get("color")
            datexaxis = int(request.POST.get("date_xaxis"))
            dateyaxis = int(request.POST.get("date_yaxis"))
            datethick = int(request.POST.get("datethick"))
            fname = file_upload.objects.get(eventName__event_name=ename,eventYear=year)
            cssv = fname.fileupload.name
            img = Photo.objects.get(id=ma)
            template_path = 'media/'+img.image.name
            details_path = cssv
            output_path = 'media/pictures/'
            font_size = 1
            font_color = (0,0,0)
            coordinate_y_adjustment = request.POST.get("yaxis")
            coordinate_x_adjustment = request.POST.get("xaxis")
            df = pd.read_csv('media/'+cssv,usecols=[0,1])
            ind = 0
            certi_name = df['Name'][ind]
            img = cv.imread(template_path)
            font = cv.FONT_HERSHEY_COMPLEX_SMALL

            text_size = cv.getTextSize(certi_name, font, font_size, 10)[0]
            text_x = int(coordinate_x_adjustment)
            text_y = int(coordinate_y_adjustment)
            cv.putText(img, certi_name,(text_x ,text_y ),font, font_size,font_color, thickness)
            cv.putText(img,date,(datexaxis,dateyaxis),font,font_size,font_color,datethick)
            for i in asper:
                texter = request.POST.get("a"+i)
                xcordinate = int(request.POST.get("b"+i))
                ycordinate = int(request.POST.get("c"+i))
                thicker = int(request.POST.get("d"+i))
                adict["a"+i]=texter
                print(adict.get("a"+i))
                cv.putText(img, texter ,(xcordinate ,ycordinate ),font, font_size,font_color, thicker)

            # counter=len(resting)
            # co = 0
            # for i in resting:
            #     print(resting[co])
            #     co=co+1

            certi_path = output_path + certi_name + '.png'
            cv.imwrite(certi_path,img)
            form = maker(request.POST)
            context = {
                'img':img,
                'path':'/'+certi_path,
                'form':form,
                'id':pk,
                'num':asper,
                'adict':adict,


            }
            return render(request,"creator/selector.html",context)
    else:
        form = maker(request.POST)
        img = Photo.objects.get(id=pk)
        context = {'path':img.image.url,'form':form,'id':pk,'num': asper,'adict':adict}
        return render(request,'creator/selector.html',context)


@login_required
def faq(request):
    if request.method=='POST':
        lines = request.POST.get("line")
        request.session['lines']=lines
        subject = request.POST.get("subject")

        message = request.POST.get("Message")
        if request.POST.get("cc")!=None:
            cc = request.POST.get("cc")
        if request.POST.get("bcc")!=None:
            bcc = request.POST.get("bcc")
        gil = emailonly(lines=lines,subject=subject,message=message,cc=cc,bcc=bcc)
        em = gil.pk
        request.session['subject']=subject
        request.session['message']=message
        request.session['pks']=em
        return redirect('mark1',pk=em,lines=lines)

    else:
        return render(request,'creator/faq.html')
