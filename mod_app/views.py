from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Actor, Film


class HomeView(TemplateView):
    template_name = "home.html"


class ActorListView(ListView):
    model = Actor
    template_name = "actor_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for actor in context["object_list"]:
            first_three_films = actor.films.all()[:3]
            actor.known_for = first_three_films
        return context


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    paginate_by = 20
