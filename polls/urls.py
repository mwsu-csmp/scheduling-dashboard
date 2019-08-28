from django.urls import path

from . import views
from . import xmlviews
from . import models

urlpatterns = [
    path('index/', views.index, name='index'),
    path('acmcs/', xmlviews.parStandards, name='acmcs'),
    path('persemester/', views.persemester, name='persemester'),
    path('schedule/', xmlviews.parSchedule, name='schedule'),
    path('courselist/', views.getCourses, name='courselist'),
    path('courselist/<str:course>/', xmlviews.parCourses, name='course'),
]