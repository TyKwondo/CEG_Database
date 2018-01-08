from django.apps import AppConfig

# makes ceg an app on the Django app list
# Which is needed in order to work on your django project
class CegConfig(AppConfig):
    name = 'ceg'
