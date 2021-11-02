import bottle

from via import logger

from via.models.collisions.utils import get_collisions

COLLISIONS = get_collisions()


@bottle.route('/collisions/get_geojson')
def get_geojson():
    logger.info('Getting collision GeoJSON')

    filters = {
        'county': getattr(bottle.request.query, 'county', None),
        'year': getattr(bottle.request.query, 'year', None),
        'vehicle_type': getattr(bottle.request.query, 'vehicle_type', None)
    }

    try:
        filters['year'] = int(filters['year'])
    except:
        pass

    # if None we don't want to get where the value is None, rather
    # we don't care so remove it from the filter
    filters = {k: v for k, v in filters.items() if v is not None and v != 'all'}

    dublin_collisions = COLLISIONS.filter(**filters)
    return dublin_collisions.geojson
