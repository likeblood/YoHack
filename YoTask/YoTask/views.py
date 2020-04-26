from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from YoTask.models import Lobby, Room, Task
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


import datetime
import random


''' registration '''

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('lobby/')
    else:
        return HttpResponseRedirect('accounts/login/')


''' menu '''

@csrf_exempt
def join_lobby(request):
    if request.method == "POST":
        if request.POST.get('pin'):
            pin = request.POST.get('pin')
            try:
                lobby_id = Lobby.objects.filter(lobby_password=pin)[0].id
                lobby = Lobby.objects.filter(id=lobby_id)[0]
                lobby.users.add(request.user)
                lobby.save()

                lobby_id = Lobby.objects.filter(lobby_password=int(pin))[0].id

                lobby = Lobby.objects.filter(id=lobby_id).all()

                lobby[0].users.add(request.user)

                return render(request, "YoTask/include/joinLobby/joinLobbyInput.html",
                              { "lobby_id": lobby_id,
                                "pin": pin})
            except:
                return render(request, "YoTask/include/joinLobby/joinLobbyInput.html",
                              {"error": "Мы не нашли лобби с таким пином"})
        
        elif request.POST.get('lobby_name'):

            # generate and check pin
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            pin =''
            for i in range(6):
                pin += random.choice(chars)

            try:
                lobby = Lobby.objects.filter(lobby_password=pin)[0]
                while lobby.id:
                    pin =''
                    for i in range(6):
                        pin += random.choice(chars)
                    lobby = Lobby.objects.filter(lobby_password=pin)[0]
            except:
                pass

            lobby_name = request.POST['lobby_name']
            lobby_password = pin

            lobby = Lobby(
                creater=request.user,
                lobby_name=lobby_name,
                lobby_password=lobby_password,
            )

            lobby.save()
            lobby.users.add(request.user)
            lobby.save()

            ''' ADD HERE NEEDFUL AGRUMENTS '''
            # context = {
            #     'rooms': [],
            #     'users': lobby.users,
            #     'user_id': request.user.id
            # }

            return render(request, "YoTask/include/joinLobby/createLobbyInput.html",
                          {"lobby": lobby,
                           "pin": pin})

    return render(request, "YoTask/joinLobby.html")




''' in-lobby '''

def lobby(request, lobby_id):
    lobby = Lobby.objects.filter(id=lobby_id).all()
    rooms = Room.objects.all()

    context = {
        'lobby': lobby[0],
        'rooms': rooms,
    }

    return render(request, "YoTask/lobby.html", context)


@csrf_exempt
def join_room(request):
    if request.method == "POST":
        if request.POST.get('room_name') and\
        request.POST.get('room_description'):

            # generate and check pin
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            pin =''
            for i in range(6):
                pin += random.choice(char)

            try:
                room = Room.objects.filter(room_password=pin)[0]
                while room.id:
                    pin =''
                    for i in range(6):
                        pin += random.choice(chars)
                    room = Room.objects.filter(room_password=pin)[0]
            except:
                pass

            room_name = request.POST['room_name']
            room_description = request.POST['room_description']
            room_password = pin

            room = Room(
                        creater=request.user,
                        room_name=room_name,
                        room_description=room_description,
                        room_password=room_password
                        )
            room.save()
            room.users.add(request.user)
            room.save()

            ''' ADD HERE NEEDFUL AGRUMENTS '''
            # context = {
            #     'rooms': [],
            #     'users': room.users,
            #     'user_id': request.user.id
            # }

            return render(request, "YoTask/include/joinRoom/joinRoomInput.html",
                         {"room_id": room_id,
                          "pin" : pin})

        elif request.POST.get('room_name'):
            room_name = request.POST['room_name']
            room = Room.objects.filter(room_name=room_name)[0]
            room.users.add(request.user)
            room.save()

            return render(request, "YoTask/include/joinRoom/joinRoomInput.html",
              { "room_id": room.id})

        elif request.POST.get('pin'):
            pin = request.POST.get('pin')
            try:
                room = Room.objects.filter(room_password=pin)[0]
                room_id = room.id
                room.add(request.user)
                room.save()
                return render(request, "YoTask/include/joinRoom/joinRoomInput.html",
                              { "room_id": room_id,
                                "pin" : pin})
            except:
                return render(request, "YoTask/include/joinRoom/joinRoomInput.html",
                              {"error": "Мы не нашли комнату с таким пином"})

    return render(request, "YoTask/joinRoom.html")



''' in-room '''

def issues(request, room_id):
    room = Room.objects.filter(id=room_id).all()
    tasks = Task.objects.filter(room_id=room_id).order_by('date')

    context = {
        'tasks': tasks,
        'users': room.users,
        'user_id': request.user.id
    }

    render(request, "YoTask/room.html", context)


@csrf_exempt
def create_issue(request, lobby_id, room_id):
    lobby = Lobby.objects.filter(id=lobby_id).all()
    room = lobby.objects.filter(id=room_id).all()
    if request.method == "POST":
        if request.POST.get('asignee') and request.POST.get('task_title') \
                and request.POST.get('task_description'):
            task_title = request.POST['task_title']
            task_description = request.POST['task_description']
            task_date = datetime().now()
            asignee = request.POST['asignee']
            is_done = False
            issue = Task(
                author=request.user.name,
                task_title=task_title,
                task_description=task_description,
                task_date=task_date,
                is_done=is_done,
                asignee=asignee
            )
            room.tasks.add(issue)
    room.save()
    issue.save()

    context = {
        'tasks': room.tasks,
        'users': room.users,
        'user_id': request.user.id
    }

    render(request, "YoTask/room.html", context)


def about_issue(request, issue_id):
    issue = Task.objects.filter(id=issue_id)
    context = {
        'author': issue.author,
        'asignee': issue.asignee,
        'title': issue.task_title,
        'description': issue.task_description,
        'date': issue.date
    }

    render(request, "YoTask/about_issue.html", context)


