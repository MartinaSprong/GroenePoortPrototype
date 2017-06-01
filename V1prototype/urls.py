from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static


urlpatterns = (
    url(r'^$', views.index, name='index'),
    # url(r'^tide/(?P<oid>[0-9]+)/$', views.graphView, name='graph'),
    url(r'^tide/(?P<oid>\d+\.\d{4})/$', views.graphView, name='graph'), 
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^tide/$', views.jsonGetTide, name='jsonGetTide'),
    url(r'^chlorosity/$', views.jsonGetChlorosity, name='jsonGetChlorosity'),
)
