import argparse
from collections import defaultdict

from via.utils import (
    get_journeys,
    get_combined_id,
    force_list
)


def print_condition(journeys, min_edge_usage):
    """

    :param journeys:
    :param min_edge_usage:
    """

    journeys_graph = journeys.graph
    used_edge_data = defaultdict(list)

    used_edges = journeys.edge_quality_map
    for (u, v, k, d) in journeys_graph.edges(keys=True, data=True):
        combined_id = get_combined_id(u, v)
        try:
            used_edge_data[d['name']] = {
                **used_edges[combined_id],
                **d
            }
        except:
            pass

    name_quality_map = defaultdict(list)
    for edge in used_edge_data.values():
        for name in force_list(edge.get('name', [])):
            name_quality_map[name].append(edge['avg'])

    name_quality_map = sorted(
        used_edge_data.items(),
        key=lambda x: x[1]['avg'],
        reverse=True
    )

    for street_name, quality in name_quality_map:
        print('%s: %s' % (street_name.ljust(30), quality['avg']))


def main():

    parser = argparse.ArgumentParser()

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
    print_condition(journeys, args.min_edge_usage)


if __name__ == '__main__':
    main()
