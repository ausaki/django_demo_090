from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^django_test_project_v0_90/', include('django_test_project_v0_90.apps.foo.urls.foo')),

    (r'^admin/', include('django.contrib.admin.urls.admin')),
    (r'^polls/', include('django_090.apps.polls.urls'))
)
