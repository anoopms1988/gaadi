from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from console.login.models import Company

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        companies = Company.objects.exclude(is_active=False)
        return render(request, 'general/home.html', {'companies': companies})
