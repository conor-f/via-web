import argparse

from via.geojson.generate import generate_geojson


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--transport-type',
        dest='transport_type',
        default=None,
        help='bike/car/scooter or whatever else is on the app. Generates all if not specified'
    )
    parser.add_argument(
        '--version',
        dest='version',
        action='store_true'
    )
    args = parser.parse_args()

    generate_geojson(
        args.transport_type,
        version=args.version
    )


if __name__ == '__main__':
    main()
