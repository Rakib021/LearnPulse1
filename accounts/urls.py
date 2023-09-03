from django.urls import path,include

from . import views



urlpatterns = [
    path('register/',views.register,name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user_login/',views.user_login, name='user_login'),
    path('accounts/profile/',views.profile,name='profile'),
    path('accounts/profile/update',views.profile_update,name='profile_update'),
    path('search/',views.search,name="search"),



] 
