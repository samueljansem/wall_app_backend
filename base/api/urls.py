from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path('users/', views.getUsers, name='list_users'),
    path('users/details/<str:pk>/', views.getUserDetail, name='user_detail'),
    path('users/create/', views.createUser, name='signup'),
    path('users/update/<int:pk>/', views.updateUser, name='update_user'),
    path('users/delete/<int:pk>/', views.deleteUser, name='delete_user'),

    path('posts/', views.getPosts, name='list_posts'),
    path('posts/<int:pk>/', views.getPostDetail, name='post_detail'),
    path('posts/create/', views.createPost, name='create_post'),
    path('posts/update/<int:pk>/', views.updatePost, name='update_post'),
    path('posts/delete/<int:pk>/', views.deletePost, name='delete_post'),

    path('token/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
]
