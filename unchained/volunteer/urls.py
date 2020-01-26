from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('home/', views.home, name='home'),
	path('user_stats/<uname>/', views.user_stats, name='user_stats'),
	path('create_user/<uname>/<nm>/<loc>', views.insert_user, name='insert_user'),
	path('login/<uname>', views.login, name='login'),
	path('map/<min_lat>/<max_lat>/<min_long>/<max_long>', views.events, name='events'),
]
