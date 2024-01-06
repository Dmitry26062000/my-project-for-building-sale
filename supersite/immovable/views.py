import json
import matplotlib.pyplot as plt
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from immovable.models import Users, Home, application, contract, status
from datetime import date, timezone, timedelta
from django.conf import settings
import random
import string
from django.template.loader import render_to_string
from post_office.mail import send
from collections import Counter


def h(request, id):
    print(request.GET)

    return HttpResponse(f'<h1>Страница </h1><p>{id}</p>')


def adminka(request):
    return render(request, 'adminka.html')


def users(request):
    use = Users.objects.all()
    name = request.POST.get("username")
    pas = request.POST.get("password")

    for i in use:
        if i.username == name and i.password == pas and i.role_id == 2:
            tittle = i.username
            f = 'Контракты'
            s = ''
            d = 'Управляющая компания'
            e = ''
            j = ''
            ml = i.email
            datac = contract.objects.filter(Buyer_id=i.pk)
            app = application.objects.all()
            price=[]
            dta2 = []
            val2 = []
            datefpr = []
            slov={}
            slov2={}
        elif i.username == name and i.password == pas and i.role_id == 3:
            tittle = i.username
            f = ''
            s = 'Сотрудники'
            d = 'Управляющая компания'
            e = 'Отчеты'
            j = 'Заявки'
            ml = i.email
            datac = contract.objects.all()
            app = application.objects.all()
            dta2=[]
            val2=[]
            price=[]
            datefpr=[]
            slov={}
            slov2={}
    for i in datac:
        stt = status.objects.filter(pk=i.status_id)
        usr = Users.objects.filter(pk=i.Buyer_id)
        datt = i.dateOfSign.strftime("%m-%d")
        datt2=i.dateOfSign.strftime("%B")
        dat2=i.dateOfSign
        Crow=contract.objects.filter(dateOfSign=dat2).count()
        slov[datt]=Crow
        spr = 0
        if i.dateOfSign.strftime("%B")==datt2:
            spr+=i.Resprice
            slov2[datt2]=spr
    for k,qs in slov2.items():
        price.append(qs)
        datefpr.append(k)
    for i,n in slov.items():
        dta2.append(i)
        val2.append(n)
    ath = {
        'f': f,
        's': s,
        'tit': tittle,
        'data': datac,
        'em': ml,
        'd': d,
        'e': e,
        'j': j,
        'applicat': app,
        'stt': stt,
        'usr': usr,
        'dta':dta2[::-1],
        'val':val2[::-1],
        'datepr':datefpr[::-1],
        'prices':price[::-1]
    }
    return render(request, 'actuser.html', context=ath)


def clients(request):
    return render(request, 'clients.html')


def emp(request):
    return render(request, 'employees.html')


def reg(request):
    username = request.GET.get('username')
    email = request.GET.get('email')

    use = Users.objects.all()

    if username != '' or email != '':
        if username != '':
            use = Users.objects.filter(username=username)
            cUse = Users.objects.filter(username=username).count()
            context = {
                'use': use,
                'cout': cUse,
            }
        elif email != '':
            use = Users.objects.filter(email=email)
            cUse = Users.objects.filter(email=email).count()
            context = {
                'use': use,
                'cout': cUse,
            }
    else:
        cUse = Users.objects.all().count()
        context = {
            'use': use,
            'cout': cUse
        }
    return render(request, 'register.html', context=context)


def contr(request):
    return render(request, 'contracts.html')


def menu(request):
    Croom = request.GET.get("box")
    # area = request.GET.get("area")
    if Croom != '':
        h = Home.objects.filter(Croom=Croom)
        ch = Home.objects.filter(Croom=Croom).count()

    else:
        h = Home.objects.all()
        ch = Home.objects.all().count()
    context = {
        'home': h,
        'ch': ch
    }
    return render(request, 'menu.html', context=context)


def hello(request):
    return render(request, 'ht.html')


def regus(request):
    usname = request.POST.get('username', 'def')
    email = request.POST.get('email', 'pk')
    pas = request.POST.get('password', 'uhuih')
    Users.objects.create(username=usname, email=email, password=pas, role_id="2")
    emails = [email]

    me = 'Название компании <{}>'.format(settings.EMAIL_HOST_USER)
    subject = 'Тестовое письмо'

    now = timezone.now()
    delta_sec = -70  # Нужно, чтобы первое письмо было отправлено сразу же

    for email in emails:
        delta_sec += random.randint(60, 70)
        scheduled_time = now + timedelta(seconds=delta_sec)

        message = render_to_string('immovable/email.html', {'email': email, 'some_var': 'xxx'})
        headers = {'To': 'Получатель письма от компании  ЖК Орион'.format(email)}
        send(email, me, subject=subject,
             message=message, html_message=message,
             scheduled_time=scheduled_time, headers=headers)
    return render(request, 'registredus.html')


def finished(request):
    f = request.POST.get('username')
    s = request.POST.get('email')
    context = {
        'first': f,
        'second': s
    }
    if regus(request):
        return render(request, 'finished.html', context=context)
    else:
        return HttpResponse(f'''<h1>Error register<h1>''')


def uscrud(request):
    t = request.GET.get('unm')
    use = Users.objects.all()
    for i in use:
        if i.username == t:
            name = t
            mail = i.email
    context = {
        'tit': name,
        'mail': mail,
    }
    return render(request, 'crudus.html', context=context)


def app(request):
    id = request.GET.get('hom')
    h = Home.objects.get(pk=id)
    room = h.Croom
    area = h.area
    price = h.price
    ids = h.pk
    context = {
        'r': room,
        'a': area,
        'p': price,
        'ids': ids,
    }
    return render(request, 'application.html', context=context)


def sub(request):
    prof = request.POST.get('prs')
    newemail = request.POST.get('efirst', 'dimkapolozov@yandex.ru')
    password = ''
    try:
        for p in range(8):
            p = random.choice(string.ascii_letters)
            password += p
        application.objects.create(email=newemail, Home_id=prof)
        Users.objects.create(username=newemail, email=newemail, password=password, role_id='2')
        return render(request, 'subdata.html')
    except:
        return HttpResponse(
            '<body><script> alert("К сожалению, квартиру забронировали!Через секунду вы попадете на  главную страницу!"); let h=  window.setTimeout(function () {window.location.href = "/"}, 1500);</script></body>')


def createcon(request):
    usernm = request.GET.get('appmaiil')
    idenA = request.GET.get('iden')
    us = Users.objects.filter(username=usernm)
    stat = status.objects.all()
    a = application.objects.filter(pk=idenA)
    for i in a:
        h = Home.objects.filter(pk=i.Home_id)
    for u in h:
        Ipice = u.price
        Ipice += Ipice * 0.2
    for i in us:
        buid = i.pk
    data = {
        'iden': idenA,
        'buid': buid,
        'stat': stat,
        'iPrice': Ipice
    }
    return render(request, 'contract_crt.html', context=data)


def subcon(request):
    try:
        selectt = request.POST.get('status')
        aplication = request.POST.get('applic')
        datee = request.POST.get('date')
        client = request.POST.get('client')
        emp = request.POST.get('edenemp')
        Iprice = request.POST.get('Iprice')
        totalprice = int(round(float(Iprice), 0))
        contract.objects.create(dateOfSign=datee, Buyer_id=client, employee_id=emp, status_id=selectt,
                                appl_id=aplication, Resprice=totalprice)
        return render(request, 'subcon.html')
    except:
        return HttpResponse(
            '<body><script>alert("По данной заявке договор уже создан!"); let h= window.setTimeout(function () {window.location.href = "/"}, 1500);</script></body>')
