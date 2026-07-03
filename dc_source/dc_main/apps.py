from django.apps import AppConfig


class DcMainConfig(AppConfig):
    name = 'dc_main'

    def ready(self):
        import dc_main.signals
