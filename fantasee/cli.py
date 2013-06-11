import argparse
import sys

from bs4 import BeautifulSoup
import requests

from models import FantasyTeam, Player

_URL_FORMAT = 'http://games.espn.go.com/%s/leaguerosters?leagueId=%s'
_SPORT_CHOICES = ['baseball', 'basketball', 'football', 'hockey']
_LEAGUE_ABBRS = dict(zip(_SPORT_CHOICES, ['flb', 'fba', 'ffl', 'fhl']))

def init():
    parser = argparse.ArgumentParser('Get ESPN fantasy sports info.')
    parser.add_argument(
        'sport', help='The sport you want.', choices=_SPORT_CHOICES
    )
    parser.add_argument('league_id', help='Your public league id.')
    return parser.parse_args()

def main():
    args = init()
    resp = requests.get(_URL_FORMAT % (
        _LEAGUE_ABBRS[args.sport], args.league_id)
    )
    soup = BeautifulSoup(resp.text)

    teams_markup = soup.select('table.playerTableTable')
    teams = [FantasyTeam.from_soup(markup) for markup in teams_markup]
    for team in teams:
        print team.name
        for injured_player in team.injured_players():
            print injured_player

if __name__ == '__main__':
    sys.exit(main())
