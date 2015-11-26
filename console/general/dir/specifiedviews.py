from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from console.general.models import User
from console.general.forms import UserForm


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

    def specific_user(self, request):
        user_id = request.POST.get('id')
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(request, 'general/editusers.html', {'form': form,'user_id':user_id})

    def delete_user(self, request):
        user_id = request.POST.get('id')
        user = User.objects.get(id=user_id)
        user.is_active = 0
        user.save()
        return HttpResponse('success')

    def edit_user(self, request):
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'User details edited.')
            return HttpResponseRedirect('/general/listusers')
        else:
            return HttpResponseRedirect('/general/listusers')
