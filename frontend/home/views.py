from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from console.login.models import Company, Car, Variant
from console.general.models import InteriorFeatures, ExteriorFeatures, SafetyFeatures
from django.db.models import F, Count
from django.forms.models import model_to_dict


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
            car_id  =variant.car.id
            car = Car.objects.get(id=car_id)
            diesel_variants = Variant.objects.filter(car=car).filter(fuel_id=1).exclude(id=variant_id)
            petrol_variants = Variant.objects.filter(car=car).filter(fuel_id=2).exclude(id=variant_id)
        except Variant.DoesNotExist:
            variant = None
            diesel_variants = None
            petrol_variants = None
        try:
            interiorfeatures = InteriorFeatures.objects.get(variant=variant)
            interiorfeatures_dict = model_to_dict(interiorfeatures, fields=[], exclude=["id", "variant"])
        except InteriorFeatures.DoesNotExist:
            interiorfeatures = None
            interiorfeatures_dict = None
        try:
            exteriorfeatures = ExteriorFeatures.objects.get(variant=variant)
            exteriorfeatures_dict = model_to_dict(exteriorfeatures, fields=[], exclude=["id", "variant"])
        except ExteriorFeatures.DoesNotExist:
            exteriorfeatures = None
            exteriorfeatures_dict = None
        try:
            safetyfeatures = SafetyFeatures.objects.get(variant=variant)
            safetyfeatures_dict = model_to_dict(safetyfeatures, fields=[], exclude=["id", "variant"])
        except SafetyFeatures.DoesNotExist:
            safetyfeatures = None
            safetyfeatures_dict = None
        # return HttpResponse(interiorfeatures._meta.get_field_by_name('power_steering')[0].verbose_name.title())
        return render(request, 'general/variantdetails.html',
                      {'variant': variant, 'interiorfeatures_dict': interiorfeatures_dict,
                       'exteriorfeatures_dict': exteriorfeatures_dict,'safetyfeatures_dict':safetyfeatures_dict ,
                       'exteriorfeatures': exteriorfeatures, 'safetyfeatures': safetyfeatures,
                       'interiorfeatures': interiorfeatures,'diesel_variants':diesel_variants,'petrol_variants':petrol_variants})
