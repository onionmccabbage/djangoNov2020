from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse # reverse url lookup can read a route

# import the models we need
from .models import Question, Choice

# Create your views here.
def index(request): # a functional view, receiving the entire request that the user made
    # get hold of all the existing questions        reverse order
    latest_question_list = Question.objects.order_by('-pub_date')[:10] # first ten (via SQL limit)
    # output = ', '.join([q.question_text for q in latest_question_list]) # this is a comprehension
    # use a template to iterate over them
    # template = loader.get_template('polls/index.html') # we don't need to explicitly mention the template
    context = {'latest_question_list':latest_question_list}
    # we can return something for the user to see
    return render(request, 'polls/index.html', context)

def detail(request, question_id=1):
    # try:
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404( Question, pk=question_id ) # shortcut
    # except Question.DoesNotExist :
    #     raise Http404('Question does not exist') # debug info not for end user
    # # response = 'This is question number %s'
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id=1):
    # response = 'Results for question number %s' # will include poll votes later
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

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