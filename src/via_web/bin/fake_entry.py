import threading
import time


from via import logger
from via.pull_journeys import pull_journeys
from via.utils import setup_cache

from via.geojson.generate import generate_geojson


def update_journeys():
    logger.info('Pulling journeys')
    pull_journeys()
    threading.Timer(60 * 60, update_journeys).start()


setup_cache()

print('FINISHED SETUP')

update_journeys()

print('FINISHED UPDATE')

generate_geojson(
    None,
    version=None
)

time.sleep(300)
