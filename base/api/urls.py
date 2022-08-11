from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path('users/', views.getUsers),
    path('users/details/<str:pk>/', views.getUserDetail),
    path('users/create/', views.createUser),
    path('users/update/<int:pk>/', views.updateUser),
    path('users/delete/<int:pk>/', views.deleteUser),

    path('posts/', views.getPosts),
    path('posts/<int:pk>/', views.getPostDetail),
    path('posts/create/', views.createPost),
    path('posts/update/<int:pk>/', views.updatePost),
    path('posts/delete/<int:pk>/', views.deletePost),

    path('token/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('logout/', views.logout)
]
