from django.db import models
import os

def generate_filename(self, filename):
    extension = os.path.splitext(filename)[1]
    changed_name = self.name + extension
    url = "companies/logos/%s/%s" % (self.name, changed_name)
    return url

def generate_carlogo(self, filename):
    extension = os.path.splitext(filename)[1]
    changed_name = self.name + extension
    url = "cars/logos/%s/%s" % (self.name, changed_name)
    return url

class Company(models.Model):

    class Meta:
        db_table = 'companies'

    name = models.CharField(max_length=100)
    logo = models.FileField(verbose_name='Upload Logo', upload_to=generate_filename, blank=True, null=True)
    description = models.TextField()
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
    logo = models.FileField(verbose_name='Upload image', upload_to=generate_carlogo, blank=True, null=True)
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
    cylinders = models.PositiveIntegerField(null=True)
    valvespercylinder = models.PositiveIntegerField(null=True)
    valvemechanism = models.CharField(max_length=100)
    cylinderconfiguration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Dealer(models.Model):
    class Meta:
        db_table = 'dealers'

    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    phonenumber = models.CharField(max_length=100, blank=False)
    mobilenumber = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    email = models.CharField(max_length=100, blank=False)
    openinghours = models.CharField(max_length=100, blank=False)
    token = models.CharField(max_length=100, blank=True)



class Assistance(models.Model):
    class Meta:
        db_table = 'road_assistance'

    company = models.ForeignKey(Company)
    contact_details = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
