import os
from importlib import import_module

config_env = os.getenv('ENV', 'local')

module = import_module(f'app.config.{config_env}')
Config = getattr(module, 'Config', None)
