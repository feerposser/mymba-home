from django.contrib import admin
from .models import ModelTestimony, ModelContact


class AdminContact(admin.ModelAdmin):
    readonly_fields = ("name", "email", "subject", "message", "created", "updated",)


admin.site.register(ModelTestimony)
admin.site.register(ModelContact, AdminContact)
