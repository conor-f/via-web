import argparse
import threading

import bottle

from ..api import *
from ..settings import PRELOAD_CACHE

from via import logger
from via.pull_journeys import pull_journeys
from via.utils import setup_cache

from via.geojson.generate import generate_geojson


def update_journeys():
    logger.info('Pulling journeys')
    pull_journeys()
    threading.Timer(60 * 60, update_journeys).start()


@bottle.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    bottle.response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    bottle.response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--port',
        dest='port',
        default=8081
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        dest='debug'
    )
    parser.add_argument(
        '--reloader',
        action='store_true',
        dest='reloader'
    )
    args = parser.parse_args()

    if PRELOAD_CACHE:
        setup_cache()

    update_journeys()
    generate_geojson(
        'bike',
        version=None
    )

    bottle.debug(args.debug)

    run_config = {
        'host': '0.0.0.0',
        'port': args.port,
        'debug': args.debug,
        'reloader': args.reloader,
        # 'server': 'gunicorn'
    }

    bottle.run(
        **run_config
    )


if __name__ == '__main__':
    main()
