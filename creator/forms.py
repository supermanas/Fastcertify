from .models import filemaker,emailonly
from django import forms
from colorfield.fields import ColorField
import datetime

class maker(forms.ModelForm):
    class Meta:
        model = filemaker
        fields = '__all__'
        widgets={
            'eventName': forms.Select(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'eventYear' : forms.Select(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'filed' : forms.DateField(),
            'xaxis' : forms.NumberInput(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'yaxis' : forms.NumberInput(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'thickness' : forms.NumberInput(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'date' : forms.DateInput(attrs={'onchage':'mySubmit(this)','class':'w3','value':datetime.date.today()}),
            'date_xaxis' : forms.NumberInput(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'date_yaxis' : forms.NumberInput(attrs={'onchange':'mySubmit(this)','class':'w3'}),
            'datethick' : forms.NumberInput(attrs={'onchange':'mySubmit(this)','class':'w3'}),

        }


class emailform(forms.ModelForm):
    class Meta:
        model = emailonly
        fields = '__all__'
        widgets={
            'lines':forms.NumberInput(attrs={'name':'lines'}),
            'subject':forms.NumberInput(attrs={'name':'subject'}),
            'message':forms.NumberInput(attrs={'name':'message'}),
            'cc':forms.NumberInput(attrs={'name':'cc','required':False}),
            'bcc':forms.NumberInput(attrs={'name':'bcc','required':False}),
        }
