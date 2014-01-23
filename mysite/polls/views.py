from django.shortcuts import render,get_object_or_404
from polls.models import Poll

def index(request):
    latest_poll_list=Poll.objects.order_by('-pub_date')[:5]
    context={'latest_poll_list':latest_poll_list}
    return render(request,'polls/index.html',context)

def detail(request,poll_id):
   
    poll=get_object_or_404(Poll,pk=poll_id)
   
    context={'poll':poll}
    return render(request,'polls/detail.html',context)
# Create your views here.
