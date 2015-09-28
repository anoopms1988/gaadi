from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, CarForm, VariantForm, CompanyForm
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
        if form.is_valid():
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
        if form.is_valid():
            car = form.save(commit=False)
            car.company = form.cleaned_data['company']
            car.cartype = form.cleaned_data['cartype']
            car.save()
            messages.success(request, 'Car details added.')
            return HttpResponseRedirect('/console/dashboard/')
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
        company_id = car.company.id
        cartype_id = car.cartype.id
        form = CarForm(instance=car, initial={'company': company_id, 'cartype': cartype_id})
        return render(request, 'editcars.html', {'form': form, 'car_id': car_id})

    def edit_car(self, request):
        car_id = request.POST.get('car_id')
        car = Car.objects.get(pk=car_id)
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.company = form.cleaned_data['company']
            car.cartype = form.cleaned_data['cartype']
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
        if form.is_valid():
            variant = form.save(commit=False)
            variant.car = form.cleaned_data['car']
            variant.fuel = form.cleaned_data['fuel']
            variant.save()
            messages.success(request, 'Variant details added.')
            return HttpResponseRedirect('/console/addvariant/')
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
        car_id = variant.car.id
        fuel_id = variant.fuel.id
        form = VariantForm(initial={'company': company_id, 'car': car_id, 'fuel': fuel_id}, instance=variant)
        return render(request, 'editvariant.html', {'form': form, 'variant_id': variant_id})

    def edit_variant(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        form = VariantForm(request.POST, instance=variant)
        if form.is_valid():
            variant = form.save(commit=False)
            variant.car = form.cleaned_data['car']
            variant.fuel = form.cleaned_data['fuel']
            variant.save()
            messages.success(request, 'Car details edited.')
            return HttpResponseRedirect('/console/listvariants')
        else:
            return HttpResponseRedirect('/console/listvariants')


class CompanyView(View):
    'View for dealing with company manipulation'

    def get(self, request, *args, **kwargs):
        all_companies = Company.objects.exclude(is_active=False)
        return render(request, 'companies.html', {'all_companies': all_companies, 'form': CompanyForm})

    def add_company(self, request):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/console/listcompanies/')
        else:
            return HttpResponseRedirect('/console/listcompanies/')

    def delete_company(self, request):
        company_id = request.POST.get('id')
        company = Company.objects.get(id=company_id)
        company.is_active = 0
        company.save()
        return HttpResponse('success')

    def specific_company(self, request):
        company_id = request.POST.get('id')
        company = Company.objects.get(id=company_id)
        form = CompanyForm(instance=company)
        return render(request, 'editcompany.html', {'form': form,'company_id':company_id })
