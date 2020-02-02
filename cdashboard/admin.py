from django.contrib import admin

""" This file will not be needed. It was decided that admin rights will be determined elsewhere """
""" But for right now Django needs an admin.py  """

class CurriculumAdmin(admin.ModelAdmin):
    """ This is not needed """
    fields = ['pub_date', 'question_text']
