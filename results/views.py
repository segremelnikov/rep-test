from django.shortcuts import render
from main.models import UserData
from django.contrib.auth.models import User


def index(request):
    user = request.user
    data = UserData.objects.get_or_create(user=request.user)[0]
    passed = data.has_added_people and data.has_estimeted_people
    
    context = {'user': user, 'passed': passed, 'pth': 'res' }
    return render(request, "results/index.html", context)
