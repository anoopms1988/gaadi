from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from console.login.models import Company, Car, Variant
from console.general.models import InteriorFeatures, ExteriorFeatures, SafetyFeatures
from django.db.models import F, Count


class DashboardView(View):
    """
    Companies view and home page
    """

    def get(self, request, *args, **kwargs):
        companies = Company.objects.exclude(is_active=False)
        return render(request, 'general/home.html', {'companies': companies})

    def specific_company(self, request):
        """
        Specific company's carlist
        """
        company_id = request.GET.get('company_id')
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            company = None
        car_list = Car.objects.filter(company=company)
        return render(request, 'general/carlist.html', {'carlist': car_list, 'company': company})

    def specific_car(self, request):
        """
        Specific car's variantlist
        """
        car_id = request.GET.get('car_id')
        try:
            car = Car.objects.get(id=car_id)
        except Company.DoesNotExist:
            car = None
        diesel_variants = Variant.objects.filter(car=car).filter(fuel_id=1)
        petrol_variants = Variant.objects.filter(car=car).filter(fuel_id=2)
        return render(request, 'general/variantlist.html',
                      {'diesel_variants': diesel_variants, 'petrol_variants': petrol_variants, 'car': car})

    def specific_variant(self, request):
        """
        Specific variant's details
        """
        variant_id = request.GET.get('variant_id')
        try:
            variant = Variant.objects.get(id=variant_id)
        except Variant.DoesNotExist:
            variant = None
        try:
            interiorfeatures = InteriorFeatures.objects.get(variant=variant)
        except InteriorFeatures.DoesNotExist:
            interiorfeatures = None
        try:
            exteriorfeatures = ExteriorFeatures.objects.get(variant=variant)
        except ExteriorFeatures.DoesNotExist:
            exteriorfeatures = None
        try:
            safetyfeatures = SafetyFeatures.objects.get(variant=variant)
        except SafetyFeatures.DoesNotExist:
            safetyfeatures = None
        return render(request, 'general/variantdetails.html',
                      {'variant': variant, 'interiorfeatures ': interiorfeatures,
                       'exteriorfeatures': exteriorfeatures, 'safetyfeatures': safetyfeatures})
