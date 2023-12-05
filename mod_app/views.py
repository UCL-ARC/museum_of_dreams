from django.views.generic import DetailView, ListView, TemplateView

from .models import Film


class HomeView(TemplateView):
    template_name = "home.html"


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
            # print(starring, "film.actors", film.actors.all())
        return context


class FilmDetailView(DetailView):
    model = Film
    template_name = "film_detail.html"
    context_object_name = "film"
