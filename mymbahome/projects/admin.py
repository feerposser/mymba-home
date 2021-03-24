from django.contrib import admin

from .models import ModelProject as Project, ModelContributor as Contributor, ModelAction as Action


admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Action)
