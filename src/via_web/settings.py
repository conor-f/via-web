import os

PRELOAD_CACHE = os.getenv('PRELOAD_CACHE', 'false').lower() == 'true'
