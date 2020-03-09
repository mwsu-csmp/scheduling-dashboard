import xml.dom.minidom as minidom

import jinja2
from lxml import etree
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mwsu_curriculum import *
from jinja2 import Environment, FileSystemLoader
from pkg_resources import resource_filename


file_loader = FileSystemLoader('templates')


def index(request, ay=None):
    """ finds and displays the index.jinja template """
    if ay:
        return render(request, "index.jinja", {'years': available_years(), 'ay': ay})
    return render(request, "index.jinja", {'years': available_years()})


def offerings(request, ay):
    """ retrieves a summary of all courses offered over a two year period """
    return render(request, "offerings.jinja",
            {'courses': load_syllabi(ay), 'hours_per_semester': hours_per_semester(ay), 'ay': ay})

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


def schedule(request, ay, semester):
    """ List teaching assignments for a single semester """
    if semester == 'fa':
        year = ay[2:4]
    else:
        year = ay[7:9]
    courses = load_schedule(semester, year)
    sections = []
    for course in courses:
        sections = sections + courses[course]
    sections = sorted(sections, 
            key=lambda section : section.course.subject + str(section.course.number) + str(section.section))

    bumped_sections = set()
    for section in sections:
        if not (section in bumped_sections):
            for section2 in sections:
                if section is not section2 and section.conflicts_with(section2):
                    bumped_sections.add(section2)

    for section in sections:
        if section.startTime:
          hour, minutes = map(int, section.startTime.split(':'))
          if hour < 8:
              hour += 12
          hour -= 7  # start at 8am
          minutes += hour*60
          section.startPos = minutes
          section.position = 1 if section in bumped_sections else 0

    roster = {}
    instructor_color= {}
    colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 
            'orange', 'chartreuse', 'azure', 'violet', 'salmon']
    i=0
    for instructor in load_roster(ay):
        roster[instructor.id] = instructor.name
        instructor_color[instructor.id] = colors[i]
        i += 1

    daypos = {
            'M': 1,
            'T': 2,
            'W': 3,
            'R': 4,
            'F': 5
    }
    return render(request, "teaching_assignments.jinja", 
            {'sections': sections, 'daypos': daypos, 'roster': roster, 
                'instructor_color': instructor_color, 'ay': ay})


def standards(request, ay):
    """lists available curriculum standards"""
    standards = load_standards()
    return render(request, "curriculum_standards.jinja", {"standards": standards, 'ay': ay})

# Parse and pull all data from the acm-cs.xml file and returns all info within an array.
# this is used because of no xsl for this xml file
def standard(request, standard, ay):
    """ parses Standards then sets the information inside of the file to a list, this list is passed to the Template """
    standard_id = standard
    standard = load_standard(standard_id)

    return render(request, "curriculum_standard.jinja", {"standard": standard, 'ay': ay})
