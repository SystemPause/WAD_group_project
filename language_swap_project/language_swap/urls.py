from django.conf.urls import url
from language_swap import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^searchResult/$', views.searchResult, name = "result"),
    url(r'^about/$', views.about, name = "about"),
    url(r'^team/$', views.team, name = "team"),
    url(r'^contactUs/$', views.about, name = "contact"),
]