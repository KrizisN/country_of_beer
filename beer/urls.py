from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('', views.BeerListView.as_view(), name='home'),
    path('detail/<slug:slug>/', views.BeerDetailView.as_view(), name='beer_detail'),
]