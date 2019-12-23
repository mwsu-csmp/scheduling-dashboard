import os
from . import views
from pkg_resources import resource_filename

##All of these def's return a HttpResponse. They are not sent to a template

def parStandards(request, standard):
    return views.syllabiXmlHTML(request, resource_filename('mwsu_curriculum', 'standards/'+standard+'.xml'))

def parSchedule(request, schedule):
    return views.syllabiXmlHTML(request, resource_filename('mwsu_curriculum', 'schedules/'+schedule+'.xml'))

def parTeachingAssignment(request, schedule):
    return views.syllabiXmlHTML(request, resource_filename('mwsu_curriculum', 'schedules/'+schedule+'.xml'))

