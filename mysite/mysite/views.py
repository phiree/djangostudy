from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import  reverse
from django.views import generic
from polls.models import Poll,Choice
def home(request):
    random_poll=Poll.objects.last()
    
    templateContent={'last_poll':random_poll}
    return render(request,'index.html',templateContent)
