from django.shortcuts import render


''' tasks page '''

def tasks(request):
	return render(request, 'roomApp/room.html')

def tasks(request):
	return render(request, 'roomApp/tasksClosed.html')

def tasks(request):
	return render(request, 'roomApp/tasksAll.html')





''' To-Do user's page '''

def tasks(request):
	return render(request, 'roomApp/toDoList.html')


def tasks(request):
	return render(request, 'roomApp/Done.html')
