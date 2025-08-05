# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
 name = models.CharField(max_length=100)
 description = models.TextField()
 # Additional fields
 country = models.CharField(max_length=50, blank=True, null=True)
 founded = models.IntegerField(blank=True, null=True)
 
 def __str__(self):
     return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
 # Many-to-One relationship with CarMake
 car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
 
 # Required fields
 name = models.CharField(max_length=100)
 
 # Type choices
 CAR_TYPES = [
     ('SEDAN', 'Sedan'),
     ('SUV', 'SUV'),
     ('WAGON', 'Wagon'),
     ('COUPE', 'Coupe'),
     ('HATCHBACK', 'Hatchback'),
     ('CONVERTIBLE', 'Convertible'),
     ('PICKUP', 'Pickup Truck'),
     ('VAN', 'Van'),
     ('SPORTS', 'Sports Car'),
     ('TRUCK', 'Truck')
 ]
 type = models.CharField(max_length=15, choices=CAR_TYPES, default='SUV')
 
 # Year with validators
 year = models.IntegerField(
     default=2023,
     validators=[
         MinValueValidator(2015),
         MaxValueValidator(2023)
     ]
 )
 
 # Additional fields
 dealer_id = models.IntegerField()
 color = models.CharField(max_length=50, blank=True, null=True)
 price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
 mileage = models.IntegerField(blank=True, null=True)
 
 def __str__(self):
     return f"{self.car_make.name} {self.name}"