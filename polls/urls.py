from django.urls import path
from . import views
from . import xmlviews

urlpatterns = [
    path('index/', views.index, name=''),
    path('acmcs/', xmlviews.parStandards, name='acmcs'),
    path('persemester/', views.persemester, name='persemester'),
    path('schedulelist/<str:schedule>/', xmlviews.parSchedule, name='schedule'),
    path('schedulelist/', xmlviews.schedulelistHtml, name='schedulelist'),
    path('assignmentlist/<str:schedule>/', xmlviews.parTeachingAssignment, name='assignment'),
    path('assignmentlist/', views.assignmentlistHtml, name='assignmentlist'),
    path('courselist/', views.coursesHtml, name='courselist'),
    path('courselist/<str:course>/', xmlviews.parCourses, name='course'),
]