from django.contrib import admin
from .models import Event, EventRegistration, Category

# Register your models here.
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(Category)