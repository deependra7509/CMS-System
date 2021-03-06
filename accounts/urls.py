from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlspatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardsView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
]