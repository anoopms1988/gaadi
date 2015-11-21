from django import forms
from .models import Dimensions, Brake, Capacity, Mileage, Price, Steering, Wheel, InteriorFeatures,ExteriorFeatures
from console.login.models import Engine
from django.utils.safestring import mark_safe


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimensions
        fields = ['length', 'width', 'height',
                  'wheelbase', 'bootspace', 'kerbweight']

    length = forms.CharField(label='Length',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Length'}))
    width = forms.CharField(label='Width',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Width'}))
    height = forms.CharField(label='Height',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Height'}))
    wheelbase = forms.CharField(label='Wheelbase', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wheelbase'}))
    bootspace = forms.CharField(label='Bootspace', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bootspace'}))
    kerbweight = forms.CharField(label='Kerbweight', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kerbweight'}))


class EngineForm(forms.ModelForm):
    class Meta:
        model = Engine
        fields = ['torque', 'displacement', 'power', 'cylinders', 'valvespercylinder', 'valvemechanism',
                  'cylinderconfiguration']

    torque = forms.CharField(label='Torque', required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Torque'}))
    displacement = forms.CharField(label='Displacement', required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Displacement'}))
    power = forms.CharField(label='Power', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Power'}))
    cylinders = forms.CharField(label='Cylinders', required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cylinders'}))
    valvespercylinder = forms.CharField(label='Valvespercylinder', required=False,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': 'Valvespercylinder'}))
    valvemechanism = forms.CharField(label='Valvemechanism', required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Valvemechanism'}))
    cylinderconfiguration = forms.CharField(label='Cylinder configuration', required=False,
                                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Cylinder configuration'}))


class BrakeForm(forms.ModelForm):
    class Meta:
        model = Brake
        fields = ['rear_brakes', 'front_brakes']

    rear_brakes = forms.CharField(label='Rear brakes', required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rear brakes'}))
    front_brakes = forms.CharField(label='Front brakes', required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Front brakes'}))


class CapacityForm(forms.ModelForm):
    class Meta:
        model = Capacity
        fields = ['seating_capacity', 'tank_capacity']

    seating_capacity = forms.CharField(label='Seating capacity', required=False,
                                       widget=forms.TextInput(
                                           attrs={'class': 'form-control', 'placeholder': 'Seating capacity'}))
    tank_capacity = forms.CharField(label='Tank capacity', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Tank capacity'}))


class MileageForm(forms.ModelForm):
    class Meta:
        model = Mileage
        fields = ['mileage_highway', 'mileage_city', 'mileage_overall']

    mileage_highway = forms.CharField(label='Mileage highway', required=False,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'placeholder': 'Mileage highway'}))
    mileage_city = forms.CharField(label='Mileage city', required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Mileage city'}))
    mileage_overall = forms.CharField(label='Mileage overall', required=False,
                                      widget=forms.TextInput(
                                          attrs={'class': 'form-control', 'placeholder': 'Mileage overall'}))


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['showroom_price', 'onroad_price']

    showroom_price = forms.CharField(label='Showroom price', required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Showroom price'}))
    onroad_price = forms.CharField(label='Onroad price', required=False,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Onroad price'}))


class SteeringForm(forms.ModelForm):
    class Meta:
        model = Steering
        fields = ['turning_radius', 'steering_type']

    turning_radius = forms.CharField(label='Turning radius', required=False,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'Turning radius'}))
    steering_type = forms.CharField(label='Steering type', required=False,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Steering type'}))


class WheelForm(forms.ModelForm):
    class Meta:
        model = Wheel
        fields = ['wheelsize', 'wheeltype']

    wheelsize = forms.CharField(label='Wheel size', required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Wheel size'}))
    wheeltype = forms.CharField(label='Wheel type', required=False,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Wheel type'}))


class InteriorfeaturesForm(forms.ModelForm):
    class Meta:
        model = InteriorFeatures
        fields = ['power_steering', 'power_windows', 'anti_pinch', 'air_con', 'audio_system', 'electric_mirrors',
                  'deffoger', 'leather_seats', 'reversing_camera', 'bluetooth_connectivity', 'cruise_control',
                  'remote_boot_release', 'chilled_glovebox',
                  'rear_ac_vents', 'keyless_start_stop_button', 'electric_foldable_mirrors', 'tachometer', 'arm_rest',
                  'steering_controls', 'driver_info_display', 'foot_rest', 'driver_seat_height_adjust', 'power_seats']

    power_steering = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                            choices=((False, 'No'), (True, 'Yes')),
                                            widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                            label='Power steering')

    power_windows = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                           choices=((False, 'No'), (True, 'Yes')),
                                           widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                           label='Power windows')

    anti_pinch = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                        choices=((False, 'No'), (True, 'Yes')),
                                        widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Anti Pinch')
    air_con = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'No'), (True, 'Yes')),
                                     widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                     label='Air conditioner')
    audio_system = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                          choices=((False, 'No'), (True, 'Yes')),
                                          widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                          label='Audio System')
    electric_mirrors = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                              choices=((False, 'No'), (True, 'Yes')),
                                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                              label='Electric Mirrors')
    deffoger = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                      choices=((False, 'No'), (True, 'Yes')),
                                      widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Deffoger')
    leather_seats = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                           choices=((False, 'No'), (True, 'Yes')),
                                           widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                           label='Leather seats')
    reversing_camera = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                              choices=((False, 'No'), (True, 'Yes')),
                                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                              label='Reversing camera')
    bluetooth_connectivity = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                    choices=((False, 'No'), (True, 'Yes')),
                                                    widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                                    label='Bluetooth connectivity')
    cruise_control = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                            choices=((False, 'No'), (True, 'Yes')),
                                            widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                            label='Cruise control')
    remote_boot_release = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                 choices=((False, 'No'), (True, 'Yes')),
                                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                                 label='Remote boot release')
    chilled_glovebox = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                              choices=((False, 'No'), (True, 'Yes')),
                                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                              label='Chilled glovebox')
    rear_ac_vents = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                           choices=((False, 'No'), (True, 'Yes')),
                                           widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                           label='Rear ac vents')
    keyless_start_stop_button = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                       choices=((False, 'No'), (True, 'Yes')),
                                                       widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                                       label='Keyless start stop button')
    electric_foldable_mirrors = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                       choices=((False, 'No'), (True, 'Yes')),
                                                       widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                                       label='Electric foldable mirrors')
    tachometer = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                        choices=((False, 'No'), (True, 'Yes')),
                                        widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Tachometer')
    arm_rest = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                      choices=((False, 'No'), (True, 'Yes')),
                                      widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Arm rest')
    steering_controls = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                               choices=((False, 'No'), (True, 'Yes')),
                                               widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                               label='Steering controls')
    driver_info_display = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                 choices=((False, 'No'), (True, 'Yes')),
                                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                                 label='Driver info display')
    foot_rest = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                       choices=((False, 'No'), (True, 'Yes')),
                                       widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Foot rest')
    driver_seat_height_adjust = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                                       choices=((False, 'No'), (True, 'Yes')),
                                                       widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                                       label='Driver seat height adjust')
    power_seats = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                         choices=((False, 'No'), (True, 'Yes')),
                                         widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                         label='Power seats')


class ExteriorfeaturesForm(forms.ModelForm):
    class Meta:
        model = ExteriorFeatures
        fields = ['keyless_entry', 'rear_wiper', 'rain_sensing_wipers', 'alloy_wheels', 'roof_rails', 'projector_lamps',
                  'fog_lights', 'moon_roof', 'auto_headlamps', 'steel_rims', 'rear_spoiler',
                  'chrome_grille', 'daytime_running_lamps',
                  ]

    keyless_entry = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                            choices=((False, 'No'), (True, 'Yes')),
                                            widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                            label='Keyless entry')

    rear_wiper = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                           choices=((False, 'No'), (True, 'Yes')),
                                           widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                           label='Rear wiper')

    rain_sensing_wipers = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                        choices=((False, 'No'), (True, 'Yes')),
                                        widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Rain sensing wipers')
    alloy_wheels = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'No'), (True, 'Yes')),
                                     widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                     label='Alloy wheels')
    roof_rails = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                          choices=((False, 'No'), (True, 'Yes')),
                                          widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                          label='Roof rails')
    projector_lamps = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                              choices=((False, 'No'), (True, 'Yes')),
                                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                              label='Projector lamps')
    fog_lights = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                            choices=((False, 'No'), (True, 'Yes')),
                                            widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                            label='Fog lights')

    moon_roof = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                           choices=((False, 'No'), (True, 'Yes')),
                                           widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                           label='Moon roof')

    auto_headlamps = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                        choices=((False, 'No'), (True, 'Yes')),
                                        widget=forms.RadioSelect(renderer=HorizontalRadioRenderer), label='Auto headlamps')
    steel_rims = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'No'), (True, 'Yes')),
                                     widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                     label='Steel rims')
    rear_spoiler = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                          choices=((False, 'No'), (True, 'Yes')),
                                          widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                          label='Rear spoiler')
    chrome_grille = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                              choices=((False, 'No'), (True, 'Yes')),
                                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                              label='Chrome grille')
    daytime_running_lamps = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                              choices=((False, 'No'), (True, 'Yes')),
                                              widget=forms.RadioSelect(renderer=HorizontalRadioRenderer),
                                              label='Daytime running lamps')
