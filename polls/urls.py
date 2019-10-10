from django.urls import path
from . import views
from . import xmlviews

urlpatterns = [
    path('index/', views.index, name=''),
    path('acmcs/', xmlviews.parStandards, name='acmcs'),
    path('persemester/', views.persemester, name='persemester'),
    path('schedule/', xmlviews.parSchedule, name='schedule'),
    path('assignments/', xmlviews.parTeachingAssignment, name='assignment'),
    path('courselist/', views.coursesHtml, name='courselist'),
    path('courselist/<str:course>/', xmlviews.parCourses, name='course'),
]