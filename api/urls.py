from django.urls import path
from . import views

urlpatterns = [
	path('', views.UserList, name='user_list'),
	path('user-detail/<int:pk>', views.UserDetail, name='user_detail'),
	path('user-create/', views.UserCreate, name='user_create'),
	path('user-update/<int:pk>/', views.UserUpdate, name='user_update'),
	path('user-delete/<int:pk>/', views.UserDelete, name='user_delete'),
]