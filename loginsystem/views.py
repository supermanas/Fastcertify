from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
import wikipedia
# Create your views here.

def home(request):
    """
    this is the home page
    """
    return render(request,"home/index.html")

@login_required
def contacts(request):
    """
    this is the contact us page
    """
    if request.method == 'POST':

        emailing = request.user.email
        lname = request.POST['last_name']
        fname = request.POST['first_name']
        messaging = request.POST['message']
        contactsave = Contact(first_name=fname,last_name=lname,email=emailing,message=messaging)
        contactsave.save()
        # co = whatsappdata(messaging)
        # if co==True:
        #     msg = "message sent successfully"
        # else:
        #     msg = "there was some error in the process try again"
        return redirect('/')
    else:
        form = ContactForm()
        context = {'form':form}
        return render(request,'nav/contacts.html',context)

# def whatsappdata(message):
#     import time
#     import webbrowser as web
#     import pyautogui as pg

#     pn="9425367540"
#     phone="+91"+pn
#     web.open('https://web.whatsapp.com/send?phone='+phone+'&text='+message)
#     time.sleep(20)
#     pg.press('enter')

#     return redirect('/')

def helping(request):
    """
    this is help page
    """
    if request.method == 'POST':

        query = request.POST.get('query')


        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request,'nav/help.html',{'ans':ans })



        except Exception:
            try:
                ans = "FOUND NOTHING"
                return render(request,'nav/help.html',{'ans':ans })
                # webbrowser.open('https://google.com/?#q=' + query)

            except:
                print("It is weird but I got nothing try re-running the program")
        return redirect("/")
    else:
        return render(request,'nav/help.html')

def aboutus(request):
    return render(request,"nav/aboutus.html")