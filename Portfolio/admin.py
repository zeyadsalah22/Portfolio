from django.contrib import admin

from .models import Certificate,Project,Skill,Texter

admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(Skill)
admin.site.register(Texter)

