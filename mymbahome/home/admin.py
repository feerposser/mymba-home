from django.contrib import admin
from .models import ModelTestimony, ModelContact, ModelFAQ, ModelNewsletterAssign


class AdminContact(admin.ModelAdmin):
    readonly_fields = ("name", "email", "office", "created", "updated",)


class AdminNewsletterAssign(admin.ModelAdmin):
    readonly_fields = ("created", "updated",)


admin.site.register(ModelTestimony)
admin.site.register(ModelContact, AdminContact)
admin.site.register(ModelFAQ)
admin.site.register(ModelNewsletterAssign, AdminNewsletterAssign)
