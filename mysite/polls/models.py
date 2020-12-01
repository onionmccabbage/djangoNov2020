import datetime # any date or time calcs - use this
from django.utils import timezone
from django.db import models

# Create your models here.
# All models MUST be classes, inheriting from models.Model

class Question(models.Model):
    question_text = models.CharField(max_length=260)
    pub_date      = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=260)
    votes       = models.IntegerField(default=0)
    def __str__(self): # override built in __str__ for nice printing
        return self.choice_text

class Weather(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    temperature = models.FloatField(default=22)
    wind_speed = models.FloatField(default=0)
    wind_direction = models.IntegerField(default=0)
    def __str__(self):
        report_str = "{}: {} {} {} {}".format(self.city, self.description, self.temperature, self.wind_speed, self.wind_direction)
        return report_str