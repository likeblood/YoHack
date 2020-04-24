from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.tasks, name='tasks'),
    url(r'^$', views.tasksActive, name='tasksActive'),
    url(r'^$', views.tasksClosed, name='tasksClosed'),
    url(r'^$', views.tasksAll, name='tasksAll'),

    
    url(r'^$', views.toDoList, name='toDoList'),
    url(r'^$', views.Done, name='Done'),
]
