from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic # these are generic view classes we can extend

from .models import Choice, Question

# declare class-based views
class IndexView(generic.ListView): # by convention call is NnnnView
    template_name = 'polls/index.html' # if left out, it looks for a default template
    context_object_name = 'latest_question_list' # again, over-ride default context object name
    # declare functions of this view class
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:10]

class DetailView(generic.DetailView): # details of ONE model member
    model = Question # the exact question will be derived from pk parameter
    template_name = 'polls/detail.html' # default would be question_detail.html

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# vote has no template, so cannot use a generic view
def vote(request, question_id=1):


    # get hold of the relevant question for this vote
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError :
        # just show the form again
        return render(request, 'polls/detail.html', {'question':question, 'error_message':'Invalid choice'})
    else: # only runs if there was no exception
        selected_choice.votes += 1
        selected_choice.save() # commits the changes to the database
        # NB reverse expect an iterable, so put a comma to make this a tuple 
        return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) )

class ChildView(generic.ListView):
    model = Question
    template_name = 'polls/child.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:10]
