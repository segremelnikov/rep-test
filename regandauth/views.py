# views.py
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import JsonResponse, Http404
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
from django.contrib.auth import login
from main.models import UserData
import threading


def register(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        user = None
        if "usernamesignup" in request.POST:
            user = User.objects.create_user(username=request.POST["usernamesignup"], password=request.POST["passwordsignup"], email=request.POST["emailsignup"])
            UserData.objects.create(user = user)
        if "usernamelogin" in request.POST:
            user = User.objects.get(username=request.POST["usernamelogin"]) 
        if "emailforgot" in request.POST: 
            user = User.objects.get(email=request.POST["emailforgot"])   
            user.set_password(request.POST["newpassword"])
            user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect("/")

    return render(request, "regandauth/index.html", {})


def check_code(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}

        user = User.objects.get(email=request.POST["email"])  
        response_data["correct"] = user.userdata.secret_code == request.POST["code"]

        return JsonResponse(response_data)


def check_password(request):

    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        try:
            user = User.objects.get(username=request.POST["login"])
            response_data["correct"] = user.check_password(request.POST["password"])
        except Exception as e:
            response_data["err"] = str(e)

        return JsonResponse(response_data)



def check_login(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        try:
            login = request.POST["login"]
            response_data["l"] = login
            user = None
            try:
                user = User.objects.get(username=login)
            except ObjectDoesNotExist as e:
                pass
            if not user:
                response_data["user_exists"] = False
            else:
                response_data["user_exists"] = True
        except Exception as e:
            response_data["err"] = str(e)

        return JsonResponse(response_data)

# for validating an Email
def check(email):
    if email.count('@') != 1:
        return False
    if email.rfind('.') < email.rfind('@'):
        return False
    if email.strip()[-1] == '.':
        return False
    left = email.split('@')[0]
    right = email.split('@')[1]
    if left.strip() != left:
        return False
    if len(left) == 0:
        return False
    if not left[0].isalpha():
        return False
    if right.count('.') != 1:
        return False
    sp = right.split('.')
    if not sp[-1].isalpha():
        return False
    if sp[0].strip() != sp[0]:
        return False
    if sp[1].strip() != sp[1]:
        return False
    if not any(map(str.isalpha, sp[0])):
        return False
    if len(sp[0]) < 2:
        return False
    if len(sp[1]) < 2:
        return False
    return True





def check_email(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        try:
            email = request.POST["email"]
            response_data["l"] = email
            user = None
            response_data["is_correct"] = check(email)
            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_busy"] = False
            else:
                response_data["is_busy"] = True
        except Exception as e:
            response_data["err"] = str(e)

        return JsonResponse(response_data)


def sendcode(request):    
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        try:
            code = random.randint(100,999)
            email = request.POST["email"]
            user = User.objects.get(email=email)
            user.userdata.secret_code = str(code)
            user.userdata.save()
            res = send_mail(
                'Секретный код',
                str(code),
                'Kelly Rep test <kellyreptest@gmail.com>',
                [email],
                fail_silently=False,
            )
            response_data["is_correct"] = bool(res)
        except Exception as e:
            response_data["err"] = e
        return JsonResponse(response_data)
