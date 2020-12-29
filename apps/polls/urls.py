from django.conf.urls.defaults import *
from .views import index

urlpatterns = patterns('',
    (r'^$', 'django_090.apps.polls.views.index'),
)
