# we added this page to the polls app
# here we explain the routing for our polls app

from django.urls import path

# we need our views
from . import views # from the current folder (dot)

# we can name our app to make code more generic/reusable
app_name = 'polls' # this is a name-space

urlpatterns = [ # a list of url routes
    # eg '/polls/
    path('', views.index, name='index'), # this is the default path ''
    # eg '/polls/4/ or /polls/99/ etc.
    path('<int:question_id>/', views.detail, name='detail'),
    # eg /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # you could put common mispellings and alternate names as url routes
    # eg /polls/75/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]