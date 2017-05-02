from __future__ import unicode_literals

from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class V1PrototypeConfig(ModuleMixin, AppConfig):
    name = 'V1prototype'
    icon = '<i class="material-icons">flight_takeoff</i>'
