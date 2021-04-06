from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'

    def ready(self):
        """
        Connect signals.
        https://docs.djangoproject.com/en/3.2/ref/signals/
        https://docs.djangoproject.com/en/3.2/topics/signals/
        :return:
        """
        import projects.signals
