from django.contrib import admin
from .models import CustomerGroups,Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone_number','name','company']

# Register your models here.
admin.site.register(Customer,CustomerAdmin)
admin.site.register(CustomerGroups)