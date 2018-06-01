from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^cricket_center/$', views.CricketCenterIndexView, name="cricket_center"),
]
