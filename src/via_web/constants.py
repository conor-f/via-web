import os

METRES_PER_DEGREE = 110574.38855780

BASE_PATH = '/opt/via/' if os.getenv('TEST_ENV', 'False') == 'False' else '/tmp/via'

DATA_DIR = os.path.join(BASE_PATH, 'data')
GENERATED_DIR = os.path.join(BASE_PATH, 'generated')
CACHE_DIR = os.path.join(BASE_PATH, 'cache')

REMOTE_DATA_DIR = os.path.join(DATA_DIR, 'raw')

EDGE_CACHE_DIR = os.path.join(CACHE_DIR, 'edge_cache')
EDGE_DATA_CACHE_DIR = os.path.join(CACHE_DIR, 'edge_data_cache')
NETWORK_CACHE_DIR = os.path.join(CACHE_DIR, 'network_cache')

GEOJSON_DIR = os.path.join(GENERATED_DIR, 'geojson')

LOG_LOCATION = '/var/log/via/via.log' if os.getenv('TEST_ENV', 'False') == 'False' else '/tmp/log/via/via.log'

DEFAULT_EDGE_COLOUR = '#E1E1E1'

POLY_POINT_BUFFER = 0.002
