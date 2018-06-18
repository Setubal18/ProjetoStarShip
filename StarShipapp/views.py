from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    return render (request,"base.html",)


def listar_naves(request):
    naves= Nave.objects.all()
    naves ={ 'lista' : naves}
    return render (request,"listar_nave.html",naves)


def logar(request):
    next = request.GET.get('next', '/listar_naves/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(sername=username, password=password)

        if user is not None:
            login(request, user)
        return HttpResponseRedirect(next)

    else:
        messages.error(request,'Usuario ou senha Incorretas')
        return  HttpResponseRedirect('/login/')
        #return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request,'Login.html',{'redirect_to': next})
