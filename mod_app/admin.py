from django.contrib import admin
from .models import Actor, Film, Location, Tag

class FilmInline(admin.StackedInline):
    model = Film.actors.through
    extra = 1

    def __str__(self):
        return self.film.title
    

class ActorAdmin(admin.ModelAdmin):
    inlines = (FilmInline,)


admin.site.register([ Film, Location, Tag])
admin.site.register(Actor, ActorAdmin)
