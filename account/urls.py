from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register



urlpatterns = [	
	path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
	path('register/', register, name='register'),
	path('', include('django.contrib.auth.urls')),
]