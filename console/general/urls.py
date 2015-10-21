from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from .views import SpecificationView,EngineView,BrakeView,CapacityView,MileageView,PriceView
from . import views

urlpatterns = [
    url(r'^adddimensions',login_required(SpecificationView.as_view()), name='adddimensions'),
    url(r'^specificdimension',login_required(views.SpecificationView().specific_dimension), name='specificdimension'),
    url(r'^editdimensions',login_required(views.SpecificationView().edit_dimension), name='editdimensions'),
    url(r'^addengine',login_required(EngineView.as_view()), name='addengine'),
    url(r'^specificengine',login_required(views.EngineView().specific_engine), name='specificengine'),
    url(r'^editengine',login_required(views.EngineView().edit_engine), name='editengine'),
    url(r'^addbrake',login_required(BrakeView.as_view()), name='addbrake'),
    url(r'^specificbrake',login_required(views.BrakeView().specific_brake), name='specificbrake'),
    url(r'^editbrake',login_required(views.BrakeView().edit_brake), name='editbrake'),
    url(r'^addcapacity',login_required(CapacityView.as_view()), name='addcapacity'),
    url(r'^specificcapacity',login_required(views.CapacityView().specific_capacity), name='specificcapacity'),
    url(r'^editcapacity',login_required(views.CapacityView().edit_capacity), name='editcapacity'),
    url(r'^addmileage',login_required(MileageView.as_view()), name='addmileage'),
    url(r'^specificmileage',login_required(views.MileageView().specific_mileage), name='specificmileage'),
    url(r'^editmileage',login_required(views.MileageView().edit_mileage), name='editmileage'),
    url(r'^specificprice',login_required(views.PriceView().specific_price), name='specificprice'),
    url(r'^$', login_required(SpecificationView.as_view())),
]