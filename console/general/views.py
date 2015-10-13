from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core import serializers
from console.login.models import Company, CarType, Car, Variant, Fuel, Dealer, Assistance
from .models import Dimensions
from inspect import getmembers
from pprint import pprint


class SpecificationView(View):
    def get(self, request, *args, **kwargs):
        variant_id = request.GET.get('id')
        variant = Variant.objects.get(id=variant_id)
        try:
            dimensions = Dimensions.objects.get(variant=variant)
        except Dimensions.DoesNotExist:
            dimensions = None
        return render(request, 'general/specifications.html', {'variant': variant, 'dimensions': dimensions})
