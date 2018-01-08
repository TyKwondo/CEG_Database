from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from ceg.models import Project #UserProfile

# Form for new users to register on our website
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # meta is all the different attributes to the model that is then attached
    # to the form.
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
# Saves the data and uploads data to tables
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

# This was made to link a project to user so there could be a list of
# users on a specific project.
'''class UserProfileForm(UserCreationForm):

    project = forms.ChoiceField(choices=ProjectName, required=True)
    phone = forms.CharField(max_length=25, required=True)

    class Meta:
        model = UserProfile
        fields = (
            'project',
            'phone',
        )
    def save(self, commit=True):
        userProfile = super(UserProfileForm, self).save(commit=False)
        userProfile.project = self.cleaned_data['project']
        userProfile.phone = self.cleaned_data['phone']

        if commit:
            userProfile.save()
        return userProfile'''

# Form for points list names
class ProjectForm(UserCreationForm):
    name = forms.CharField(required=True)
    pub_time = forms.DateTimeField(required=True)

    class Meta:
        model = Project
        fields = (
            'name',
            'pub_time',
        )
    def save(self, commit=True):
        project = super(ProjectForm, self).save(commit=False)
        project.name = self.cleaned_data['name']
        project.pub_date = self.cleaned_data['pub_date']

        if commit:
            project.save()

        return project
