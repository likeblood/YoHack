from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from YoTask.models import Lobby, Room, Task
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

import datetime

''' registration '''
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('lobby/')
    else:
        return HttpResponseRedirect('accounts/login/')


''' menu '''
@csrf_exempt
def create_lobby(request):
    try:
        max_lobby_password = int(Lobby.objects.order_by("-lobby_password").first()['lobby_password'])
    except:
        max_lobby_password = 0

    if request.method == "POST":
        if request.POST.get('lobby_name'):
            lobby_name = request.POST['lobby_name']
            lobby_password = [i for i in range(10000)][max_lobby_password + 1]
            lobby = Lobby(
                creator=request.user.id,
                lobby_name=lobby_name,
                lobby_password=lobby_password,
            )
        lobby.save()

    context = {
        'rooms': [],
        'users': [],
        'user_id': request.user.id
    }
    return render(request, "YoTask/lobby.html", context)


@csrf_exempt
def join_lobby(request):
    if request.method == "POST":
        if request.POST.get('pin'):
            pin = request.POST.get('pin')
            try:
                lobby_id = Lobby.objects.filter(lobby_password=pin).id
            except:
                return render(request, "YoTask/include/joinLobby/joinLobbyInput.html",
                              {"error": "Мы не нашли лобби с таким пином"})

        return HttpResponseRedirect('/lobby/{}/'.format(lobby_id))
    return render(request, "YoTask/joinLobby.html")


''' in-lobby '''
@csrf_exempt
def create_room(request, lobby_id):
    lobby = Lobby.objects.filter(id=lobby_id).all()
    if request.method == "POST":
        if request.POST.get('room_name') and request.POST.get('room_description'):
            room_name = request.POST['room_name']
            room_description = request.POST['room_description']

            room = Room(
                room_name=room_name,
                room_description=room_description
            )
            lobby.rooms.add(room)
    room.save()
    lobby.save()

    context = {
        'tasks': [],
        'users': [],
        'user_id': request.user.id
    }

    return render(request, "YoTask/room.html", context)


def lobby(request, lobby_id):
    lobby = Lobby.objects.filter(id=lobby_id).all()
    if lobby.creator.id == request.user.id:
        rooms = lobby.filter(id=lobby_id).rooms
    else:
        rooms = Room.objects.filter(users.id=request.user.id)

    context = {
        'rooms': rooms,
        'users': lobby.users,
        'user_id': request.user.id
    }

    return render(request, "YoTask/lobby.html", context)


@csrf_exempt
def join_room(request, room_id):
        return HttpResponseRedirect('/room/{}/'.format(room_id))



''' in-room '''
def issues(request, room_id):
    room = lobby.objects.filter(id=room_id).all()
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
    context = 
    {
        'author': issue.author,
        'asignee': issue.asignee,
        'title': issue.task_title,
        'description': issue.task_description
        'date': issue.date
    }

    render(request, "YoTask/about_issue.html", context)



# ''' tasks page '''
#
# def tasks(request):
#     return render(request, 'roomApp/room.html')
#
#
# def tasks(request):
#     return render(request, 'roomApp/tasksClosed.html')
#
#
# def tasks(request):
#     return render(request, 'roomApp/tasksAll.html')
#
#
# ''' To-Do user's page '''
#
# def tasks(request):
#     return render(request, 'roomApp/toDoList.html')
#
#
# def tasks(request):
#     return render(request, 'roomApp/Done.html')
