import argparse

from via.utils import (
    get_journeys,
    get_combined_id
)


def print_coverage(journeys, min_edge_usage):
    """

    :param journeys:
    :param min_edge_usage:
    """

    journeys_graph = journeys.bounding_graph
    used_edge_ids = set()
    used_edge_data = {}

    for journey in journeys:
        bounding_graph = journey.bounding_graph
        used_edges = set(list(journey.edge_quality_map.keys()))
        for (u, v, k, d) in bounding_graph.edges(keys=True, data=True):
            combined_id = get_combined_id(u, v)
            if combined_id in used_edge_ids:
                continue
            used_edge_ids.add(combined_id)

            if combined_id in used_edges:
                if combined_id not in used_edge_data.keys():
                    used_edge_data[combined_id] = {
                        'used_times': 1,
                        **d
                    }
                else:
                    used_edge_data[combined_id]['used_times'] += 1

    total_length = 0
    for (u, v, k, d) in journeys_graph.edges(keys=True, data=True):
        total_length += d['length']

    used_length = sum(
        [
            d['length'] for d in used_edge_data.values() if d['used_times'] >= min_edge_usage
        ]
    )

    coverage_perc = (used_length / total_length) * 100
    print('Coverage: %s%%' % (round(coverage_perc, 2)))


def main():

    parser = argparse.ArgumentParser()

    # TODO: ability to define a bbox / polygon for the coverage to cover

    parser.add_argument(
        '--min-edge-usage',
        dest='min_edge_usage',
        type=int,
        help='The minimum number of times an edge has to be used for it to be included in the final data (1 per journey)',
        default=1
    )
    parser.add_argument(
        '--transport-type',
        dest='transport_type',
        default=None,
        help='bike/car/scoorter or whatever else is on the app'
    )
    parser.add_argument(
        '--place',
        dest='place',
        default='Dublin, Ireland',
        help='What place to limit the data to (so you don\'t try to visualize too big an area). Must be an osmnx recognised place / format for example "Dublin, Ireland"'
    )
    args = parser.parse_args()

    journeys = get_journeys(
        transport_type=args.transport_type,
        source='remote',
        place=args.place
    )
    print_coverage(journeys, args.min_edge_usage)


if __name__ == '__main__':
    main()
