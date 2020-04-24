from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.join_lobby, name='join_lobby'),          # page with lobby login and lobby creating
    url(r'^(\d+)/$', views.lobby, name='lobby'),              # lobby
]
