from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question, Choice

# Create your tests here.
# test the Question class
class QuestionModelTests(TestCase):
    ''' we should write a docstring '''
    def test_was_published_recently(self):
        # generate a future date
        time = timezone.now() + datetime.timedelta(days=12)
        future_question = Question(pub_date=time)
        # assert
        self.assertIs(future_question.was_published_recently(), False)
    def test_pub_with_old_question(self):
        ''' '''
        time = timezone.now() - datetime.timedelta(days=1, seconds=88)
        old_q = Question(pub_date=time)
        # assert
        self.assertIs(old_q.was_published_recently(), False)
    
    def test_pub_with_today_question(self):
        ''' '''
        time = timezone.now() - datetime.timedelta(days=0, seconds=88)
        current_q = Question(pub_date=time)
        # assert
        self.assertIs(current_q.was_published_recently(), True) # it was published today!!

    # test the Choice model
    def test_choice(self):
        ''' '''
        current_choice = Choice(choice_text='this is a test choice')
        # assert
        self.assertEqual(current_choice.choice_text, 'this is a test choice')
        self.assertIs(current_choice.votes, 0)

# to run tests
# manage.py test polls
