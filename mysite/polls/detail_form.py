from django import forms # Django form widgets are now available
from django.shortcuts import get_object_or_404
from .models import Question

class DetailForm(forms.Form):
    question = get_object_or_404( Question, pk=3 ) #question_id )
    # [choice for choice in question.choice_set.all]
    # CHOICES =  [('1', 'First'), ('2', 'Second')]
    CHOICES = []
    for choice in question.choice_set.all():
        CHOICES.append( (choice.id, choice.choice_text) )
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label='Vote')
    #     <input type='radio' name='choice' id='choice{{forloop.counter}}'
    #             value='{{choice.id}}' />
    #     <label for='choice{{forloop.counter}}'> {{choice.choice_text}}  </label>
    #     <br/>