from django.conf.urls import url
from language_swap import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^searchResult/$', views.searchResult, name = "result"),
    url(r'^about/$', views.about, name = "about"),
    url(r'^contactUs/$', views.contact, name = "contact"),
    url(r'^myProfile/$', views.profile, name = "myProfile"),
    url(r'^myProfile/edit/$', views.edit_profile, name = 'edit_profile'),
    url(r'^myProfile/delete/$', views.delete_account, name = 'delete_account'),
    url(r'^contactHistory/$', views.contactHistory, name = "contactHistory"),
    url(r'^rating/$', views.rating, name = "rating"),
    url(r'^emailCheck/$',views.emailCheck,name = "emailCheck"),
    url(r'^sendEmail/$', views.sendEmail, name = 'sendEmail'),
]
