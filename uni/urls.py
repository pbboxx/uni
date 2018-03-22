from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',  views.program_list , name='program_list'),
        url(r'^(?P<slug>[\w-]+)/$', views.program_detail, name="detail"),
        url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
        ]