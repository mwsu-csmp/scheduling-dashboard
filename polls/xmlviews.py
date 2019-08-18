from polls.views import *

##All of these def's return a HttpResponse. They are not sent to a template

#finds acm-cs.xml file. Called from urls.py
def parStandards(request):
    path = 'curriculum/mwsu_curriculum/standards/'
    for filename in os.listdir(path):
     if not filename.endswith('acm-cs.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseStandardsXml(request, fullname)
     print('i got this one: '+filename)
    return xml

#finds schedule.xml file. Called from urls.py
def parSchedule(request):
    path = 'curriculum/mwsu_curriculum/schedules/'
    for filename in os.listdir(path):
     if not filename.endswith('schedule.xml'): continue
     fullname = os.path.join(path, filename)
     xml = parseSchedule(request, fullname)
     print('i got this one: '+filename)
    return xml

#finds the requested course xml file. Called from urls.py
def parCourses(request, course):
    path = 'curriculum/mwsu_curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith(course + '.xml'): continue
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml
