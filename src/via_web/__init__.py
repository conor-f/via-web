import requests

import warnings
warnings.filterwarnings('ignore', '.*Geometry is in a geographic CRS.*', )

import osmnx as ox

from via import settings
from via.logging import logger


# overpass api clone for this so we can disable rate limiting and not feel bad

try:
    CUSTOM_AVAILABLE = 'www.openstreetmap.org' in requests.get(settings.CUSTOM_OVERPASS_API, timeout=1).text
except:
    CUSTOM_AVAILABLE = False

if CUSTOM_AVAILABLE:
    overpass_endpoint = settings.CUSTOM_OVERPASS_API
    overpass_rate_limit = False
    logger.info('Using custom overpass api')
else:
    overpass_endpoint = settings.DEFAULT_OVERPASS_API
    overpass_rate_limit = True
    logger.info('Using default overpass api')

ox.config(
    overpass_endpoint=overpass_endpoint,
    overpass_rate_limit=overpass_rate_limit
)
