from django.contrib import admin

from .models import KnowledgeArea, Importance, Topic, Outcome, SubKnowledgeArea

class CurriculumAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(KnowledgeArea)
admin.site.register(Importance)
admin.site.register(Topic)
admin.site.register(Outcome)
admin.site.register(SubKnowledgeArea)
