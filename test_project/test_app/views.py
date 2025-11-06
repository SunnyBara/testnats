from django.contrib.auth import authenticate, get_user
from django.http import JsonResponse
from test_app.models import Dummy, Geo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.dispatch.dispatcher import Signal
from test_project.utils.jwt_utils import generate_jwt
from test_project.utils.nats_jwt_utils import generate_nats_jwt


@csrf_exempt
def handler(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name_value = data.get('name')
        color_value = data.get('color')

        if name_value and color_value:
            try:
                obj = Geo.objects.get(name=name_value)
            except Geo.DoesNotExist:
                return JsonResponse({'error': 'object not found'}, status=404)
            obj.color = color_value
            obj.save()
            return JsonResponse({'ok': 'updated'}, status=200)
    return JsonResponse({'error': 'invalid method'}, status=405)


def getGeo(request):
    if request.method == 'GET':
        data = list(Geo.objects.values('name', 'color'))
        return JsonResponse({'data': data}, status=200)
    return JsonResponse({'error': 'invalid method'}, status=405)


def createUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        Dummy.objects.create(name=name, password=password)
    return render(request, 'template.html')


def createGeo(request):
    message = ''
    if request.method == 'POST':
        name = request.POST.get('name').lower()
        color = request.POST.get('color')
        try:
            Geo.objects.get(name=name)
        except Geo.DoesNotExist:
            Geo.objects.create(name=name.lower(), color=color.lower())
            message = f'Geo {name} created'
        message = f'Geo {name} already exist'
    return render(request, 'geo.html', {'message': message})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(
            username=data['username'], password=data['password']
        )
        if user:
            token = generate_jwt(user.name)
            response = JsonResponse({'message': 'Logged in'})
            response.set_cookie(
                'access_token',
                token,
                httponly=False,
                samesite='Lax',
                secure=False,
            )
            return response
        return JsonResponse({'error': 'invalid credentials'}, status=400)
    return JsonResponse({'error': 'invalid method'}, status=405)


def user_view(request):
    user = None

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            user = Dummy.objects.filter(name=name).first()

    return render(request, 'user.html', {'user': user})


addressbook_signal = Signal()
user_signal = Signal()


@csrf_exempt
def mocktest(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event = data.get('event')
        match event.get('event').lower():
            case 'addressbook':
                addressbook_signal.send(sender=None)
                return JsonResponse({'status': 'signal envoyé'})
            case 'user':
                user_signal.send(sender=event.get('sender'))
                return JsonResponse({'status': 'signal envoyé'})
    return JsonResponse({'status': 'méthode non supportée'}, status=405)


@csrf_exempt
def nats_auth(request):
    token = generate_nats_jwt('test')
    return JsonResponse({'jwt': token, 'server': 'ws://127.0.0.1:9222'})
