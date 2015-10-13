from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import SpecificationView
from . import views

urlpatterns = [
    url(r'^adddimensions',login_required(SpecificationView.as_view()), name='adddimensions'),
    url(r'^$', login_required(SpecificationView.as_view())),
]