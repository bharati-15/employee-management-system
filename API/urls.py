from django.urls import path
from django.urls import path, include
from .import views

from django.shortcuts import redirect
from .import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()

router.register('skill_api', views.Skillsviewset, basename='skill_api')
router.register('Dep_api', views.Departmentviewset, basename='Depart')
router.register('Emp1_api', views.Empviewset, basename='emp1_api')

urlpatterns = [
    path('',views.home, name='home'),
    path('api/',include(router.urls))
]
