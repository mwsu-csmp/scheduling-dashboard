import xml.dom.minidom as minidom

import jinja2
from lxml import etree
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from mwsu_curriculum import *
from jinja2 import Environment, FileSystemLoader
from pkg_resources import resource_filename


file_loader = FileSystemLoader('templates')


def index(request, ay=None):
    """ finds and displays the index.jinja template """
    if ay:
        return render(request, "index.jinja", {'years': available_years(), 'ay': ay})
    return render(request, "index.jinja", {'years': available_years()})


def persemester(request, semester, year):
    """ Gets the objects from models.py and loads them into a template """
    courses = load_schedule(ay)
    return render(request, "persemester.jinja",
            {'courses': courses, 'hours_per_semester': hours_per_semester(ay), 'ay': ay})


def catalog(request, ay):
    return render(request, 'catalog.jinja', {'courses': load_syllabi(ay), 'ay': ay})


def syllabus(request, course, ay):
    """renders a course syllabus using the XSLT template in the curriculum lib"""
    xslt_doc = etree.parse(resource_filename('mwsu_curriculum', 'transformations/syllabus-to-html.xsl'))
    xslt_transformer = etree.XSLT(xslt_doc)
    coursexmlfile = resource_filename('mwsu_curriculum', 'syllabi/'+ay+'/'+course+'.xml')
    source_doc = etree.parse(coursexmlfile)
    output_doc = xslt_transformer(source_doc)
    return HttpResponse(output_doc)

def getSchedule(ay):
    """ Creates a list of all Schedule objects """
    scheduleList = list()
    for s in load_schedule(ay):
        for i in s:
            schedule = schedule_f(course=i[0], section_number=i[1], start_time=i[2],
                                  end_time=i[3], day=i[7], building_room=i[4], max=i[5],
                                  instructor=i[6])
            scheduleList.append(schedule)
    return scheduleList


def getAssignments(ay):
    """ Creates a list of all Assignment objects """
    assignmentlist = list()
    for s in load_assignments(ay):
        assignment = assignments(instructor=s[0], workloadhours=s[1])
        assignmentlist.append(assignment)
    return assignmentlist


def schedulelistHtml(request, ay):
    """ This goes through and grabs all of the schedules in the schedule folder and adds them to the list that
     will be displayed inside of the Template """
    schedulelist = list()
    path = resource_filename('mwsu_curriculum', 'schedules')
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        newfilename = filename.replace('.xml', "")
        schedulelist.append(newfilename)
    schedules = schedulelist
    return render(request, "schedulelist.jinja", {'schedules': schedules, 'ay': ay})


def scheduleHtml(request, ay):
    """ This gets the request and goes through the list of schedules, and deploys the corresponding
         Template """
    schedule = sorted(getSchedule(ay), key=lambda x: x.course, reverse=False)
    return render(request, "schedule.jinja", {'schedule': schedule, 'ay': ay})


def load(request, ay):
    """ determines faculty load for the given academic year """
    roster = load_roster(ay)
    fall = load_schedule('fa', ay[2:4])
    spring = load_schedule('sp', ay[7:9])
    for instructor in roster:
        instructor.load = 0
        instructor.fallSections = []
        for release in instructor.releases:
            instructor.load += instructor.releases[release]
        for course in fall:
            for section in fall[course]:
                if section.instructorId == instructor.id:
                    instructor.load += course.workload_hours
                    instructor.fallSections.append(section)
        instructor.springSections = []
        for course in spring:
            for section in spring[course]:
                if section.instructorId == instructor.id:
                    instructor.load += course.workload_hours
                    instructor.springSections.append(section)

    return render(request, "load.jinja", {'roster': roster, 'ay': ay})


def scheduleTeachingAssignmentHtml(request, semester, ay):
    """ This sets the chosen xml file and sets it to the xslt file. """
    getSchedule().sort(key=lambda x: x.instructor, reverse=False)
    assignment = sorted(getSchedule(), key=lambda x: x.instructor, reverse=False)
    additional_assignments = getAssignments(ay)
    for instructor in additional_assignments:
        print(instructor.instructor)
    courses = load_courses(ay)
    roster = load_roster(ay)
    total = 0
    final_total = 0
    currentinstructor = ""
    for instructor in assignment:
        if currentinstructor != instructor.instructor:
            final_total = total
            total = 0
            assignemnt_hours.append(final_total)
        for course in courses:
            currentinstructor = instructor.instructor
            if instructor.course == course.course:
                total = total + course.workloadhours
    assignemnt_hours.append(final_total)
    return render(request, "teaching_assignments.jinja", {'assignment': assignment, 'courses': courses,
                                                                'ay': ay,
                                                                'assignment_hours': assignemnt_hours,
                                                                'additional_assignments': additional_assignments})


# Parse and pull all data from the acm-cs.xml file and returns all info within an array.
# this is used because of no xsl for this xml file
def parseStandardsXml(request, standard, ay):
    """ parses Standards then sets the information inside of the file to a list, this list is passed to the Template """
    standardsXml = resource_filename('mwsu_curriculum', 'standards/'+standard+'.xml')
    xmldoc = minidom.parse(standardsXml)
    name = xmldoc.getElementsByTagName('name')
    body = xmldoc.getElementsByTagName('body')
    version = xmldoc.getElementsByTagName('version')
    knowledgeArea = xmldoc.getElementsByTagName('knowledgeArea')
    values = []
    for s in name:
        textvalue = s.firstChild.data
        values.append('Name: ' + textvalue)

    for s in body:
        textvalue = s.firstChild.data
        values.append('Body: ' + textvalue)

    for s in version:
        textvalue = s.firstChild.data
        values.append('Version: ' + textvalue)

    for s in knowledgeArea:
        namevalue = s.getAttribute('name')
        if not namevalue == "": continue
        idvalue = s.getAttribute('id')
        namevalue = s.getAttribute('name')
        values.append('Knowledge Area id: ' + idvalue)
        subKnowledgeArea = s.getElementsByTagName('knowledgeArea')
        for s in subKnowledgeArea:
            idvalue = s.getAttribute('id')
            namevalue = s.getAttribute('name')
            values.append('Knowledge Area ' + 'id: ' + idvalue + ' name: ' + namevalue)
            subTopics = s.getElementsByTagName('topic')
            subOutcomes = s.getElementsByTagName('outcome')
            for s in subTopics:
                textvalue = s.firstChild.data
                impvalue = s.getAttribute('importance')
                values.append(' topic importance: ' + impvalue + ': ' + textvalue)
            for s in subOutcomes:
                textvalue = s.firstChild.data
                impvalue = s.getAttribute('importance')
                values.append('outcome importance: ' + impvalue + ': ' + textvalue)

    return render(request, 'acmcs.jinja', {'values': values, 'ay': ay})
