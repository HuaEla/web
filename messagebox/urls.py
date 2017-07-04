from django.conf.urls import url

from . import views

app_name = 'message'
urlpatterns = [
    url(r'^$', views.messageview, name='message'),
]