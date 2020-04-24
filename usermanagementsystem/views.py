from django.shortcuts import render
from usermanagementsystem.models import Adduser
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"MainPage.html")
    
def homepage(request):
    return render(request,"homepage.html")
def adduser(request):
    return render(request,"Adduser.html")
def showuser(request):
    abc = Adduser.objects.all()
    context={
        'data':abc
    }
    return render(request,"showuser.html",context)
def showparticularuser(request):
    return render(request,"particularuserdetails.html")

def showparticularuser1(request):
    name = request.POST['username']
    # print(name)
    abc = Adduser.objects.all()
    for i in abc:
        if(i.firstname == name):
            context={
                'data': i
            }
            return render(request,"particularuserdetails.html",context)
    else:
        return HttpResponse("<h1> Username not found </h1>")

def deleteuser(request):
    return render(request,"Deleteuser.html")
def deleteuser1(request):
    name = request.POST['username']
    # print(name)
    abc = Adduser.objects.all()
    for i in abc:
        if(i.firstname == name):
            context={
                'data': i
            }
            i.delete()
        
            return render(request,"deleteuser.html",context)
    else:
        return HttpResponse("<h1> Username not found </h1>")

def addetails(request):
    first_name = request.POST['Firstname']
    last_name = request.POST['Lastname']
    email = request.POST['Email']
    age = request.POST['Age']
    a = Adduser(firstname = first_name,lastname = last_name,email = email,Age = age)
    a.save()

    return render(request,"homepage.html")