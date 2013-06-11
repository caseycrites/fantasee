# This should contain important urls, such as:
# - where to get league info
# - where to get team info
# - where to get player info
# In addition to the urls, locations of important info within the document
# should be given.

class ESPNMap(object):
    _BASE_URL = 'http://games.espn.go.com'
    _MAP = {
        'league': {
        },
        'team': {
        },
        'player': {
        }
    }
    sport = None
    abbr = None

    _SPORTS_TO_ABBR_MAP = {
        'baseball': 'flb',
        'basketball': 'fba',
        'football': 'ffl',
        'hockey': 'fhl'
    }

    def __init__(self, sport):
        self.sport = sport
        self.abbr = _SPORTS_TO_ABBR_MAP[sport]

    @classmethod
    def for_sport(cls, sport):
        return cls(sport)

    @propery
    def league_map(self):
        return _MAP['league']

    @propery
    def team_map(self):
        return _MAP['team']

    @propery
    def player_map(self):
        return _MAP['player']
