from . import views
from django.conf.urls import url

app_name = 'about'
urlpatterns = [
    url(r'^$', views.about, name='about'),

]