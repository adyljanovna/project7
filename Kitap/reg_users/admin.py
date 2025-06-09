from django.contrib import admin
from .models import Profile, Selected, Readlater, Reading, History, Purchases

# Register your models here.
admin.site.register(Profile)
admin.site.register(Selected)
admin.site.register(Readlater)
admin.site.register(Reading)
admin.site.register(History)
admin.site.register(Purchases)
