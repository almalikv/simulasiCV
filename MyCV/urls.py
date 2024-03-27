from django.urls import path
from .views import *

urlpatterns = [
    path('mycv', mycv, name='mycv'),
]