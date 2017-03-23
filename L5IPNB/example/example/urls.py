from django.conf.urls import url

from main.views import view_example


urlpatterns = [
    url(r'', view_example, name='example'),
]
