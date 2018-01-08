from django.shortcuts import render, redirect, render_to_response
from ceg.forms import RegistrationForm, ProjectForm
from django.contrib.auth.models import User
from ceg.models import Project
from ceg import models

from django.views.generic import UpdateView, ListView
from django.http import HttpResponse
from django.template.loader import render_to_string

# Each one is tied to an html file for it render. Below is the most simplistic
# some have the models.X.objects.all() which includes all attributes tied to
# that model

# Each view that is defined below is tied to a url pattern in urls.py
def base(request):
    return render_to_response('ceg/base.html', {'obj': models.Project.objects.all()})

def home(request):
    return render(request, 'ceg/home.html')

def projects(request):
    return render_to_response('ceg/projects.html', {'obj': models.Project.objects.all()})

# Allowing reg_form to render
def register(request):
    if request.method == 'POST':
        # checks to see if you need to register
        # regForm is a built in form particularily used for registration
        regForm = RegistrationForm(request.POST)
        # if it passes it returns the user to the main page
        if regForm.is_valid():
            regForm.save()
            return redirect('/ceg') # main page
        else:
            # Otherwise it loads reg_form, which is a html files
            return render(request, 'ceg/reg_form.html', {'regForm': regForm})
    else:
        regForm = RegistrationForm()
        return render(request, 'ceg/reg_form.html', {'regForm': regForm})

# data_flow accepts two arguments: the normal request object and the name
# whose value is mapped by data_flow defined in r'^post/(?P<post_id>\d+)/detail.html$'
def data_flow(request, project_name):
    try:
        project = models.Project.objects.get(name=project_name)
    except models.Project.DoesNotExist:
        raise Http404
    return render(request, 'ceg/data_flow.html', {'project':project})

# Allowing data.html to render
# In place for all the data to be held/shown
def data(request):
    return render(request, 'ceg/data.html')

# Is the form to add projects
def projectForm(request):
    return render(request, 'ceg/points_list_form.html')


def addProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ceg')
        else:
            return render(request, 'ceg/reg_form.html', {'form': form})
    else:
        form = ProjectForm()
        return render(request, 'ceg/reg_form.html', {'form': form})
