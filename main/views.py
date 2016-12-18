from django.shortcuts import render
from django.http import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class MainView(TemplateView):
	template_name = "main/main.html"

def login_user(request):
    #redirect_to = request.GET['next']
    logout(request)
    username = password = server = ''
    if request.POST:
        webmail = request.POST['webmail']
        password = request.POST['password']
        server = request.POST['server']
        user = authenticate(webmail=webmail, password=password, server=server)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'main/login.html', {'invalid_auth': 1})
    return render(request, 'main/login.html', {})