from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, CarForm, VariantForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from .models import Company, CarType, Car, Variant, Fuel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core import serializers


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/console/dashboard/')
        else:
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
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)

        return render(request, 'listcars.html', {'cars': cars})

    def delete_cars(self, request):
        car_id = request.POST.get('id')
        car = Car.objects.get(id=car_id)
        car.is_active = 0
        car.save()
        return HttpResponse('success')

    def specific_car(self, request):
        car_id = request.POST.get('id')
        car = Car.objects.get(id=car_id)
        form = CarForm(instance=car)
        return render(request, 'editcars.html', {'form': form, 'car_id': car_id})

    def edit_car(self, request):
        form = CarForm(request.POST)
        if form.is_valid:
            company = request.POST.get('company')
            cartype = request.POST.get('cartype')
            name = request.POST.get('name')
            description = request.POST.get('description')
            car_id = request.POST.get('car_id')
            if company and cartype and name:
                car = Car(id=car_id)
                car.company = Company.objects.get(id=company)
                car.cartype = CarType.objects.get(id=cartype)
                car.name = name
                car.description = description
                car.save()
                messages.success(request, 'Car details edited.')
                return HttpResponseRedirect('/console/cars')
        else:
            return HttpResponseRedirect('/console/cars')


class VariantView(View):
    'Class for dealing with car details manipulation'

    def get(self, request, *args, **kwargs):
        return render(request, 'variant.html', {'form': VariantForm})

    def post(self, request, *args, **kwargs):
        form = VariantForm(request.POST)
        if form.is_valid:
            name = request.POST.get('name')
            car_id = request.POST.get('car')
            fuel_id = request.POST.get('fuel')
            if name and car_id and fuel_id:
                variant = Variant()
                variant.name = name
                variant.car = Car.objects.get(id=car_id)
                variant.fuel = Fuel.objects.get(id=fuel_id)
                variant.is_active = True
                variant.save()
                messages.success(request, 'Variant details added.')
                return HttpResponseRedirect('/console/addvariant/')

            return render(request, 'variant.html', {'form': form})
        else:
            return render(request, 'variant.html', {'form': form})

    def specific_cars(self, request):
        company_id = request.POST.get('id')
        company = Company.objects.get(id=company_id)
        car_list = Car.objects.filter(company=company)
        data = serializers.serialize('json', car_list)
        return HttpResponse(data)

    def list_variants(self, request):
        variants_list = Variant.objects.exclude(is_active=False)
        paginator = Paginator(variants_list, settings.PAGINATION_LIMIT)
        page = request.GET.get('page')
        try:
            variants = paginator.page(page)
        except PageNotAnInteger:
            variants = paginator.page(1)
        except EmptyPage:
            variants = paginator.page(paginator.num_pages)

        return render(request, 'listvariants.html', {'variants': variants})

    def delete_variant(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        variant.is_active = 0
        variant.save()
        return HttpResponse('success')

    def specific_variant(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        company_id = variant.car.company.id
        form = VariantForm(initial={'company': company_id}, instance=variant)
        return render(request, 'editvariant.html', {'form': form, 'variant_id': variant_id})

    def edit_variant(self, request):
        form = VariantForm(request.POST)
        if form.is_valid:
            name = request.POST.get('name')
            car_id = request.POST.get('car')
            fuel_id = request.POST.get('fuel')
            variant_id = request.POST.get('variant_id')
            if name and car_id and fuel_id:
                variant = Variant(id=variant_id)
                variant.car = Car.objects.get(id=car_id)
                variant.fuel = Fuel.objects.get(id=fuel_id)
                variant.name = name
                variant.save()
                messages.success(request, 'Car details edited.')
                return HttpResponseRedirect('/console/listvariants')

        else:
            return HttpResponseRedirect('/console/listvariants')
