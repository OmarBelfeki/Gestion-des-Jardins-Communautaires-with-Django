from django.contrib import admin
from .models import Affectation, Parcelle, Jardin, Member

admin.site.register(Affectation)
admin.site.register(Parcelle)
admin.site.register(Jardin)
admin.site.register(Member)
