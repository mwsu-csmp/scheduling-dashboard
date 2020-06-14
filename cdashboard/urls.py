from django.urls import path
from . import views

""" This holds the url patterns for each of the pages """
""" alot of the pages are using regex to find each selected course passed in through the url """

urlpatterns = [
    path('', views.index, name=''),
    path('index/<str:ay>/', views.index, name='year-home'),
    path('catalog/<str:ay>/', views.catalog, name='catalog'),
    path('catalog/<str:ay>/<str:course>/', views.syllabus, name='course'),
    path('load/<str:ay>/', views.load, name='load'),
    path('offerings/<str:ay>/', views.offerings, name='offerings'),
    path('schedule/<str:ay>/<str:semester>', views.schedule, name='schedule'),
    path('standards/<str:ay>', views.standards, name='standards'),
    path('standard/<str:ay>/<str:standard_id>', views.standard, name='standard'),
    path('standard/<str:ay>/<str:standard_id>/<str:program_id>', views.standard, name='standard'),
]
