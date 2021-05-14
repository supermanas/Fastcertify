from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import file_upload,events
from .forms import UploadForm,eventregister,fetcher,PhotoForm
from django.http import JsonResponse
import pandas as pd


# Create your views here.

@login_required
def upload_docs(request):
    """
    this is the uploading of documents
    """
    prompt = {'order':'Order of the csv should be name of the event, year of the event, file to be uploaded'}
    if request.method == 'POST':
        if request.POST.get('fi'):
            form = UploadForm(request.POST ,request.FILES)
            en_id = request.POST.get("events")
            year = request.POST.get("year")
            fil = request.FILES['file']
            en = events.objects.get(id=en_id)
            if not fil.name.endswith('.csv'):
                messages.error(request,'this is not a csv file')
                return HttpResponse("not csv file")
            else:
                file_upload.objects.create(
                    eventName=en,
                    eventYear=year,
                    fileupload=fil
                )
                return HttpResponse("File was uploaded")
        elif request.POST.get('su'):
            register = eventregister(request.POST)
            if register.is_valid():
                register.save()
                return redirect('/')

        else:
            photof = PhotoForm(request.POST or None,request.FILES or None)
            data = {}
            if request.is_ajax():
                if photof.is_valid():
                    photof.save()
                    data['name'] = photof.cleaned_data.get('name')
                    data['status']='ok'
                    return JsonResponse(data)


            # else:
            #     register = eventregister(request.POST)
            #     if register.is_valid():
            #         register.save()
            #         return redirect('/upload/')
            #     else:
            #         messages.error(request,'Something went wrong')


    else:
        reg = eventregister()
        photos = PhotoForm()
        form = UploadForm()
        year = [i for i in range(2000,2028)]
        context ={
            'register':reg,
            'form':form,
            'events':events.objects.all(),
            'upload':file_upload.objects.all(),
            'photos':photos,
            'prompt':prompt,
            'year': year
        }
        return render(request,"uploads/uploadmain.html",context=context)

@login_required
def searchforum(request):
    """
    this is the search forum
    """
    if request.method == 'POST':
        year = int(request.POST.get('year'))
        name = request.POST.get('name')
        nameofstudent = request.POST.get('nameofstudent')
        try:
            fname = file_upload.objects.get(eventName__event_name=name,eventYear=year)
            cssv = fname.fileupload.name
            df = pd.read_csv('media/'+cssv,usecols=[0,1])
            for ind in df.index:
                if nameofstudent.lower() in df['Name'][ind].lower():
                    return HttpResponse("studentfound")

            form = fetcher()
            context ={
                'ans':'not found',
                'form':form
            }

            return render(request,'searchforum/searchmain.html',context)
        except:
            return HttpResponse(request,'Something is wrong with the file please try again')

    else:
        form = fetcher()
        ev = events.objects.all()

        context = {
            'form':form,
            'events':ev
        }
        return render(request,'searchforum/searchmain.html',context)