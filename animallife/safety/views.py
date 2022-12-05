from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import *
import json
from django.db.models import Q, Count
from datetime import datetime, timedelta
import time
from operator import itemgetter
from django.core.paginator import Paginator
from django.db.models.functions import Cast
from django.db import connections
from django.shortcuts import render
from .models import Videos
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File as DjangoFile

def upload(request):
    return render(request,'upload.html')

def tmp_result(request):
    tmp_results=Videos.objects.all()
    return render(request,'tmp_result.html',{'tmp_results':tmp_results})


@csrf_exempt
def upload_create(request):
    form = Videos()
    form.title = request.POST.get('title', "test")
    form.status = request.POST.get('status', "status")
    form.begin_timestamp = request.POST.get('begin_timestamp', "begin_timestamp")
    form.end_timestamp = request.POST.get('end_timestamp', "end_timestamp")
    form.user_id = request.POST.get('user_id', "user_id")
    try:
        form.video= request.FILES['video']
    except:
        pass
    form.save()
    return redirect('tmp_result')

def index(request):
    user_id = request.session.get('user')
    if user_id:
        user_name = AnimalUsers.objects.get(pk=user_id).username
    else:
        user_name = None

    res_data = {'user_name': user_name}
    return render(request, 'index.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def about_lifestyle(request):
    user_id = request.session.get('user')
    if user_id:
        user_name = AnimalUsers.objects.get(pk=user_id).username
    else:
        user_name = None

    res_data = {'user_name': user_name}
    return render(request, 'about_animal_lifestyle.html', res_data)

def about_bodypoint(request):
    user_id = request.session.get('user')
    if user_id:
        user_name = AnimalUsers.objects.get(pk=user_id).username
    else:
        user_name = None

    res_data = {'user_name': user_name}
    return render(request, 'about_animal_bodypoint.html', res_data)


def bodypoint(request):
    user_id = request.session.get('user')
    if user_id:
        user_name = AnimalUsers.objects.get(pk=user_id).username
    else:
        user_name = None

    res_data = {'user_name': user_name}
    return render(request, 'animal_body_point.html', res_data)

def lifestyle(request):
    user_id = request.session.get('user')
    if user_id:
        user_name = AnimalUsers.objects.get(pk=user_id).username
        eat_result = Videos.objects.filter(Q(user_id=user_name) & Q(status="eat")).order_by('-begin_timestamp')
        return render(request, 'animal_lifestyle.html', {'user_name':user_name,'eat_result': eat_result})
    else:
        user_name = None

    return redirect('login')


def contact(request):
    user_id = request.session.get('user')
    if user_id:
        user_name = AnimalUsers.objects.get(pk=user_id).username
    else:
        user_name = None

    res_data = {'user_name':user_name}
    return render(request, 'contact.html', res_data)

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = "Input all value"
        if password != re_password :
            res_data['error'] = 'Repeat Password '
        else :
            user = AnimalUsers(username=username, password=make_password(password))
            user.save()
        return render(request, 'register.html', res_data)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_data = {}
        if not (username and password):
            res_data['error'] = 'Login failed'
        else:
            try:
                fcuser = AnimalUsers.objects.get(username=username)
                if check_password(password, fcuser.password):
                    request.session['user'] = fcuser.id
                    return redirect('/')

                else:
                    res_data['error'] = 'Login failed'
            except AnimalUsers.DoesNotExist:
                res_data['error'] = 'Login failed'
        return render(request, 'login.html', res_data)

    res_data = {
                }
    return render(request, 'login.html', res_data)



