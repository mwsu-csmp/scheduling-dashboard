from django.db import models
from django.urls import reverse
from lxml import etree
from curriculum.mwsu_curriculum.curriculumlib import hours_per_semester, courses_per_semester, load_courses
import os


class hours_per_semester_f(models.Model):
    hours_per_semester_text = hours_per_semester()

    def __str__(self):
        return str(self.hours_per_semester_text)


class courses_per_semester_f(models.Model):
    courses_per_semester_text = courses_per_semester()

    def __str__(self):
        return str(self.courses_per_semester_text)


class courses_f(models.Model):
    subject = models.CharField(max_length=3, default="")
    number = models.CharField(max_length=3, default="")
    title = models.CharField(max_length=120, default="")
    offered = models.CharField(max_length=120, default="")
    scheduleType = models.CharField(max_length=120, default="")
    workloadhours = models.IntegerField(default=0)
    catalogDescription = models.CharField(max_length=5000, default="")
    prerequisites = models.CharField(max_length=120, default="")
    objective = models.CharField(max_length=120, default="")
    topic = models.CharField(max_length=120, default="")

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.subject, self.number, self.title,
                                               self.offered, self.scheduleType,
                                               self.catalogDescription, self.prerequisites,
                                               self.objective, self.topic)

    def __int__(self):
        return self.workloadhours


class xml_output(models.Model):
    output_text = models.TextField(max_length=1000000)

    def __str__(self):
        return self.output_text


class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name


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
