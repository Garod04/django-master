from django.contrib import admin
from .models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

    def __str__(self):
        return self.name


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value')
    search_fields = ('model',)
    list_filter = ('brand', 'factory_year', 'model_year')

    def __str__(self):
        return self.model

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)