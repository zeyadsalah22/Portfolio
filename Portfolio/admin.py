from django.contrib import admin

from .models import Certificate,Project,Texter

admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(Texter)

