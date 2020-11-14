from django.urls import path
from smsapp import views

urlpatterns = [
    path('post/', views.my_view),
]

