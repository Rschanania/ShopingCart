from django.urls import path,include
from . import views




urlpatterns=[

    path('products/',views.pro,name="pro"),
    path('products/<int:pk>/',views.pro_details,name="pro_details"),
]