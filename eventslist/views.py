from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse
import json

# Create your views here.

def eventIndex(request):
    events=list(EventIndex.objects.order_by('-priority'))

    notStartedEvents=[]
    startedEvents=[]
    endedEvents=[]

    currentTime=timezone.now()

    for i in events:
        if i.startTime>currentTime:
            notStartedEvents.append(i)
        elif i.startTime <=currentTime and currentTime<i.endTime:
            startedEvents.append(i)
        else:
            endedEvents.append(i)

    return render(request, 'eventslist/eventIndex.html', { 'notStartedEvents':notStartedEvents, 'startedEvents':startedEvents, 'endedEvents':endedEvents })


def details(request):
    try:
        event=EventIndex.objects.get(title=request.GET.get('eventtitle'))
    except:
        return render('eventslist/eventIndex.html')

    return render(request,'eventslist/details.html',{'event':event})
