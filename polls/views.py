import xml.dom.minidom as minidom
import os
from os import walk
from collections import defaultdict
from xml.dom.minidom import Node
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import say_something, xml_output, hours_per_semester_f

def index(request):
    latest_say_something = say_something.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_say_something': latest_say_something,
    }
    return HttpResponse(template.render(context, request))

def persemester(request):
    hours_per_semester = hours_per_semester_f.objects.all()
    template = loader.get_template('polls/persemester.html')
    context = {
        'hours_per_semester': hours_per_semester,
    }
    return HttpResponse(template.render(context, request))

def acmcs(request):
    latest_output = xml_output.objects.all()
    template = loader.get_template('polls/acmcs.html')
    context = {
         'latest_output': latest_output,
    }
    return HttpResponse(template.render(context, request))

def courselist(request):
    template = loader.get_template('polls/courselist.html')
    context = {}
    return HttpResponse(template.render(context, request))

def parseSyllabiXml(request, xmldocname):
    xmldoc = minidom.parse(xmldocname)
    college = xmldoc.getElementsByTagName('college')
    subject = xmldoc.getElementsByTagName('subject')
    number = xmldoc.getElementsByTagName('number')
    title = xmldoc.getElementsByTagName('title')
    offered = xmldoc.getElementsByTagName('offered')
    scheduleType = xmldoc.getElementsByTagName('scheduleType')
    catalogDescription = xmldoc.getElementsByTagName('catalogDescription')
    prerequisites = xmldoc.getElementsByTagName('prerequisites')
    objectives = xmldoc.getElementsByTagName('objectives')
    outline = xmldoc.getElementsByTagName('outline')
    values = []
    for s in college :
        textvalue = s.firstChild.data
        values.append('College: ' + textvalue)

    for s in subject :
        textvalue = s.firstChild.data
        values.append('Subject: ' + textvalue)
        break

    for s in number :
        textvalue = s.firstChild.data
        values.append('Number: ' + textvalue)
        break

    for s in title :
        textvalue = s.firstChild.data
        values.append('Title: ' + textvalue)

    for s in offered :
        textvalue = s.firstChild.data
        values.append('Offered: ' + textvalue)

    for s in scheduleType :
        textvalue = s.firstChild.data
        values.append('Schedule Type: ' + textvalue)

    for s in catalogDescription :
        textvalue = s.firstChild.data
        values.append('Catalog Description: ' + textvalue)

    for s in prerequisites :
        values.append('Prerequisites: ')
        prerequisiteCourse = s.getElementsByTagName('prerequisiteCourse')
        for p in prerequisiteCourse:
            prereqvalue = p.getAttribute('minimumGrade')
            prereqsub = p.getElementsByTagName('subject')
            prereqnum = p.getElementsByTagName('number')
            for s in prereqsub:
                textvalue = s.firstChild.data
                for n in prereqnum:
                    numvalue = n.firstChild.data
                    values.append('Course: '+ textvalue + ' ' + numvalue + ' Minimum Grade: ' + prereqvalue)  

    for s in objectives :
        objective = s.getElementsByTagName('objective')
        values.append('Objectives: ')
        for o in objective :
            childElem = o.firstChild.data 
            values.append("Objective: " + childElem)

    for s in outline :
        topics = s.getElementsByTagName('topic')
        values.append('Outline: ')
        for t in topics :
            childElem = t.firstChild.data
            values.append('Topic: ' + childElem)
    fixedName = xmldocname.replace('.xml',"")
    xmlfile = fixedName.replace('curriculum/syllabi/',"")
    print('youre in parse')
    return render(request, 'polls/'+xmlfile+'.html',{'values': values})


def parseStandardsXml(request, standardsXml):
    xmldoc = minidom.parse(standardsXml)
    name = xmldoc.getElementsByTagName('name')
    body = xmldoc.getElementsByTagName('body')
    version = xmldoc.getElementsByTagName('version')
    knowledgeArea = xmldoc.getElementsByTagName('knowledgeArea')
    values = []
    for s in name :
        textvalue = s.firstChild.data
        values.append('Name: ' + textvalue)

    for s in body :
        textvalue = s.firstChild.data
        values.append('Body: ' + textvalue)

    for s in version :
        textvalue = s.firstChild.data
        values.append('Version: ' + textvalue)

    for s in knowledgeArea :
        namevalue = s.getAttribute('name')
        if not namevalue == "": continue 
        idvalue = s.getAttribute('id')
        namevalue = s.getAttribute('name')
        values.append('Knowledge Area id: ' + idvalue)
        subKnowledgeArea = s.getElementsByTagName('knowledgeArea')
        for s in subKnowledgeArea :
            idvalue = s.getAttribute('id')
            namevalue = s.getAttribute('name')
            values.append('Knowledge Area ' + 'id: ' + idvalue + ' name: ' + namevalue)
            subTopics = s.getElementsByTagName('topic')
            subOutcomes = s.getElementsByTagName('outcome')
            for s in subTopics :
                textvalue = s.firstChild.data
                impvalue = s.getAttribute('importance')
                values.append(' topic importance: ' + impvalue + ': ' + textvalue)                
            for s in subOutcomes :
                textvalue = s.firstChild.data
                impvalue = s.getAttribute('importance')
                values.append('outcome importance: ' + impvalue + ': ' + textvalue)

    fixedName = standardsXml.replace('.xml',"")
    xmlfile = fixedName.replace('curriculum/standards/',"")
    return render(request, 'polls/acmcs.html',{'values': values})

#def load_syllabi(request):
#  return [parseSyllabiXml(request,open('curriculum/syllabi/'+filename)) for filename in #next(walk('curriculum/syllabi'))[2]]
#
#def hours_per_semester(request):
#  # update to use credit hours instead of # of courses
#  semesters = defaultdict(list)
#  for xmldoc in load_syllabi(request):
#    for semester in offered:
#      semesters[semester].append(course)
#  ret = []
#  for semester in semesters:
#    ret.append((semester, sum(map((lambda course: course.workload_hours), semesters[semester]))))
#    template = loader.get_template('polls/hours_per_semester.html')
#    context = {}
#    return render(request, 'poll/hourspersemester.html',{'ret': ret})

