from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.logout,name="logout"),
    path('updateProfile/',views.updateProfile,name='update_profile'),
]
