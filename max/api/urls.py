from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.register_user,name="register_user"),
    path("login/",views.logins,name="logins"),
    path("logout/",views.logout,name="logout"),
    path("home/",views.home,name="home"),
]
