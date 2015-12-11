#!python

import click
import re
import itertools

@click.command()
@click.option('--file', default='day9/input.txt', help='Input file path')
def run(file):
    destinations = []
    route_distances = []
    distances = {}
    route_re = re.compile(r'^([^ ]+) to ([^ ]+) = ([0-9]+)')
    with click.open_file(file) as strings:
        for row in strings:
            row = row.rstrip()
            route_info = re.match(route_re, row)

            place1 = route_info.group(1)
            place2 = route_info.group(2)
            distance = route_info.group(3)

            if place1 not in destinations:
                destinations.append(place1)
            if place2 not in destinations:
                destinations.append(place2)

            if place1 not in distances.keys():
                distances[place1] = {}
            distances[place1][place2] = int(distance)

            if place2 not in distances.keys():
                distances[place2] = {}
            distances[place2][place1] = int(distance)

    for comb in itertools.permutations(destinations):
        dist = 0
        for idx in range(len(comb)-1):
            place_from = comb[idx] 
            place_to = comb[idx+1]
            dist += distances[place_from][place_to]
        route_distances.append(dist)


    click.echo('Shortest distance is {}'.format(min(route_distances)))
    click.echo('Longest distance is {}'.format(max(route_distances)))


if __name__ == '__main__':
    run()
