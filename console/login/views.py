from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, CarForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Company, CarType, Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings


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

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html', {'form': CarForm})

    def post(self, request, *args, **kwargs):
        form = CarForm(request.POST)
        if form.is_valid:
            company = request.POST.get('company')
            cartype = request.POST.get('cartype')
            name = request.POST.get('name')
            description = request.POST.get('description')
            if company and cartype and name:
                car = Car()
                car.company = Company.objects.get(id=company)
                car.cartype = CarType.objects.get(id=cartype)
                car.name = name
                car.description = description
                car.save()
                messages.success(request, 'Car details added.')
                return HttpResponseRedirect('/console/dashboard/')

            return render(request, 'dashboard.html', {'form': form})
        else:
            return render(request, 'dashboard.html', {'form': form})

    def list_cars(self, request):
        cars_list = Car.objects.exclude(is_active=False)
        paginator = Paginator(cars_list, settings.PAGINATION_LIMIT)
        page = request.GET.get('page')
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            cars = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            cars = paginator.page(paginator.num_pages)

        return render(request, 'listcars.html', {'cars': cars})

    def delete_cars(self, request):
        car_id = request.POST.get('id')
        car = Car.objects.get(id=car_id)
        car.is_active = 0
        car.save()
        return HttpResponse('success')
