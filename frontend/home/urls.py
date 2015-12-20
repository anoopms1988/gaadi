from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from . import views
from .views import DashboardView

urlpatterns = [
    url(r'^company',views.DashboardView().specific_company, name='company'),
    url(r'^car',views.DashboardView().specific_car, name='car'),
    url(r'^variant',views.DashboardView().specific_variant, name='variant'),
    url(r'^$',DashboardView.as_view(),name='home'),
]
