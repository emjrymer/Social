from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView, ListView

from app.models import UserProfile, Suggestion, Alcohol, Follower


class NewUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=25)
    age = forms.IntegerField()
    favorite_alcohol = forms.CharField(max_length=30)


class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreationForm

    def form_valid(self, form):
        user_object = form.save()
        user_name = form.cleaned_data.get("name")
        user_age = form.cleaned_data.get("age")
        user_fav_alcohol = form.cleaned_data.get("favorite_alcohol")
        UserProfile.objects.create(user=user_object, age=user_age, name=user_name, favorite_alcohol=user_fav_alcohol)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("login_view")


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['suggestions'] = Suggestion.objects.all()
        return context


class AlcoholCreateView(CreateView):
    model = Alcohol
    fields = ('alcohol_type',)

    def get_success_url(self):
        return reverse("main_view")


class SuggestionCreateView(CreateView):
    model = Suggestion
    fields = ('body', 'alcohol')

    def form_valid(self, form):
        suggestion_object = form.save(commit=False)
        suggestion_object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("main_view")


class UserDetailView(DetailView):
    model = User


class AddFollower(DetailView):
    model = Follower

    def get_object(self):
        follower_object = super().get_object()
        Follower.objects.create(name=follower_object)
        return follower_object


def redirect(request):
    return HttpResponseRedirect(reverse('main_view'))
