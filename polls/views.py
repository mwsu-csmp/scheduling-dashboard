import xml.dom.minidom as minidom
import os
import lxml.html
from lxml import etree
from collections import defaultdict
from xml.dom.minidom import Node
from django.shortcuts import render
from django.shortcuts import render_to_response
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
    ## This sets the chosen xml file and sets it to the xslt file.
    xslt_doc = etree.parse("curriculum/syllabi/syllabus-to-html.xsl")
    xslt_transformer = etree.XSLT(xslt_doc)
 
    source_doc = etree.parse(xmldocname)
    output_doc = xslt_transformer(source_doc)
    #print(str(output_doc))
    return HttpResponse(output_doc)


    #return render(request, 'polls/syllabus-to-html.xsl',xmldoc)

def parseSchedule(request, xmldocname):
    ## This sets the chosen xml file and sets it to the xslt file.
    xslt_doc = etree.parse("curriculum/schedules/schedule-to-html.xsl")
    xslt_transformer = etree.XSLT(xslt_doc)
    source_doc = etree.parse(xmldocname)
    output_doc = xslt_transformer(source_doc)
    return HttpResponse(output_doc)

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

