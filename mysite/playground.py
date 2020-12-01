# this is not normal production - just for demo purposes
# this module would be invoked in the django shell
# e.g. python manage.py shell
# >>> import playground

from django.utils import timezone

from polls.models import Choice, Question 

# see all the Question models
print( Question.objects.all() ) # objects (plural)

# create question instance                              timezone.now()
q = Question(question_text='Is it lunch yet?', pub_date=timezone.now() )
q.save() # commit to the db

print(q.id, q, q.pub_date)

# we can mutate properties directly
q.question_text = 'not yet lunch is it?'
print(q.id, q, q.pub_date) # was q.question_text

# see all the Question models
print( Question.objects.all() ) # objects (plural)
