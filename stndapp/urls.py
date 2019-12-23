from django.urls import path
from . import views
from . import xmlviews

""" This holds the url patterns for each of the pages """
""" alot of the pages are using regex to find each selected course passed in through the url """

urlpatterns = [
    path('', views.index, name=''),
    path('standard/<str:standard>/', xmlviews.parStandards, name='standard'),
    path('persemester/', views.persemester, name='persemester'),
    path('schedulelist/', views.scheduleHtml, name='schedulelist'),
    path('assignmentlist/<str:schedule>/', views.scheduleTeachingAssignmentHtml, name='assignment'),
    path('assignmentlist/', views.assignmentlistHtml, name='assignmentlist'),
    path('courselist/', views.coursesHtml, name='courselist'),
    path('courselist/<str:course>/', views.syllabiXmlHTML, name='course'),
]
