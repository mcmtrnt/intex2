from django.db import models

# Create your models here.
class Doctor(models.Model):
    DoctorID = models.IntegerField(null=True)
    Fname = models.TextField(null=True)
    Lname = models.TextField(null=True)
    Gender = models.TextField(null=True)
    State = models.TextField(null=True)
    Credentials = models.TextField(null=True)
    Specialty = models.TextField(null=True)
    OpioidPrescriber = models.TextField(null=True)
    TotalPrescriptions = models.TextField(null=True)
    	
class Drug(models.Model):
    DrugName = models.TextField(null=True)
    IsOpioid = models.TextField(null=True)

class DrugDoctor(models.Model):
    DoctorID = models.IntegerField(null=True)
    DrugName = models.TextField(null=True)
    Qty = models.IntegerField(null=True)

class ExtraInfo(models.Model):
    DoctorID = models.IntegerField(null=True)
    NumOpioids = models.TextField(null=True)
    AtRisk = models.TextField(null=True)
    PrescriberScore = models.TextField(null=True)
