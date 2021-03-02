from salestrackingapp.models import *
from django import forms

class dailytask(forms.ModelForm):
    class Meta:
        model=dailystatus
        fields=['Area_visited','total_persons_approched','number_converted']

        widgets = {'Area_visited' : forms.TextInput(attrs={'class': 'form-control','id':'Area_visited'}),
                   'total_persons_approched' : forms.TextInput(attrs={'class': 'form-control','id':'total_persons_approched'}),
                   'number_converted' : forms.TextInput(attrs={'class': 'form-control','id':'number_converted'}),
                    }