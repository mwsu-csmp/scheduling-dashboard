from django.urls import path

from . import views
from . import xmlviews
from polls.views import *
#from polls.xmlviews import *


urlpatterns = [
    path('', views.index, name='index'),   
    path('acmcs/', xmlviews.parStandards, name='acmcs'),
    path('persemester/', views.persemester, name='persemester'),
    path('courselist/', views.courselist, name='courselist'),
    path('courselist/ACT102/', xmlviews.parACT102, name='ACT102'),
    path('courselist/ACT211/', xmlviews.parACT211, name='ACT211'),
    path('courselist/ACT301/', xmlviews.parACT301, name='ACT301'),
    path('courselist/ACT302/', xmlviews.parACT302, name='ACT302'),
    path('courselist/ACT311/', xmlviews.parACT311, name='ACT311'),
    path('courselist/ACT324/', xmlviews.parACT324, name='ACT324'),
    path('courselist/ACT405/', xmlviews.parACT405, name='ACT405'),
    path('courselist/ACT476/', xmlviews.parACT476, name='ACT476'),
    path('courselist/CSC184/', xmlviews.parCSC184, name='CSC184'),
    path('courselist/CSC201/', xmlviews.parCSC201, name='CSC201'),
    path('courselist/CSC208/', xmlviews.parCSC208, name='CSC208'),
    path('courselist/CSC245/', xmlviews.parCSC245, name='CSC245'),
    path('courselist/CSC246/', xmlviews.parCSC246, name='CSC246'),
    path('courselist/CSC254/', xmlviews.parCSC254, name='CSC254'),
    path('courselist/CSC264/', xmlviews.parCSC264, name='CSC264'),
    path('courselist/CSC274/', xmlviews.parCSC274, name='CSC274'),
    path('courselist/CSC285/', xmlviews.parCSC285, name='CSC285'),
    path('courselist/CSC289/', xmlviews.parCSC289, name='CSC289'),
    path('courselist/CSC294/', xmlviews.parCSC294, name='CSC294'),
    path('courselist/CSC305/', xmlviews.parCSC305, name='CSC305'),
    path('courselist/CSC328/', xmlviews.parCSC328, name='CSC328'),
    path('courselist/CSC345/', xmlviews.parCSC345, name='CSC345'),
    path('courselist/CSC346/', xmlviews.parCSC346, name='CSC346'),
    path('courselist/CSC386/', xmlviews.parCSC386, name='CSC386'),
    path('courselist/CSC400/', xmlviews.parCSC400, name='CSC400'),
    path('courselist/CSC406/', xmlviews.parCSC406, name='CSC406'),
    path('courselist/CSC410/', xmlviews.parCSC410, name='CSC410'),
    path('courselist/CSC445/', xmlviews.parCSC445, name='CSC445'),
    path('courselist/CSC450/', xmlviews.parCSC450, name='CSC450'),
    path('courselist/CSC451/', xmlviews.parCSC451, name='CSC451'),
    path('courselist/CSC484/', xmlviews.parCSC484, name='CSC484'),
    path('courselist/CSC550/', xmlviews.parCSC550, name='CSC550'),
    path('courselist/CSC570/', xmlviews.parCSC570, name='CSC570'),
    path('courselist/CSC580/', xmlviews.parCSC580, name='CSC580'),
    path('courselist/CSC590/', xmlviews.parCSC590, name='CSC590'),
    path('courselist/CSC615/', xmlviews.parCSC615, name='CSC615'),
    path('courselist/CSC625/', xmlviews.parCSC625, name='CSC625'),
    path('courselist/CSC630/', xmlviews.parCSC630, name='CSC630'),
    path('courselist/CSC635/', xmlviews.parCSC635, name='CSC635'),
    path('courselist/CSC650/', xmlviews.parCSC650, name='CSC650'),
    path('courselist/CSC660/', xmlviews.parCSC660, name='CSC660'), 
]

