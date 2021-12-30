from django.contrib import admin
from .models import CompTeam, Competition, Module, SubmitPerformance
# Register your models here.
admin.site.register(Module)
admin.site.register(Competition)
admin.site.register(CompTeam)
admin.site.register(SubmitPerformance)
