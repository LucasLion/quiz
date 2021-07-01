from django.contrib import admin
from .models import Question


class FormAdmin(admin.ModelAdmin.form):
    list_display = ('question', 'option1', 'option2', 'option3', 'option4')


admin.site.register(Question)
