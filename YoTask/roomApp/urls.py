from django.conf.urls import url

urlpatterns = [
    url(r'^$',  views.rooms, name='rooms'),                                 # all rooms
    url(r'^(\d+)/issues/$', views.issues, name='issues'),                   # room issues
    url(r'^(\d+)/issues/(\d+)/$', views.about_issue, name='about_issue'),   # about issue
    url(r'^(\d+)/todo/$', views.todo, name='todo'),                         # user's todo
]
