from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from console.general.models import User


class InsuranceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accessories/listenquiries.html', {})


class UserView(View):
    """
    Class view to deal with user management
    """
    def get(self, request, *args, **kwargs):
        users_list = User.objects.exclude(is_active=False)
        paginator = Paginator(users_list, settings.PAGINATION_LIMIT)
        page = request.GET.get('page')
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'general/listusers.html', {'users': users})

    def delete_user(self,request):
        user_id = request.POST.get('id')
        user = User.objects.get(id=user_id )
        user.is_active = 0
        user.save()
        return HttpResponse('success')