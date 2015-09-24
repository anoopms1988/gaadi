from django.db import models


class Company(models.Model):
    class Meta:
        db_table = 'companies'

    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    description =models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class CarType(models.Model):
    class Meta:
        db_table = 'cartypes'

    cartype = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Car(models.Model):
    class Meta:
        db_table = 'cars'

    name = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    company = models.ForeignKey(Company)
    cartype = models.ForeignKey(CarType)
    description = models.CharField(max_length=100)


class Fuel(models.Model):
    class Meta:
        db_table = 'fueltype'

    name = models.CharField(max_length=100)


class Variant(models.Model):
    class Meta:
        db_table = 'variants'

    car = models.ForeignKey(Car)
    fuel = models.ForeignKey(Fuel, default=1)
    name = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Engine(models.Model):
    class Meta:
        db_table = 'engines'

    variant = models.ForeignKey(Variant)
    torque = models.CharField(max_length=100)
    displacement = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    cylinders = models.PositiveIntegerField()
    valvespercylinder = models.PositiveIntegerField()
    valvemechanism = models.CharField(max_length=100)
    cyclinderconfiguration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
