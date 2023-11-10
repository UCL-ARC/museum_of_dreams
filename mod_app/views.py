from django.views.generic import ListView, TemplateView, DetailView
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
            first_three_films = list(actor.films.all()[:3])
            actor.known_for = ", ".join(str(film) for film in first_three_films)
        return context
    
class ActorDetailView(DetailView):
    model = Actor
    template_name = "actor_detail.html"
    context_object_name = "actor"


class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for film in context["object_list"]:
            # themes = list(film.themes.all())
            # film.themes = themes
            starring = list(film.actors.all()[:2])
            film.starring = ", ".join(str(actor) for actor in starring)
            print(starring, "film.actors", film.actors.all())
        return context
    
class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"
    context_object_name = "film"