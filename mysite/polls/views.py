from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic # these are generic view classes we can extend

from .models import Choice, Question, Weather
from .name_form import NameForm 
from .detail_form import DetailForm


# declare class-based views
class IndexView(generic.ListView): # by convention call is NnnnView
    template_name = 'polls/index.html' # if left out, it looks for a default template
    context_object_name = 'latest_question_list' # again, over-ride default context object name
    # declare functions of this view class
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:10]

# class DetailView(generic.DetailView): # details of ONE model member
#     model = Question # the exact question will be derived from pk parameter
#     template_name = 'polls/detail.html' # default would be question_detail.html
def detail(request, question_id=1):
    if request.method == 'POST':
        detail_form = DetailForm(request.POST)
        if detail_form.is_valid():
            pass
            # subject = detail_form.cleaned_data['subject']
            # message = detail_form.cleaned_data['message']
            # sender = detail_form.cleaned_data['sender']
            # cc_myself = detail_form.cleaned_data['cc_myself']
            # return HttpResponse('Thank you for the data {} {} {} {}'.format(subject, message, sender, cc_myself) ) # we should send to another URL
        else:
            return HttpResponse('Errors!!')
    else:
        question = get_object_or_404( Question, pk=question_id )
        detail_form = DetailForm()
        return render(request, 'polls/detail.html', {'detail_form':detail_form}) #,'question': question_id})

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

def weather(request):
    weather_list = Weather.objects.order_by('city') 
    context = {'weather_list': weather_list}
    return render(request, 'polls/weather.html', context)

def weather_form(request, weather_id):
    # is it GET or POST?
    if request.method =='POST':
        # the form has been submitted, so save the changes and then show the 'weather' view
        selected_weather = get_object_or_404(Weather, pk=request.POST['id'])
        selected_weather.country = request.POST['country']
        selected_weather.city = request.POST['city']
        selected_weather.description = request.POST['description']
        selected_weather.temperature = request.POST['temperature']
        selected_weather.wind_speed = request.POST['wind_speed']
        selected_weather.wind_direction = request.POST['wind_direction']
        selected_weather.save()
        weather_list = Weather.objects.order_by('city') 
        context = {'weather_list': weather_list}
        return render(request, 'polls/weather.html', context)
    else:
        # for form has NOT yet been submitted - just show the weather_form view
        weather = get_object_or_404(Weather, pk=weather_id)
        context = {'weather':weather}
        return render(request, 'polls/weather_form.html', context)

# here is a view which handles getting the user name from a form called NameForm
def get_name(request):
    if request.method == 'POST': # POST means the form has been submitted
        # we can handle the sumbitted values in the form
        name_form = NameForm(request.POST)
        if name_form.is_valid():
            # process the data
            # DANGER -the data may contain user attacks
            # so we must beware
            subject = name_form.cleaned_data['subject'] # cleaned means validated!
            message = name_form.cleaned_data['message']
            sender = name_form.cleaned_data['sender']
            cc_myself = name_form.cleaned_data['cc_myself']
            return HttpResponse('Thank you for the data {} {} {} {}'.format(subject, message, sender, cc_myself) ) # we should send to another URL
        else:
            return HttpResponse('Errors!!')
    else: # this is for GET - form has not been submitted
        # just render the form
        name_form = NameForm()
        return render(request, 'polls/name_form.html', {'name_form':name_form})