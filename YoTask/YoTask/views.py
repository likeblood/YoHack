from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/admin/')
    else:
        return HttpResponseRedirect('/accounts/login/')
