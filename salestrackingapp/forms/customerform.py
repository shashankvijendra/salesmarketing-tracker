from salestrackingapp.models import *
from django import forms

class customer(forms.ModelForm):
    class Meta:
        model=customerdata
        fields=['Name','DOB','Age','Gender','Family_member','Is_client']

        widgets = {'Name' : forms.TextInput(attrs={'class': 'form-control','id':'Name'}),
                   'DOB' : forms.TextInput(attrs={'class': 'form-control','id':'DOB'}),
                   'Age' : forms.TextInput(attrs={'class': 'form-control','id':'Age'}),
                   'Gender' : forms.TextInput(attrs={'class': 'form-control','id':'Gender'}),
                   'Family_member' : forms.TextInput(attrs={'class': 'form-control','id':'Family_member'}),

                    }