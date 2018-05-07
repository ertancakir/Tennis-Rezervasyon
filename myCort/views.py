from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
from django.http import JsonResponse
from django.core import serializers
import simplejson as json

from .models import Reservation, Users

# Create your views here.


def index(request):
    if request.method == 'POST':
        return redirect('/tennis/')
    else:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return render(request,'myCort/index.html',{'user' : request.user, 'reservation' : None})
            u = Users.objects.get(email = request.user.username)
            allReservation = Reservation.objects.filter(userId = u).order_by('-date')
            return render(request,'myCort/index.html',{'user' : request.user, 'reservation' : allReservation})
        else:
            return render(request,'myCort/index.html',{'user' : None, 'reservation' : None})



def loginView(request):
    if request.method == 'POST':
        loginMail = request.POST.get('loginMail','')
        loginPass = request.POST.get('loginPass','')
        user = authenticate(request, username=loginMail, password=loginPass)
        if user is not None:
            login(request, user)
            return redirect('/tennis/')
        else:
            return redirect('/tennis/login/')
    else:
        return render(request,'myCort/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('uName','')
        email = request.POST.get('uEmail','')
        password = request.POST.get('uPass','')
        lastName = request.POST.get('lName','')

        u = User.objects.create_user(email)
        u.first_name = name
        u.email = email
        u.username = email
        u.set_password(password)
        u.last_name = lastName
        u.save()
        user = authenticate(request, username=email, password=password)
        login(request, user)
        userTable = Users()
        userTable.name = name
        userTable.email = email
        userTable.surname = lastName
        userTable.save();
        return redirect('/tennis/')

def adminPanel(request):
    if request.method == "GET":
        if request.user.is_superuser:
            u = Users.objects.all()
            return render(request,'myCort/admin.html',{'users' : u})
        else:
            return redirect('/tennis/')
    else:
        uid = request.POST.get('userId','')
        u = Users.objects.get(pk = uid)
        r = Reservation.objects.filter(userId = u).order_by('-date')
        jsonStr = serializers.serialize('json', r)
        return JsonResponse(jsonStr,safe=False)

#Burası çalışmıyor.
#Hata veriyor json ile ilgili galiba burasını düzelt
#tabloda olan saatleri dom ile index.html'den çıkar
def ajaxRequest(request):
    pickDate = request.POST.get('date','')
    data = Reservation.objects.values('time').filter(date = pickDate)
    times = [];
    for time in data:
        times.append(time)
    jsonStr = json.dumps(times)
    #data_serialized = serializers.serialize('json', times)
    return JsonResponse(jsonStr,safe=False)



def reservation(request):
    date = request.POST.get('date','')
    time = request.POST.get('time','')
    res = Reservation()
    res.date = date
    res.time = time
    if request.user.is_authenticated:
        res.userId = Users.objects.get(email = request.user.email)
        print(res.userId)
    else:
        userTable = Users()
        userTable.name = request.POST.get('misafir_ad','')
        userTable.email = request.POST.get('misafir_email','')
        userTable.surname = request.POST.get('misafir_soyad','')
        userTable.save();
        res.userId = userTable
    res.save()
    return redirect('/tennis/')

def deleteReservation(request,res_id):
    res = Reservation.objects.get(pk = res_id)
    res.delete()
    return redirect('/tennis/')

def logoffSession(request):
    logout(request)
    return redirect('/tennis/')

def getReservation(request):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request,'myCort/listRes.html')
        else:
            return redirect('/tennis/')
    else:
        pickDate = request.POST.get('date','')
        data = Reservation.objects.filter(date = pickDate)
        data_serialized = serializers.serialize('json', data)
        return JsonResponse(data_serialized,safe=False)
