import os
import operator

import fast_json

from via import logger
from via.constants import GEOJSON_DIR
from via.utils import (
    get_journeys,
    should_include_journey
)
from via.models.journeys import Journeys
from via.geojson.utils import generate_basename


def get_generation_config(transport_type=None, version=None, version_op=None, earliest_time=None, latest_time=None, place=None):
    config = []
    if transport_type in {None, 'all'}:
        config = [
            {'transport_type': 'all', 'name': 'all', 'version': version, 'version_op': version_op if version else None, 'earliest_time': earliest_time, 'latest_time': latest_time, 'place': place},
            {'transport_type': 'bike', 'name': 'bike', 'version': version, 'version_op': version_op if version else None, 'earliest_time': earliest_time, 'latest_time': latest_time, 'place': place},
            {'transport_type': 'car', 'name': 'car', 'version': version, 'version_op': version_op if version else None, 'earliest_time': earliest_time, 'latest_time': latest_time, 'place': place},
            {'transport_type': 'bus', 'name': 'bus', 'version': version, 'version_op': version_op if version else None, 'earliest_time': earliest_time, 'latest_time': latest_time, 'place': place}
        ]
    else:
        config = [
            {'transport_type': transport_type, 'name': transport_type, 'version': version, 'version_op': version_op if version else None, 'earliest_time': earliest_time, 'latest_time': latest_time, 'place': place}
        ]

    return config


def generate_geojson(
    transport_type,
    version=False,
    version_op=None,
    earliest_time=None,
    latest_time=None,
    place=None
):

    os.makedirs(
        os.path.join(GEOJSON_DIR),
        exist_ok=True
    )

    for config_item in get_generation_config(
        transport_type=transport_type,
        version=version,
        version_op=version_op,
        earliest_time=earliest_time,
        latest_time=latest_time,
        place=place
    ):
        logger.info(f'Generating geojson for "{config_item["transport_type"]}"')

        journeys = get_journeys(
            transport_type=config_item['transport_type'],
            earliest_time=earliest_time,
            latest_time=latest_time,
        )

        versions = set([journey.version for journey in journeys])

        for version in versions:

            basename = generate_basename(
                name=config_item['name'],
                version=version,
                version_op=config_item['version_op'],
                earliest_time=config_item['earliest_time'],
                latest_time=config_item['latest_time'],
                place=config_item['place']
            )
            geojson_file = os.path.join(
                GEOJSON_DIR,
                f'{basename}.geojson'
            )

            journeys = Journeys(
                data=[
                    journey for journey in journeys if should_include_journey(
                        journey,
                        version_op=getattr(operator, version_op) if version_op is not None else None,
                        version=version
                    )
                ]
            )

            with open(geojson_file, 'w') as json_file:
                fast_json.dump(
                    journeys.geojson,
                    json_file
                )
