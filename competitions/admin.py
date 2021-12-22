from django.contrib import admin
from .models import CompTeam, Competition, PreviousPerformance
# Register your models here.
admin.site.register(Competition)
admin.site.register(CompTeam)
admin.site.register(PreviousPerformance)
