from django.contrib import admin
from .models import (
    Site,
    Olympiade,
    Typologie,
    Denomination,
    DateReference,
)

admin.site.register(Site)
admin.site.register(Olympiade)
admin.site.register(Typologie)
admin.site.register(Denomination)
admin.site.register(DateReference)
