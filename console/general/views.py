from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core import serializers
from console.login.models import Company, CarType, Car, Variant, Fuel, Dealer, Assistance, Engine
from .models import Dimensions
from .forms import DimensionForm


class SpecificationView(View):

    def get(self, request, *args, **kwargs):
        variant_id = request.GET.get('id')
        variant = Variant.objects.get(id=variant_id)
        try:
            dimensions = Dimensions.objects.get(variant=variant)
        except Dimensions.DoesNotExist:
            dimensions = None
        try:
            engine = Engine.objects.get(variant=variant)
        except Engine.DoesNotExist:
            engine = None
        return render(request, 'general/specifications.html',
                      {'dimensionsform': DimensionForm, 'variant': variant, 'dimensions': dimensions, 'engine': engine})

    def post(self, request, *args, **kwargs):
        form = DimensionForm(request.POST)
        variant_id = request.POST.get('variant')
        variant = Variant.objects.get(id=variant_id)
        if form.is_valid():
            dimensions = form.save(commit=False)
            dimensions.variant = variant
            dimensions.save()
            messages.success(request, 'Car dimensions added.')

        return HttpResponseRedirect('/general/?id={0}'.format(variant_id))

    def specific_dimension(self, request):
        variant_id = request.POST.get('id')
        variant = Variant.objects.get(id=variant_id)
        dimension = Dimensions.objects.get(variant=variant)
        form = DimensionForm(instance=dimension)
        return render(request, 'general/specificdimension.html', {'form': form, 'variant_id': variant_id})

    def edit_dimension(self, request):
        variant_id = request.POST.get('variant_id')
        variant = Variant.objects.get(id=variant_id)
        dimension = Dimensions.objects.get(variant=variant)
        form = DimensionForm(request.POST, instance=dimension)
        if form.is_valid():
            dimension = form.save(commit=False)
            dimension.variant = variant
            dimension.save()
            messages.success(request, 'Car dimensions edited.')
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
        else:
            return HttpResponseRedirect('/general/?id={0}'.format(variant_id))
