from django.conf.urls import url
from hello_world.views import hello_world


urlpatterns = [
    url(r'.*', hello_world),
]
