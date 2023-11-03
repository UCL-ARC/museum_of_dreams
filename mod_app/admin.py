from django.contrib import admin
from .models import Actor, Film, Location

admin.site.register([Actor, Film, Location])
