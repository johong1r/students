from django.urls import path
from .views import login_custom, register_view, logout_view

urlpatterns = [
    path("login/", login_custom, name="login"),        
    path("register/", register_view, name="register"),  
    path("logout/", logout_view, name="logout"),        
]
