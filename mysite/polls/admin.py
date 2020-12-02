from django.contrib import admin
from .models import Question, Choice, Weather

# we can combine models
class ChoiceInLine(admin.StackedInline): # combine models
    model = Choice
    # let's allow additional choices
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),('Date', {'fields':['pub_date']})]
    inlines = [ChoiceInLine]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Weather)
