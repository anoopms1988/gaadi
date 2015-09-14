from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm,CarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Company,CarType


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'form': LoginForm})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/console/dashboard/')
                    else:
                        messages.add_message(
                            request, messages.WARNING, 'User is not active')
                else:
                    messages.add_message(
                        request, messages.WARNING, 'User dont exist')

            return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})

    def dashboard(self,request):
        all_companies=Company.objects.all()
        all_cartypes =CarType.objects.all()
        form =CarForm()
        return render(request,'dashboard.html',{'form':form,'companies':all_companies,'cartypes':all_cartypes})

    def logout(self,request):
        logout(request)
        return HttpResponseRedirect('/console/login/')


