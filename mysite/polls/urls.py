# by the way, Django calls this the urlconf module
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [ # this is a list
    path('', views.IndexView.as_view(), name='index'), # IndexView is a class, we cast to a view
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # pk for the primary key
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'), # NB vote has no template
    path('/child/', views.ChildView.as_view(), name='child'),
]