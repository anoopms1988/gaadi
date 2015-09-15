from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, CarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Company, CarType, Car


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

    def dashboard(self, request):
        form = CarForm()
        return render(request, 'dashboard.html', {'form': form})

    def logout(self, request):
        logout(request)
        return HttpResponseRedirect('/console/login/')


class CarView(View):

    'Class for dealing with car details manipulation'

    def post(self, request, *args, **kwargs):
        form = CarForm(request.POST)
        if form.is_valid:
            company = request.POST.get('company')
            cartype = request.POST.get('cartype')
            name = request.POST.get('name')
            description=request.POST.get('description')
            if company and cartype and name:
                car = Car()
                car.company = Company.objects.get(id=company)
                car.cartype = CarType.objects.get(id=cartype)
                car.name = name
                car.description=description
                car.save()
                messages.success(request,'Car details added.')
                return HttpResponseRedirect('/console/dashboard/')

            return render(request, 'dashboard.html', {'form': form})
        else:
            return render(request, 'dashboard.html', {'form': form})
