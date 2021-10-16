from django.shortcuts import redirect
from django.contrib.auth.models import User
from main.models import UserData, UserEntry, AnonEntry
from django.http import JsonResponse, Http404, HttpResponse



def index(request):
     
    user = request.user
    userdata = UserData.objects.get_or_create(user = user)[0]
    if not userdata.has_added_people:
        return redirect('addpeople/')
    if not userdata.has_estimeted_people:
        return redirect('estpeople/')
    return redirect('results/')



def stats(request):

    if request.method == "GET":
        raise Http404("URL doesn't exists")
     

    user = request.user
    ip = get_ip(request)
    page = request.POST["page"]
    datetime = request.POST["datetime"] 
    width = request.POST["width"]
    height = request.POST["height"]
    browser = request.POST["browser"]
    os = request.POST["os"]
    mob = request.POST["mob"] == "true"
    tz = request.POST["tz"]
 

    if request.user.is_authenticated: 
        user.userentry_set.create(ip=ip, page=page, datetime=datetime, width=width, height=height, browser=browser, os=os, is_mob=mob, tz=tz)

    else: 
        AnonEntry.objects.create(ip=ip, page=page, datetime=datetime, width=width, height=height, browser=browser, os=os, is_mob=mob, tz=tz)

    
    return HttpResponse(status=204)

    



def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

        