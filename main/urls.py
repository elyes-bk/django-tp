from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("site/<int:pk>/", views.site_detail, name="site_detail"),

]
