import os

PRELOAD_CACHE = os.getenv('PRELOAD_CACHE', 'false').lower() == 'true'

VIZ_INITIAL_LAT = float(os.getenv('VIZ_INITIAL_LAT', 53.35))
VIZ_INITIAL_LNG = float(os.getenv('VIZ_INITIAL_LNG', -6.26))
VIZ_INITIAL_ZOOM = int(os.getenv('VIZ_INITIAL_ZOOM', 12))
