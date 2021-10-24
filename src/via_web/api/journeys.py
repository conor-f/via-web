import datetime

import bottle

from via import logger

from via.geojson import (
    generate,
    retrieve
)


@bottle.route('/journeys/get_geojson')
def get_geojson():
    logger.info('Getting GeoJSON')

    earliest_time = datetime.datetime.strptime(bottle.request.query.earliest_time, '%Y-%m')
    latest_time = datetime.datetime.strptime(bottle.request.query.latest_time, '%Y-%m')
    journey_type = bottle.request.query.journey_type

    try:
        data = retrieve.get_geojson(
            journey_type,
            earliest_time=earliest_time,
            latest_time=latest_time,
            place=None,  # TODO
            version=None,  # TODO
            version_op=None,  # TODO
        )
    except FileNotFoundError:
        generate.generate_geojson(
            journey_type,
            earliest_time=earliest_time,
            latest_time=latest_time,
            place=None,  # TODO
            version=None,  # TODO
            version_op=None,  # TODO
        )

        data = retrieve.get_geojson(
            journey_type,
            earliest_time=earliest_time,
            latest_time=latest_time,
            place=None,  # TODO
            version=None,  # TODO
            version_op=None,  # TODO
        )

    return data
