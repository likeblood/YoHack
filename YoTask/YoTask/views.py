from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('lobby/')
    else:
        return HttpResponseRedirect('accounts/login/')


def join_lobby(request):
    print("SUCK")
    return render(request, "YoTask/wrapper.html")


#
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
