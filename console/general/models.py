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

    variant = models.ForeignKey(Variant)
    mileage_highway = models.CharField(max_length=100, blank=True, null=True)
    mileage_city = models.CharField(max_length=100, blank=True, null=True)
    mileage_overall = models.CharField(max_length=100, blank=True, null=True)


class Price(models.Model):

    class Meta:
        db_table = 'price'

    variant = models.ForeignKey(Variant)
    showroom_price = models.CharField(max_length=100, blank=True, null=True)
    onroad_price = models.CharField(max_length=100, blank=True, null=True)


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
    CHOICES = ((1, 'Yes'),
               (0, 'NO'))
    variant = models.ForeignKey(Variant)
    power_steering = models.CharField(max_length=2,choices=CHOICES,default=0)
    power_windows = models.CharField(max_length=2,choices=CHOICES,default=0)
    anti_pinch = models.CharField(max_length=2,choices=CHOICES,default=0)
    air_con = models.CharField(max_length=2,choices=CHOICES,default=0)
    audio_system = models.CharField(max_length=2,choices=CHOICES,default=0)
    electric_mirrors = models.CharField(max_length=2,choices=CHOICES,default=0)
    deffoger=models.CharField(max_length=2,choices=CHOICES,default=0)
    leather_seats=models.CharField(max_length=2,choices=CHOICES,default=0)
    reversing_camera=models.CharField(max_length=2,choices=CHOICES,default=0)
    bluetooth_connectivity=models.CharField(max_length=2,choices=CHOICES,default=0)
    cruise_control=models.CharField(max_length=2,choices=CHOICES,default=0)
    remote_boot_release=models.CharField(max_length=2,choices=CHOICES,default=0)
    chilled_glovebox=models.CharField(max_length=2,choices=CHOICES,default=0)
    rear_ac_vents=models.CharField(max_length=2,choices=CHOICES,default=0)
    keyless_start_stop_button=models.CharField(max_length=2,choices=CHOICES,default=0)
    electric_foldable_mirrors=models.CharField(max_length=2,choices=CHOICES,default=0)
    tachometer=models.CharField(max_length=2,choices=CHOICES,default=0)
    arm_rest=models.CharField(max_length=2,choices=CHOICES,default=0)
    steering_controls=models.CharField(max_length=2,choices=CHOICES,default=0)
    driver_info_display=models.CharField(max_length=2,choices=CHOICES,default=0)
    foot_rest=models.CharField(max_length=2,choices=CHOICES,default=0)
    driver_seat_height_adjust=models.CharField(max_length=2,choices=CHOICES,default=0)
    power_seats=models.CharField(max_length=2,choices=CHOICES,default=0)