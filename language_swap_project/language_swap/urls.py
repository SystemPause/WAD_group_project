from django.conf.urls import url
from language_swap import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]