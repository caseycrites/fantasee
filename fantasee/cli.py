import argparse
import sys
import yaml

from models import FantasyLeague

# subparsers
# - league name
#   - stuff

# TODO Optional locations for the config and some defaults
config = yaml.load(open('config.yaml'))

def _add_subparsers(subparsers):
    for key, value in config.items():
        parser = subparsers.add_parser(key)

def _init():
    parser = argparse.ArgumentParser('Get ESPN fantasy sports info.')
    subparsers = parser.add_subparsers(help='Available Leagues', dest='league')
    _add_subparsers(subparsers)
    return parser.parse_args()

def main():
    args = _init()
    league_data = config[args.league]
    league = FantasyLeague.from_sport_and_id(
        league_data['sport'], league_data['id']
    )
    print 'Retrieved data for league %s' % league.league_id

if __name__ == '__main__':
    sys.exit(main())
