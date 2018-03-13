
from django.db import models



class Artists (models.Model):
    id = models.IntegerField(blank=False, null=False),  'primary_key=True'
    brand_name = models.CharField(max_length=20)
    manager = models.CharField(max_length=20)
    contact_number = models.IntegerField(blank=False, null=False)
    contact_email = models.EmailField(max_length=20)
    country = models.CharField(max_length=100)

class Customers  (models.Model):
    id = models.IntegerField(blank=False, null=False),  'primary_key=True'
    first_name = models.CharField(max_length=20),
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=False, null=False)
    street_adress = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    state = models.CharField(max_length= 20)
    country = models.CharField(max_length= 20)


class Stage_Details (models.Model):
    id = models.IntegerField(blank=False, null=False), 'primary_key=True'
    number_in_crew = models.IntegerField(blank=False, null=False)
    sound_checked = models.BooleanField()
    set_time = models.CharField(max_length=7)
    number_of_band_members = models.IntegerField(blank=False, null=False)
    photo = models.CharField(max_length=1000)

class Sponsors(models.Model):
    id = models.IntegerField(blank=False, null=False), 'primary_key=True'
    company_name = models.CharField(max_length=20)
    representative= models.CharField(max_length=20)
    contact_number = models.IntegerField(blank=False, null=False)
    contact_email = models.EmailField(max_length=20)
    donation = models.CharField(max_length=100)
