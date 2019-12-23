from django.contrib import admin

from .models import KnowledgeArea, Importance, Topic, Outcome, SubKnowledgeArea

""" This file will not be needed. It was decided that admin rights will be determined elsewhere """
""" But for right now Django needs an admin.py  """

class CurriculumAdmin(admin.ModelAdmin):
    """ This is not needed """
    fields = ['pub_date', 'question_text']

admin.site.register(KnowledgeArea)
admin.site.register(Importance)
admin.site.register(Topic)
admin.site.register(Outcome)
admin.site.register(SubKnowledgeArea)
