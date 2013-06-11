import argparse
import sys
import yaml

from models import FantasyLeague

def _load_config():
    config = yaml.load('config.yaml')

def _init():
    _load_config()
    parser = argparse.ArgumentParser('Get ESPN fantasy sports info.')
    parser.add_argument(
        'sport', help='The sport you want.', choices=FantasyLeague._SPORTS.keys()
    )
    parser.add_argument('league_id', help='Your public league id.')
    return parser.parse_args()

def main():
    args = _init()
    league = FantasyLeague.from_sport_and_id(args.sport, args.league_id)
    print league

if __name__ == '__main__':
    sys.exit(main())
