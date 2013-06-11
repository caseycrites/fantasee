from collections import Counter
import re

from bs4 import BeautifulSoup
import requests

def sanitize_text(text):
    return text.replace(u'\xa0', u'@').replace(', ', ',')

# TODO Give these entities a map and let them build themselves from it.

class Player(object):
    dom_location = 'td.playertablePlayerName'
    name = None
    team = None
    injured = False
    positions = []
    _soup_regex = re.compile(
        r'([^*,]+)(\*?),(\w+)@([^@]+)', flags=re.U
    )

    @classmethod
    def from_soup(cls, soup):
        player = cls()
        matched_player_info = player._soup_regex.match(sanitize_text(soup.text))
        player.name = matched_player_info.group(1)
        player.injured = matched_player_info.group(2) == '*'
        player.team = matched_player_info.group(3)
        player.positions = matched_player_info.group(4).split(',')
        return player

    def __str__(self):
        return '%s plays %s for %s' % (
            self.name, ', '.join(self.positions), self.team
        )

class Team(object):
    dom_location = 'table.playerTableTable'
    name = None
    players = []

    @classmethod
    def from_soup(cls, soup):
        team = cls()
        team.name = soup.select('tr.playerTableBgRowHead > th > a')[0].text
        team.players = [
            Player.from_soup(markup) for markup in
            soup.select(Player.dom_location)
        ]
        return team

    def position_counts(self):
        return Counter([val for sub in self.players for val in sub.positions])

    def injured_players(self):
        return [player for player in self.players if player.injured]

    def __str__(self):
        return '%s has %d players' % (self.name, len(self.players))

class League(object):
    league_id = None
    sport = None
    teams = []

    def __init__(self, sport, league_id, site):
        self.sport = sport
        self.league_id = league_id
        self.site = site

    @classmethod
    def from_sport_and_id(cls, sport, league_id):
        league = cls()
        league.league_id = league_id
        league.sport = sport
        resp = requests.get('%s/%s/leaguerosters?leagueId=%s' % (
            league._BASE_URL, league._SPORTS[sport], league.league_id
        ))
        soup = BeautifulSoup(resp.text)
        league.teams = [
            Team.from_soup(markup) for markup
            in soup.select(Team.dom_location)
        ]
        return league

    def __str__(self):
        return '%s is a %d-team %s league' % (
            self.league_id, len(self.teams), self.sport
        )
