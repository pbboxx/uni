from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
        url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
        url(r'^$',  views.home_dash , name='home_dash'),
        url(r'^profile/$', views.profile_dash, name='profile_dash'),
        url(r'^career/$', views.career, name='career'),
        url(r'^job/$', views.job, name='job'),
        url(r'^degree/$', views.degree,name='degree' ),
        ]

