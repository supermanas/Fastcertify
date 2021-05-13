from django import forms
from .models import file_upload,events,Photo
import datetime

class UploadForm(forms.ModelForm):
    class Meta:
        model = file_upload
        fields = '__all__'

class eventregister(forms.ModelForm):
    class Meta:
        model = events
        fields = '__all__'

class fetcher(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'name':'name'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'yearsin','class':'sar'}))
    nameofstudent = forms.CharField(widget=forms.TextInput(attrs={'name':'nameofstudent'}))
    passing_year_of_student = forms.CharField(widget=forms.DateInput(attrs={'value':datetime.date.today(),'required':False}))

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image','name','description','types']