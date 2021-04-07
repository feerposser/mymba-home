from django.contrib import admin
from .models import ModelTestimony, ModelContact, ModelFAQ


class AdminContact(admin.ModelAdmin):
    readonly_fields = ("name", "email", "subject", "message", "created", "updated",)


admin.site.register(ModelTestimony)
admin.site.register(ModelContact, AdminContact)
admin.site.register(ModelFAQ)
