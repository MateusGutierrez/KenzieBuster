from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenRefreshView.as_view()),
]
