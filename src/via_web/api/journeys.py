import datetime

import bottle

from via.geojson import (
    generate,
    retrieve
)

from via_web import logger


@bottle.route('/journeys/get_geojson')
def get_geojson():
    logger.info('Getting GeoJSON')

    earliest_time = datetime.datetime.strptime(bottle.request.query.earliest_time, '%Y-%m')
    latest_time = datetime.datetime.strptime(bottle.request.query.latest_time, '%Y-%m')

    data = None

    try:
        data = retrieve.get_geojson(
            'bike',
            earliest_time=earliest_time,
            latest_time=latest_time,
            place=None,  # TODO
            version=None,  # TODO
            version_op=None,  # TODO
        )
    except FileNotFoundError:
        logger.info('geojson not found, generating')
        try:
            generate.generate_geojson(
                'bike',
                earliest_time=earliest_time,
                latest_time=latest_time,
                place=None,  # TODO
                version=None,  # TODO
                version_op=None,  # TODO
            )
        except Exception as ex:
            logger.error(f'Could not generate geojson: {ex}')
        else:
            try:
                data = retrieve.get_geojson(
                    'bike',
                    earliest_time=earliest_time,
                    latest_time=latest_time,
                    place=None,  # TODO
                    version=None,  # TODO
                    version_op=None,  # TODO
                )
            except Exception as ex:
                logger.error(f'Could not retrieve geojson: {ex}')
    except Exception as ex:
        logger.error(f'Could not retrieve geojson: {ex}')

    return data
