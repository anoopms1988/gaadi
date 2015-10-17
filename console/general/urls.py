from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import SpecificationView,EngineView,BrakeView
from . import views

urlpatterns = [
    url(r'^adddimensions',login_required(SpecificationView.as_view()), name='adddimensions'),
    url(r'^specificdimension',login_required(views.SpecificationView().specific_dimension), name='specificdimension'),
    url(r'^editdimensions',login_required(views.SpecificationView().edit_dimension), name='editdimensions'),
    url(r'^addengine',login_required(EngineView.as_view()), name='addengine'),
    url(r'^specificengine',login_required(views.EngineView().specific_engine), name='specificengine'),
    url(r'^editengine',login_required(views.EngineView().edit_engine), name='editengine'),
    url(r'^addbrake',login_required(BrakeView.as_view()), name='addbrake'),
    url(r'^$', login_required(SpecificationView.as_view())),
]