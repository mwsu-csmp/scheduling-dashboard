from django.urls import path
from . import views
from . import xmlviews

""" This holds the url patterns for each of the pages """
""" alot of the pages are using regex to find each selected course passed in through the url """

urlpatterns = [
    path('', views.index, name=''),
    path('index/<str:ay>/', views.index, name='year-home'),
    path('standard/<str:ay>/<str:standard>/', xmlviews.parStandards, name='standard'),
#    path('persemester/<str:semester>/<Str:year>', views.persemester, name='persemester'),
    path('schedulelist/<str:ay>/', views.scheduleHtml, name='schedulelist'),
    path('assignmentlist/<str:ay>/<str:semester>/', views.scheduleTeachingAssignmentHtml, name='assignment'),
    path('assignmentlist/<str:ay>/', views.assignmentlistHtml, name='assignmentlist'),
    path('catalog/<str:ay>/', views.catalog, name='courselist'),
    path('catalog/<str:ay>/<str:course>/', views.syllabus, name='course'),
]
