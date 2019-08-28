import xml.dom.minidom as minidom
import os
import lxml.html
from lxml import etree
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from collections import defaultdict
from .models import courses_per_semester_f, hours_per_semester_f, courses_f


# finds and displays the index.html template
def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Gets teh objects from models.py and loads them into a template
def persemester(request):
    hours_per_semester = hours_per_semester_f.objects.all()
    courses = courses_f.objects.all()
    courseload = courses_f.workloadhours
    for s in courses_f.objects.all():
        print(s.workloadhours)
    template = loader.get_template('polls/persemester.html')
    context = {
        'hours_per_semester': hours_per_semester,
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))


# gets the objects from models.py and loads them into a template
# def acmcs(request):
#    latest_output = xml_output.objects.all()
#    template = loader.get_template('polls/acmcs.html')
#    context = {{% endfor %}
#         'latest_output': latest_output,
#    }
#    return HttpResponse(template.render(context, request))

# This goes through the syllabi folder and finds all of the courses and puts them in an array.
def getCourses(request):
    path = 'curriculum/mwsu_curriculum/syllabi/'
    values = []
    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        correction = filename.replace('.xml', '')
        values.append(correction)
        values.sort()
    return render(request, 'polls/courselist.html', {'values': values})


def parseSyllabiXmlHTML(request, xmldocname):
    ## This sets the chosen xml file finds it in the database and sets it to the xslt file.
    courses = courses_f.objects.all()
    xslt_doc = etree.parse("curriculum/mwsu_curriculum/transformations/syllabus-to-html.xsl")
    xslt_transformer = etree.XSLT(xslt_doc)
    for course in courses:
        name = 'curriculum/mwsu_curriculum/syllabi/' + course.subject + course.number + '.xml'
        if name == xmldocname:
            source_doc = etree.parse(xmldocname)
            output_doc = xslt_transformer(source_doc)
            return HttpResponse(output_doc)


def parseSchedule(request, xmldocname):
    ## This sets the chosen xml file and sets it to the xslt file.
    xslt_doc = etree.parse("curriculum/mwsu_curriculum/transformations/schedule-to-html.xsl")
    xslt_transformer = etree.XSLT(xslt_doc)
    source_doc = etree.parse(xmldocname)
    output_doc = xslt_transformer(source_doc)
    return HttpResponse(output_doc)


# Parse and pull all data from the acm-cs.xml file and returns all info within an array.
# this is used because of no xsl for this xml file
def parseStandardsXml(request, standardsXml):
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

    return render(request, 'polls/acmcs.html', {'values': values})
