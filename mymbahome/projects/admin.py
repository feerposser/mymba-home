from django.contrib import admin

from .models import ModelActivity, ModelContributor, ModelImageActivity


class AdminImageActivity(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Utilizado para esconder o model na página administrativa
        :param request:
        :return:
        """
        return {}


admin.site.register(ModelActivity)
admin.site.register(ModelContributor)
admin.site.register(ModelImageActivity, AdminImageActivity)
