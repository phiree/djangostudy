from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello,world. You are in the poll index.')

def detail(request,poll_id):
    return HttpResponse("you are looking at poll %s"%poll_id)
# Create your views here.
