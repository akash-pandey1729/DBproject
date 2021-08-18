from django.db import models
import datetime

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

INCOME_GROUPS = (
    ('Low Income', 'Low Income'),
    ('Middle Income', 'Middle Income'),
    ('High Income', 'High Income'),
)

DISEASES = (
    ('D1', 'Cardiovascular Disease'),
    ('D2', 'Diabetes'),
    ('D3', 'Tumor'),
    ('D4', 'Obesity'),
    ('D5', 'Hyperlipidemia'),
    ('D5', 'Respiratory Disease'),
)

LIFESTYLE = (
    ('D1', 'Unhealthy Eating Habit'),
    ('D2', 'Smoking and Drinking'),
    ('D3', 'Burning Midnight Oil'),
    ('D4', 'Emotionally unstable'),
    ('D5', 'Regular Excercise'),
    ('D5', 'Practice Meditation'),
)

PRODUCTS = (
    ('P1', 'COVID-19 PROTECTION'),
    ('P2', 'HEALTH INSURANCE FOR SELF AND DEPENDENTS'),
    ('P3', 'HEALTH INSURANCE FOR PARENTS'),
    ('P4', 'HEALTH INSURANCE FOR EMPLOYEES'),
)

class Data(models.Model):
    """
    """
    Insurance_Product = models.CharField(max_length=100, choices=PRODUCTS,null = True, blank = True)
    First_name = models.CharField(max_length=255,null = True, blank = True)
    Last_Name = models.CharField(max_length=255,null = True, blank = True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null = True, blank = True)
    country = models.CharField(max_length=100)
    Income_Group = models.CharField(max_length=100, choices=INCOME_GROUPS,null = True, blank = True)
    Morbidity_History = models.CharField(max_length=100, choices=DISEASES, null = True, blank = True)
    Lifestyle_Variables = models.CharField(max_length=100, choices=LIFESTYLE,null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Application(models.Model):
    """
    """
    Insurance_Product = models.CharField(max_length=100, choices=PRODUCTS,null = True, blank = True)
    First_Name = models.CharField(max_length=255,null = True, blank = True)
    Last_Name  = models.CharField(max_length=255,null = True, blank = True)
    Contact_Number = models.CharField(max_length=255,null = True, blank = True)
    Residential_Address = models.CharField(max_length=500,null = True, blank = True)
    Zip_Code = models.CharField(max_length=255,null = True, blank = True)
    Date_of_Birth_mm_dd_yyyy = models.CharField(max_length=255,null = True, blank = True) #Doubt 
    Your_Age = models.PositiveSmallIntegerField(null = True, blank = True) # Calculate Age
    Sex = models.CharField(max_length=100, choices=GENDER_CHOICES, null = True, blank = True)
    SSN_or_TAX_ID = models.PositiveSmallIntegerField(null = True, blank = True)
    Country = models.CharField(max_length=100,null = True, blank = True)
    Income_Group = models.CharField(max_length=100, choices=INCOME_GROUPS,null = True, blank = True)
    Income = models.PositiveSmallIntegerField(null = True, blank = True)
    Morbidity_History = models.CharField(max_length=100, choices=DISEASES, null = True, blank = True)
    Lifestyle_Variables = models.CharField(max_length=100, choices=LIFESTYLE,null = True, blank = True)
    fkey_Do_Not_Change = models.ForeignKey(Data, on_delete = models.CASCADE,null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

