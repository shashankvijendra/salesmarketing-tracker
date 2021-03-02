from django.shortcuts import render
from salestrackingapp.views import *
from django.views import View
from salestrackingapp.models import *
from django.template import RequestContext
from django.shortcuts import render
from salestrackingapp.forms import dailyform,registrationform,customerform
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
import logging
import json
from salestrackingapp.models import *
from datetime import date
from django.db.models import Max
# Create your views here.

def registration(request):
    customobject=registrationform.CustomUserCreationForm(request.POST or None)
    if customobject.is_valid():
        userdetailsobj=Userdata()

        userdetailsobj.email=customobject.cleaned_data['email']
        userdetailsobj.Age=customobject.cleaned_data['Age']
        userdetailsobj.phonenumber=customobject.cleaned_data['PhoneNumber']
        userdetailsobj.save()
        userobject=User.objects.create_user(
            email=customobject.cleaned_data['email'],
            username=customobject.cleaned_data['PhoneNumber'],
            password=customobject.cleaned_data['password1'],
            )
        userobject.save()        
        return HttpResponseRedirect('/sales/login/')
    context={
        'customobject':customobject
    }
    return render(request, 'sales/register.html', context)
def home(request):
    usernumber=Userdata.objects.get(phonenumber=request.user.username)
    max_dateobject=dailystatus.objects.aggregate(Max('created_on'))
    max_dateval=max_dateobject['created_on__max']
    dateval=dailystatus.objects.filter(User_f_id=usernumber).values('created_on')
    if max_dateval.day== datetime.datetime.now().day and max_dateval.month== datetime.datetime.now().month and max_dateval.year== datetime.datetime.now().year:
        task=0
    else:
        task=1
    context={
        'task':task
    }
    return render(request, 'sales/home.html', context)

def dailytask(request):
    taskobject=dailyform.dailytask(request.POST or None)
    if taskobject.is_valid():
        # print(User.objects.all().values())
        # print(request.user.username)
        saveobject=dailystatus()
        saveobject.Area_visited=taskobject.cleaned_data['Area_visited']
        saveobject.total_persons_approched=taskobject.cleaned_data['total_persons_approched']
        saveobject.number_converted=taskobject.cleaned_data['number_converted']
        usernumber=Userdata.objects.get(phonenumber=request.user.username)
        print(usernumber)
        saveobject.User_f_id=usernumber
        saveobject.save()
        return HttpResponseRedirect('/sales/home')
    context={
        'taskobject':taskobject,
    }
    return render(request, 'sales/dailytask.html', context)

def customer_data(request):
    customerobject=customerform.customer(request.POST or None)
    if customerobject.is_valid():
        # print(User.objects.all().values())
        # print(request.user.username)
        cus_saveobject=customerdata()
        cus_saveobject.Name=customerobject.cleaned_data['Name']
        cus_saveobject.DOB=customerobject.cleaned_data['DOB']
        cus_saveobject.Age=customerobject.cleaned_data['Age']
        cus_saveobject.Gender=customerobject.cleaned_data['Gender']
        cus_saveobject.Family_member=customerobject.cleaned_data['Family_member']
        if customerobject.cleaned_data['Is_client']:
            bool_data=True
        else:
            bool_data=False
        cus_saveobject.Is_client=customerobject.cleaned_data['Is_client']
        usernumber=Userdata.objects.get(phonenumber=request.user.username)
        cus_saveobject.User_c_id=usernumber
        cus_saveobject.save()
        return HttpResponseRedirect('/sales/home')
    context={
        "customerobject":customerobject
    }
    return render(request, 'sales/customerdata.html', context)

def customer_data_display(request):
    userobj=Userdata.objects.get(phonenumber=request.user.username)
    customerdatadisplay=customerdata.objects.filter(User_c_id=userobj).values()
    print(customerdatadisplay)
    context={
        'customer_det_display':customerdatadisplay
    }
    return render(request, 'sales/cus_data_display.html', context)

def customer_data_delete(request,id):
    customerdatadisplay=customerdata.objects.filter(id=id).delete()
    return HttpResponseRedirect('/sales/customerdata/display')

def editdata_save(request):
    edit_ajax_data=json.loads(request.POST['edit_customer_data'])
    print(edit_ajax_data)
    editobj=customerdata.objects.get(id=edit_ajax_data['id'])
    editobj.Name=edit_ajax_data['name']
    editobj.DOB=edit_ajax_data['dob']
    editobj.Family_member=edit_ajax_data['age']
    editobj.Gender=edit_ajax_data['gender']
    editobj.Family_member=edit_ajax_data['familymember']
    # editobj.Is_client=edit_ajax_data['familymember']
    editobj.save()
    
    return JsonResponse({'msg':'success'})