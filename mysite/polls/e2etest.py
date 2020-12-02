from django.test.utils import setup_test_environment
from django.test import Client

# we set up an environment for our tests. This alteres the behaviour of Django and debugging...
setup_test_environment()
# we need an instance of 'client'
client = Client() # this emulates a browser

# test what happens when we go to URLs
response = client.get('/nonsuch') # does not exist

print(response.status_code) # expect 404
# we can write our own assertions
if response.status_code == 404:
    # as expected
    pass # or log sucess to a text file
else:
    # report the outcome
    pass # write the problem to a text file - or send an email, or notify somehow

# now try some worknig addresses
from django.urls import reverse
response = client.get(reverse('polls:index'))
print(response.status_code) # expect 200
print(response.content) # expect he web apge!!!
print(response.context['latest_question_list']) # expeect the questions list here


