from django.shortcuts import render,HttpResponseRedirect
from .forms import EmployeeRegistration
from .models import User
from django.contrib import messages
# Create your views here.


#this fun willl add and show the data
def add_show(request):
    if request.method=='POST':
        fm=EmployeeRegistration(request.POST)
        if fm.is_valid():
         #fm.save()  one method is this to save data 
         nm=fm.cleaned_data['name']
         em=fm.cleaned_data['email']
         psw=fm.cleaned_data['password'] #whatever we dont want to be saved we can remove here
         reg=User(name=nm,email=em,password=psw)
         reg.save()  #second method line 10-14
         fm=EmployeeRegistration()
    else:
        fm=EmployeeRegistration()
    empy=User.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm ,'emp':empy})

#This function will update the data
def update_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm=EmployeeRegistration(request.POST,instance=pi)
        if fm.is_valid:
            fm.save()
            messages.success(request,"Updated!")
            
    else:
        pi=User.objects.get(pk=id)
        fm=EmployeeRegistration(instance=pi)

    return render(request,'enroll/updateemployee.html',{'form':fm})




#This function will delete the data
def delete_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
