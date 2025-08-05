from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
 model = CarModel
 extra = 1  # Number of empty forms to display
 fields = ['name', 'type', 'year', 'dealer_id', 'color', 'price']

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
 list_display = ('car_make', 'name', 'type', 'year', 'dealer_id', 'price')
 list_filter = ('car_make', 'type', 'year')
 search_fields = ['name', 'car_make__name']
 ordering = ['car_make', 'name', 'year']
 fieldsets = [
     ('Car Information', {'fields': ['car_make', 'name', 'type', 'year']}),
     ('Dealer Information', {'fields': ['dealer_id']}),
     ('Additional Details', {'fields': ['color', 'price', 'mileage'], 'classes': ['collapse']}),
 ]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
 list_display = ('name', 'country', 'founded', 'description')
 search_fields = ['name', 'country']
 list_filter = ['country']
 inlines = [CarModelInline]  # This allows editing CarModels directly from CarMake admin page
 fieldsets = [
     ('Basic Information', {'fields': ['name', 'description']}),
     ('Additional Information', {'fields': ['country', 'founded'], 'classes': ['collapse']}),
 ]

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)