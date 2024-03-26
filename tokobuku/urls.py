from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('<int:id>/', detail_view, name='detail'),
    path('contact/', contact_view, name='contact'),
    path('review/', create_review, name='review'),
    path('register/', register_view, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('cart/', cart_view, name='cart'),
]