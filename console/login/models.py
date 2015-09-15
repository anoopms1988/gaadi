from django.db import models


class Company(models.Model):

    class Meta:
        db_table = 'companies'

    def __str__(self):
        pass

    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
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

    CHOICES = (('1', 'Honda'),)

    name = models.CharField(max_length=100,blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    company = models.ForeignKey(Company)
    cartype = models.ForeignKey(CarType)
    description = models.CharField(max_length=100)

    def __str__(self):
    	return str(self.name)
