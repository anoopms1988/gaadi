from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from . import views
from .views import DashboardView

urlpatterns = [
    url(r'^$',DashboardView.as_view(),name='home'),
]
