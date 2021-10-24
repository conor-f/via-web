import datetime
import urllib
from packaging.version import Version


def parse_start_date(earliest_date):
    if earliest_date is None:
        return '2021-01'

    if earliest_date < datetime.datetime(2021, 1, 1):
        return '2021-01'

    return earliest_date


def parse_end_date(latest_date):
    if latest_date is None:
        return '2023-12'

    if latest_date > datetime.datetime(2023, 12, 31):
        return '2023-12'

    return latest_date


def generate_basename(
    name=None,
    version=None,
    version_op=None,
    earliest_time=None,
    latest_time=None,
    place=None
):
    data = {
        'transport_type': name,
        'version': version,
        'version_op': version_op,
        'earliest_time': parse_start_date(earliest_time),
        'latest_time': parse_end_date(latest_time),
        'place': place
    }
    if data['version'] in {None, False, '0.0.0', Version('0.0.0')}:
        del data['version']
        del data['version_op']
    if data['place'] is None:
        del data['place']
    return urllib.parse.urlencode(data)
