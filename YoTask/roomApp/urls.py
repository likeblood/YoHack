from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.tasksActive, name='room'),
    url(r'^$', views.tasksClosed, name='tasksClosed'),
    url(r'^$', views.tasksAll, name='tasksAll'),


    url(r'^$', views.toDoList, name='toDoList'),
    url(r'^$', views.Done, name='Done'),
]
