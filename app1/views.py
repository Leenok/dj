from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect
from app1.models import pzzle
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout


def index(request):
    name = request.session.get("is_auth", "Не авторизован")
    if name != 'Не авторизован':
        res = pzzle.objects.all()
        if request.method == "POST":
            data = request.POST
            new = pzzle(name = data['name'], detail = data['detail'], style = data['style'], material = data['material'], age = data['age'], price = data['price'], count = data['count'])
            new.save()
            return render(request, 'index.html', {'puzzle': res, 'username': name})
        
        else:
            return render(request, 'index.html',  {'puzzle': res, 'username': name})
    else:
        return redirect(auth)

def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username = data['login'], password = data['password'])
        if user is not None:
            request.session['is_auth'] = user.username
            return redirect(main)
            # return render(request, 'login.html',  {'res': user})
        else:
            return HttpResponse('wrong login or password.')
    else:
        return render(request, 'auth.html')
    
def reg(request):
    # res = User.objects.all()
    if request.method == "POST":
        not_valid = ''
        data = request.POST
        
        if (User.objects.filter(username = data['login'])):
            not_valid = 'Такой login уже есть'
            return render(request, 'registration.html',  {'not_valid_regist': not_valid})
        
        user = User.objects.create_user(data['login'],data['email'],data['password'])
        user.first_name = data['name']

        if data['password'] == data['password2']:
            user.save()
            auth(request)
            return redirect(main)
        
        else:
            not_valid = 'Неверный пароль'
            return render(request, 'registration.html',  {'not_valid_regist': not_valid})
        
    else:
        return render(request, 'registration.html')
    

def main(request):
    res = pzzle.objects.all()
    name = request.session.get("is_auth", "Не авторизован")
    return render(request, 'main.html',  {'puzzle': res, "username": name})

def out(request):
    logout(request)
    # return redirect(index)
    return redirect(main)


def card(request, card_id):
    data = pzzle.objects.filter(id = card_id)
    if data:
        return render(request, "card.html", {'puzzle': data})
    else:
        return redirect(main)

def buy(request, card_id):
    data = pzzle.objects.filter(id = card_id)

    return render(request, "buy.html", {'puzzle': data})