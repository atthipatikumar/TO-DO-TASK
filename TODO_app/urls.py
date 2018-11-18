from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register1, name='register2'),
    url(r'^$', views.register2, name='register1'),


]