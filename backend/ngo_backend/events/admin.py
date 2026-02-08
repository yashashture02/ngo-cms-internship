from django.contrib import admin # type: ignore
from .models import Event, Donation

admin.site.register(Event)
admin.site.register(Donation)
