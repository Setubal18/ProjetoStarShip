from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):

   return render(request,'base.html')