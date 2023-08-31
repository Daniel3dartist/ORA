from django.apps import AppConfig


class FakeGenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_gen'
