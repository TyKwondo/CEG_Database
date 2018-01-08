from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

# Each url pattern connects a view to a html page
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'ceg/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'ceg/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^data/$', views.data, name='data'),
    url(r'^projectForm/$', views.projectForm, name='projectForm'),
    url(r'^projects/$', views.projects, name='projects'),

# # Map the view function ceg.views.data_flow() to an URL pattern
# [^/]+	One or more characters until (and not including) a forward slash
    url(r'^projects/(?P<project_name>[^/]+)/data_flow.html$',
        views.data_flow, name='data_flow'),
]
