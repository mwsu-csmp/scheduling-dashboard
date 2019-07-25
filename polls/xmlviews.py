import lxml
from polls.views import *

def parStandards(request):
    path = 'curriculum/standards/'
    for filename in os.listdir(path):
     if not filename.endswith('acm-cs.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseStandardsXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parSchedule(request):
    path = 'curriculum/schedules/'
    for filename in os.listdir(path):
     if not filename.endswith('schedule.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSchedule(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT102(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT102.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT211(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT211.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT301(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT301.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT302(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT302.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT311(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT311.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT324(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT324.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT405(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT405.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parACT476(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('ACT476.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC184(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC184.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC201(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC201.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC208(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC208.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC245(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC245.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC246(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC246.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC254(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC254.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC264(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC264.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC274(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC274.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC285(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC285.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC289(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC289.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC294(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC294.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC305(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC305.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC328(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC328.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC345(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC345.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC346(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC346.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC386(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC386.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC400(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC400.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC406(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC406.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC410(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC410.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC445(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC445.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC450(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC450.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC451(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC451.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC484(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC484.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC550(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC550.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC570(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC570.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC580(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC580.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC590(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC590.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC615(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC615.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC625(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC625.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC630(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC630.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC635(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC635.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC650(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC650.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml

def parCSC660(request):
    path = 'curriculum/syllabi/'
    for filename in os.listdir(path):
     if not filename.endswith('CSC660.xml'): continue 
     fullname = os.path.join(path, filename)
     xml = parseSyllabiXml(request, fullname)
     print('i got this one: '+filename)
    return xml
