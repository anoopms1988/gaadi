from django.db import models
from console.login.models import Variant


class Dimensions(models.Model):
    class Meta:
        db_table = 'dimensions'

    variant = models.ForeignKey(Variant)
    length = models.CharField(max_length=100, blank=False)
    width = models.CharField(max_length=100, blank=False)
    height = models.CharField(max_length=100, blank=False)
    wheelbase = models.CharField(max_length=100, blank=True, null=True)
    bootspace = models.CharField(max_length=100, blank=True, null=True)
    kerbweight = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Brake(models.Model):
    class Meta:
        db_table = 'brakes'

    variant = models.ForeignKey(Variant)
    rear_brakes = models.CharField(max_length=100, blank=False)
    front_brakes = models.CharField(max_length=100, blank=False)


class Capacity(models.Model):
    class Meta:
        db_table = 'capacity'

    variant = models.ForeignKey(Variant)
    seating_capacity = models.PositiveIntegerField(null=True)
    tank_capacity = models.CharField(max_length=100, blank=True, null=True)


class Mileage(models.Model):
    class Meta:
        db_table = 'mileage'

    variant = models.ForeignKey(Variant, related_name='mileage')
    mileage_highway = models.CharField(max_length=100, blank=True, null=True)
    mileage_city = models.CharField(max_length=100, blank=True, null=True)
    mileage_overall = models.CharField(max_length=100, blank=True, null=True)


class Price(models.Model):
    class Meta:
        db_table = 'price'

    variant = models.ForeignKey(Variant, related_name='price')
    showroom_price = models.CharField(max_length=100, blank=True, null=True)
    onroad_price = models.CharField(max_length=100, blank=True, null=True)
    emi = models.CharField(max_length=100, blank=True, null=True)


class Steering(models.Model):
    class Meta:
        db_table = 'steering'

    variant = models.ForeignKey(Variant)
    turning_radius = models.CharField(max_length=100, blank=True, null=True)
    steering_type = models.CharField(max_length=100, blank=True, null=True)


class Wheel(models.Model):
    class Meta:
        db_table = 'wheel'

    variant = models.ForeignKey(Variant)
    wheelsize = models.CharField(max_length=100, blank=True, null=True)
    wheeltype = models.CharField(max_length=100, blank=True, null=True)


class InteriorFeatures(models.Model):
    class Meta:
        db_table = 'interior_features'

    variant = models.ForeignKey(Variant)
    power_steering = models.BooleanField(default=False)
    power_windows = models.BooleanField(default=False)
    anti_pinch = models.BooleanField(default=False)
    air_con = models.BooleanField(default=False)
    audio_system = models.BooleanField(default=False)
    audio_system = models.BooleanField(default=False)
    electric_mirrors = models.BooleanField(default=False)
    deffoger = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    reversing_camera = models.BooleanField(default=False)
    bluetooth_connectivity = models.BooleanField(default=False)
    cruise_control = models.BooleanField(default=False)
    remote_boot_release = models.BooleanField(default=False)
    chilled_glovebox = models.BooleanField(default=False)
    rear_ac_vents = models.BooleanField(default=False)
    keyless_start_stop_button = models.BooleanField(default=False)
    electric_foldable_mirrors = models.BooleanField(default=False)
    tachometer = models.BooleanField(default=False)
    arm_rest = models.BooleanField(default=False)
    steering_controls = models.BooleanField(default=False)
    driver_info_display = models.BooleanField(default=False)
    foot_rest = models.BooleanField(default=False)
    driver_seat_height_adjust = models.BooleanField(default=False)
    power_seats = models.BooleanField(default=False)


class ExteriorFeatures(models.Model):
    class Meta:
        db_table = 'exterior_features'

    variant = models.ForeignKey(Variant)
    keyless_entry = models.BooleanField(default=False)
    rear_wiper = models.BooleanField(default=False)
    rain_sensing_wipers = models.BooleanField(default=False)
    alloy_wheels = models.BooleanField(default=False)
    roof_rails = models.BooleanField(default=False)
    projector_lamps = models.BooleanField(default=False)
    fog_lights = models.BooleanField(default=False)
    moon_roof = models.BooleanField(default=False)
    auto_headlamps = models.BooleanField(default=False)
    steel_rims = models.BooleanField(default=False)
    rear_spoiler = models.BooleanField(default=False)
    chrome_grille = models.BooleanField(default=False)
    daytime_running_lamps = models.BooleanField(default=False)


class SafetyFeatures(models.Model):
    class Meta:
        db_table = 'safety_features'

    variant = models.ForeignKey(Variant)
    abs = models.BooleanField(default=True)
    airbags = models.BooleanField(default=True)
    immobilizer = models.BooleanField(default=True)
    hill_control = models.BooleanField(default=True)
    central_locking = models.BooleanField(default=True)
    ebd = models.BooleanField(default=True)
    child_safety_lock = models.BooleanField(default=True)
    traction_control = models.BooleanField(default=True)
    hill_descent = models.BooleanField(default=True)
    esp = models.BooleanField(default=True)
    wheel_drive = models.BooleanField(default=True)


class User(models.Model):
    """
    Model to define registered users
    """

    class Meta:
        db_table = 'users'

    user_name = models.CharField(max_length=100,blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100,blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
