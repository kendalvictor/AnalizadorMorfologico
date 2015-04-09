from django.conf.urls import patterns, include, url
from analizador import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r"analizar/$", views.analizar, name='analizar'),
)