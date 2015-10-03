from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import LoginView, CarView, VariantView, CompanyView,DealerView
from . import views

urlpatterns = [
    url(r'^login', LoginView.as_view()),
    url(r'^dashboard', login_required(views.LoginView().dashboard), name='dashboard'),
    url(r'^logout', views.LoginView().logout, name='logout'),
    url(r'^cardetails', login_required(CarView.as_view())),
    url(r'^cars', login_required(views.CarView().list_cars), name='cars'),
    url(r'^deletecar', login_required(
        views.CarView().delete_cars), name='deletecars'),
    url(r'^specificcar', login_required(
        views.CarView().specific_car), name='specificcar'),
    url(r'^editcar', login_required(views.CarView().edit_car), name='editcar'),
    url(r'^addvariant', login_required(VariantView.as_view()), name='addvariant'),
    url(r'^listcars', login_required(views.VariantView().specific_cars), name='listcars'),
    url(r'^listvariants', login_required(views.VariantView().list_variants), name='listvariants'),
    url(r'^deletevariant', login_required(views.VariantView().delete_variant), name='deletevariant'),
    url(r'^specificvariant', login_required(
        views.VariantView().specific_variant), name='specificvariant'),
    url(r'^editvariant', login_required(views.VariantView().edit_variant), name='editvariant'),
    url(r'^listcompanies', login_required(CompanyView.as_view()), name='listcompanies'),
    url(r'^addcompany', login_required(CompanyView.as_view()), name='addcompany'),
    url(r'^deletecompany', login_required(views.CompanyView().delete_company), name='deletecompany'),
    url(r'^specificcompany', login_required(views.CompanyView().specific_company), name='specificcompany'),
    url(r'^editcompany', login_required(views.CompanyView().edit_company), name='editcompany'),
    url(r'^mapcompany$', login_required(views.CompanyView().map_company), name='mapcompany'),
    url(r'^deletedealer$', login_required(views.DealerView().delete_dealer), name='deletedealer'),
     url(r'^adddealer', login_required(DealerView.as_view()), name='dddealer'),
    url(r'^', LoginView.as_view()),
]
