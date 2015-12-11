from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from console.login.models import Company,Car

class DashboardView(View):
    """
    Companies view and home page
    """

    def get(self, request, *args, **kwargs):
        companies = Company.objects.exclude(is_active=False)
        return render(request, 'general/home.html', {'companies': companies})

    def specific_company(self, request):
        company_id=request.GET.get('company_id')
        company=Company.objects.get(id=company_id)
        car_list=Car.objects.filter(company=company)
        return render(request, 'general/carlist.html', {'carlist': car_list})


