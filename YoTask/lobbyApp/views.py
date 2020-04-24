from django.shortcuts import render


def join_lobby(request):
	return render(request, 'roomApp/join_lobby.html')

def lobby(request):
	return render(request, 'roomApp/lobby.html')
