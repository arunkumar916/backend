from django.urls import path
from . import views
urlpatterns=[
    path('post/', views.postenroll,name='postenroll'),
    path('get/',views.getEnroll,name='getenroll' ),
    
]