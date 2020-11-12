import uuid
from django.db import models
from django.contrib.auth.models import User


class CustomerGroups(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name_group = models.CharField(max_length=50)

    def __str__(self):
        return self.name_group


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    company = models.CharField(max_length=100)
    group_customer = models.ForeignKey(CustomerGroups, on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

