import os
import time
import stat

import fast_json

from via.constants import GEOJSON_DIR
from via.geojson.utils import generate_basename


def get_geojson(
    journey_type,
    earliest_time=None,
    latest_time=None,
    place=None,
    version=None,
    version_op=None,
    max_age=60*60*12
):
    if journey_type is None:
        journey_type = 'all'

    basename = generate_basename(
        name=journey_type,
        version=version,
        version_op=version_op,
        earliest_time=earliest_time,
        latest_time=latest_time,
        place=place
    )
    geojson_file = os.path.join(
        GEOJSON_DIR,
        f'{basename}.geojson'
    )

    if not os.path.exists(geojson_file):
        raise FileNotFoundError()

    if time.time() - os.stat(geojson_file)[stat.ST_MTIME] > max_age:
        raise FileNotFoundError()

    geojson_data = []
    with open(geojson_file) as fh:
        geojson_data = fast_json.load(fh)

    return geojson_data
