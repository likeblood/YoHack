from django.shortcuts import render


'''  room page '''

def issues(request):
	return render(request, 'roomApp/issues.html')

def about_issue(request):
	return render(request, 'roomApp/about_issue.html')

def todo(request):
	return render(request, 'roomApp/todo.html')

def new_issue(request):
	return render(request, 'roomApp/newissue.html')
