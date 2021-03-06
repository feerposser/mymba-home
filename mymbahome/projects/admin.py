from django.contrib import admin

from .models import ModelActivity, ModelContributor, ModelImageActivity, ModelTypeActivity


class AdminImageActivity(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Utilizado para esconder o model na página administrativa
        :param request:
        :return:
        """
        return {}


class AdminTypeActivity(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class AdminActivity(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ("name",)}


admin.site.register(ModelActivity, AdminActivity)
admin.site.register(ModelContributor)
admin.site.register(ModelImageActivity, AdminImageActivity)
admin.site.register(ModelTypeActivity, AdminTypeActivity)
