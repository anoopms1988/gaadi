from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'general/home.html', {})
