from django.contrib import admin
from .models import CustomerGroups, Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'name', 'company', 'unique_id']


class CustomerGroupAdmin(admin.ModelAdmin):
    list_display = ['name_group', 'owner', 'unique_group', 'id']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerGroups, CustomerGroupAdmin)

