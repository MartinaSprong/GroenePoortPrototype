from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static


urlpatterns = (
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^graph/$', views.graphView, name='graph'),
)

