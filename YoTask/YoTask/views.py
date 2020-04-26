from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from YoTask.models import Lobby, Room, Task
from usersApp.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from datetime import datetime
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
        # join lobby with a password
        if request.POST.get('pin'):
            pin = request.POST.get('pin')
            try:
                lobby = Lobby.objects.filter(lobby_password=pin)[0]

                lobby.users.add(request.user)

                lobby.save()


                return render(request, "YoTask/include/joinLobby/joinLobbyInput.html",
                              {"lobby_id": lobby.id,
                               "pin": pin})
            except:
                return render(request, "YoTask/include/joinLobby/joinLobbyInput.html",
                              {"error": "Мы не нашли лобби с таким пином"})

        # create lobby
        elif request.POST.get('lobby_name'):

            # generate and check pin
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            pin = ''
            for i in range(6):
                pin += random.choice(chars)

            try:
                lobby = Lobby.objects.filter(lobby_password=pin)[0]
                while lobby.id:
                    pin = ''
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


@csrf_exempt
def lobby(request, lobby_id):
    lobby = Lobby.objects.filter(id=lobby_id).all()
    rooms = lobby[0].rooms.all()

    if request.method == "POST":
        if request.POST.get('add_room_name') and \
                request.POST.get('add_room_description'):

            # generate and check pin
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            pin = ''
            for i in range(6):
                pin += random.choice(chars)

            try:
                room = Room.objects.filter(room_password=pin)[0]
                while room.id:
                    pin = ''
                    for i in range(6):
                        pin += random.choice(chars)
                    room = Room.objects.filter(room_password=pin)[0]
            except:
                pass

            room_name = request.POST['add_room_name']
            room_description = request.POST['add_room_description']
            room_password = pin
            is_private = False
            if request.POST.get('add_is_private'):
                if request.POST['add_is_private'] == "false":
                    is_private = True

            room = Room(
                creater=request.user,
                is_private=is_private,
                room_name=room_name,
                room_description=room_description,
                room_password=room_password,
            )
            room.save()
            room.users.add(request.user)
            room.save()
            lobby[0].rooms.add(room)
            lobby[0].save()

            print(lobby[0])
            return render(request, "YoTask/include/lobby/rooms.html",
                          {"rooms": lobby[0].rooms.all(),
                           })

        # join room
        elif request.POST.get('room_name'):
            room_name = request.POST['room_name']
            room = Room.objects.filter(room_name=room_name)[0]
            room.users.add(request.user)
            room.save()

            return render(request, "YoTask/lobby.html",
                          {"room_id": room.id,
                           })

        # join private room with a password
        elif request.POST.get('pin'):
            pin = request.POST.get('pin')
            try:
                room = Room.objects.filter(room_password=pin)[0]
                room_id = room.id
                room.add(request.user)
                room.save()
                return render(request, "YoTask/lobby.html",
                              {"room_id": room_id,
                               "pin": pin,
                               })
            except:
                return render(request, "YoTask/lobby.html",
                              {"error": "Мы не нашли комнату с таким пином"})

    if request.method == "GET":
        if request.GET.get('searchRooms'):
            if request.GET.get('searchRooms')=="all":
                return render(request, "YoTask/include/lobby/rooms.html",
                          {"rooms": lobby[0].rooms.all()})
            else:
                search_rooms = request.GET.get('searchRooms')

                print(search_rooms)

                rooms = lobby[0].rooms.all()
                filtered_rooms = rooms.filter(room_name__contains=search_rooms)
                print(filtered_rooms)

                return render(request, "YoTask/include/lobby/rooms.html",
                              {"rooms": filtered_rooms})



    context = {
        'lobby': lobby[0],
        'rooms': rooms,
    }
    return render(request, "YoTask/lobby.html", context)


''' in-room '''

@csrf_exempt
def issues(request, room_id):
    room = Room.objects.filter(id=room_id).all()

    for i in Lobby.objects.all():
        if room[0] in i.rooms.all():
            lobby = i

    tasks = Task.objects.filter(room_id=room_id).order_by('date')

    if request.method == "POST":
        # create task
        if request.POST.get('asignee') and request.POST.get('task_title') \
                and request.POST.get('task_description'):

            task_title = request.POST['task_title']
            task_description = request.POST['task_description']
            task_date = datetime.now()
            asignee = User.objects.filter(id=request.POST['asignee']).all()[0]
            is_done = False
            issue = Task(
                author=request.user,
                task_title=task_title,
                task_description=task_description,
                date=task_date,
                is_done=is_done,
                asignee=asignee,
                room_id=room_id

            )
            print(issue)
            issue.save()
            room[0].tasks.add(issue)
            room[0].save()

        # mark task a done
        elif request.POST.get('issue_id') and \
                request.POST.get('is_done'):
            issue_id = request.POST['issue_id']
            task = Task.objects.filter(id=issue_id)[0]
            task.is_done = True
            task.save()
        context = {
            'tasks': tasks,
            'room': room[0],
            'lobby': lobby,
        }
        return render(request, "YoTask/include/room/tasks.html", context)
    if request.method == "GET":
        ''' filters '''
        if request.GET.get('date'):
            date = request.GET['date']
            tasks = tasks.order_by('date')
        if request.GET.get('author'):
            author = request.GET['author']
            tasks = tasks.filter(author=author)
        if request.GET.get('asignee'):
            asignee = request.GET['asignee']
            tasks = tasks.filter(asignee=asignee)

    context = {
        'tasks': tasks,
        'room': room[0],
        'lobby': lobby,
        'user_id': request.user.id
    }

    return render(request, "YoTask/tasks.html", context)


def about_issue(request, issue_id):
    issue = Task.objects.filter(id=issue_id)[0]

    context = {
        'author': issue.author,
        'asignee': issue.asignee,
        'title': issue.task_title,
        'description': issue.task_description,
        'date': issue.date
    }

    render(request, "YoTask/about_issue.html", context)


def todo(request, room_id):
    tasks = Task.objects.filter(asignee=request.user)

    if request.method == "GET":

        ''' filters '''
        if request.GET.get('date'):
            date = request.GET['date']
            tasks = tasks.order_by('date')
        if request.GET.get('author'):
            author = request.GET['author']
            tasks = tasks.filter(author=author)

    render(request, "YoTask/about_issue.html",
           {'tasks': tasks})


