from django.db import models
from mwsu_curriculum.curriculumlib import *

"""Python uses a MVC (Models - Views - Controller) system. Django adopts this and makes a small change. 
Instead django uses a MVT (Model - Views - Template) system. Models sets up the information """

class hours_per_semester_f(models.Model):
    """ creates a model for hours-per-semester """
    hours_per_semester_text = hours_per_semester()

    def __str__(self):
        return str(self.hours_per_semester_text)


class courses_per_semester_f(models.Model):
    """ creates a model for courses-per-semester """
    courses_per_semester_text = courses_per_semester()

    def __str__(self):
        return str(self.courses_per_semester_text)


class courses_f(object):
    """ creates a model for each individual course. This is the class that holds each courses information """
    def __init__(self, course, title, offered, scheduleType, workloadhours,
                 catalogDescription, prerequisites, objective, topic):
        self.course = course
        self.title = title
        self.offered = offered
        self.scheduleType = scheduleType
        self.workloadhours = workloadhours
        self.catalogDescription = catalogDescription
        self.prerequisites = prerequisites
        self.objective = objective
        self.topic = topic


class schedule_f(object):
    """ creates a model for each individual schedule. This is the class that holds each schedules information """
    def __init__(self, course, section_number, start_time, end_time, day,
                 building_room, max, instructor):
        self.course = course
        self.section_number = section_number
        self.start_time = start_time
        self.end_time = end_time
        self.day = day
        self.building_room = building_room
        self.max = max
        self.instructor = instructor

class assignments(object):
    """ creates a model for each individual assignment. This is the class that holds each assignment information """
    def __init__(self, instructor, workloadhours):
        self.instructor = instructor
        self.workloadhours = workloadhours

class KnowledgeArea(models.Model):
    """Model representing the Knowledge Area."""
    name = models.CharField(max_length=10, help_text='Enter a Knowledge Area (e.g. AL)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Importance(models.Model):
    """Model representing the Knowledge Area."""
    name = models.CharField(max_length=10, help_text='Enter a importance level (e.g. tier1)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Topic(models.Model):
    """Model representing the Topic."""
    name = models.CharField(max_length=200, help_text='Enter a Topic')

    importance = models.ManyToManyField(Importance, help_text='Select a importance level')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Outcome(models.Model):
    """Model representing the Outcome."""
    name = models.CharField(max_length=200, help_text='Enter an Outcome')

    importance = models.ManyToManyField(Importance, help_text='Select a importance level')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class SubKnowledgeArea(models.Model):
    """Model representing a Sub Knowledge Area."""
    name = models.CharField(max_length=6, help_text='Enter a Sub Knowledge Area')

    summary = models.TextField(max_length=1000, help_text='Name of Class')

    topic = models.ManyToManyField(Topic, help_text='Enter a Topic')

    outcome = models.ManyToManyField(Outcome, help_text='Enter an Outcome')

    def __str__(self):
        """String for representing the Model object."""
        return self.title
