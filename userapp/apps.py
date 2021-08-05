from django.apps import AppConfig


class UserappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userapp'

    # this is to use signals with userapp
    def ready(self):
        import userapp.signals
