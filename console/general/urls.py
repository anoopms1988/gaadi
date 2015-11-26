from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from .views import SpecificationView,EngineView,BrakeView,CapacityView,MileageView,PriceView,SteeringView,WheelView,InteriorFeaturesView, \
                    ExteriorFeaturesView,SafetyFeaturesView

from . import views
from console.general.dir import specifiedviews
from console.general.dir.specifiedviews import InsuranceView,UserView

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
    url(r'^editprice',login_required(views.PriceView().edit_price), name='editprice'),
    url(r'^addprice',login_required(PriceView.as_view()), name='addprice'),
    url(r'^addsteering',login_required(SteeringView.as_view()), name='addsteering'),
    url(r'^specificsteering',login_required(views.SteeringView().specific_steering), name='specificsteering'),
    url(r'^editsteering',login_required(views.SteeringView().edit_steering), name='editsteering'),
    url(r'^addwheel',login_required(WheelView.as_view()), name='addwheel'),
    url(r'^specificwheel',login_required(views.WheelView().specific_wheel), name='specificwheel'),
    url(r'^editwheel',login_required(views.WheelView().edit_wheel), name='editwheel'),
    url(r'^interiorfeatures',login_required(InteriorFeaturesView.as_view()), name='interiorfeatures'),
    url(r'^exteriorfeatures',login_required(ExteriorFeaturesView.as_view()), name='exteriorfeatures'),
    url(r'^safetyfeatures',login_required(SafetyFeaturesView.as_view()), name='safetyfeatures'),
    url(r'^insurance',login_required(InsuranceView.as_view()), name='insurance'),
    url(r'^listusers',login_required(UserView.as_view()),name='listusers'),
    url(r'^deleteuser',login_required(specifiedviews.UserView().delete_user),name='deleteuser'),
    url(r'^specificuser',login_required(specifiedviews.UserView().specific_user), name='specificuser'),
    url(r'^edituser',login_required(specifiedviews.UserView().edit_user), name='edituser'),
    url(r'^$', login_required(SpecificationView.as_view())),
]