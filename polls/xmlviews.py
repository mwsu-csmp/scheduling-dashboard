from polls.views import *

def parStandards(request):
    path = 'curriculum/mwsu_curriculum/standards/'
    for filename in os.listdir(path):
     if not filename.endswith('acm-cs.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseStandardsXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parSchedule(request):
    path = 'curriculum/mwsu_curriculum/schedules/'
    for filename in os.listdir(path):
     if not filename.endswith('schedule.xml'): continue
     fullname = os.path.join(path, filename)
     xml = parseSchedule(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCourses(request, course):
    path = 'curriculum/mwsu_curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith(course + '.xml' ): continue
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml