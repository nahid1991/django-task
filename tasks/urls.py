from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^v1/contact/$', views.ContactList.as_view()),
    url(r'^v1/contact/(?P<pk>[0-9]+)/$', views.ContactList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)