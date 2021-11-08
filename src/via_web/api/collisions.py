import bottle

from via import logger
from via.collisions.utils import generate_geojson as generate_collision_geojson
from via.collisions.utils import retrieve_geojson as retrieve_collision_geojson


@bottle.route('/collisions/get_geojson')
def get_geojson():
    logger.info('Getting collision GeoJSON')

    # FIXME: since this is so slow we can't do all of ireland
    # use caches / premade geojson files

    try:
        data = retrieve_collision_geojson(transport_type='bicycle', county='dublin')
    except FileNotFoundError:
        generate_collision_geojson(transport_type='bicycle', county='dublin')
        data = retrieve_collision_geojson(transport_type='bicycle', county='dublin')

    return data
