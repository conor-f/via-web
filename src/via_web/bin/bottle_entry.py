import argparse
import threading

import bottle
from bottle import response

from ..api import *

from via import logger
from via.pull_journeys import pull_journeys

from via.geojson.generate import generate_geojson


def update_journeys():
    logger.info('Pulling journeys')
    pull_journeys()
    threading.Timer(60 * 60, update_journeys).start()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--port',
        dest='port',
        default=8080
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

    update_journeys()
    generate_geojson(
        None,
        version=None
    )

    # bottle.debug(args.debug)

    run_config = {
        'host': '0.0.0.0',
        'port': args.port,
        'debug': args.debug,
        'reloader': args.reloader
        #'server': 'gunicorn'
    }

    print('here')
    bottle.run(
        **run_config
    )


if __name__ == '__main__':
    main()
