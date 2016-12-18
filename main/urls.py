from django.conf.urls import url
from . import views
from views import MainView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name' : 'main/main.html'}, name='logout'),
	url(r'^$', MainView.as_view(), name='MainView'), #Stud Main Page (Landing Page)
]

