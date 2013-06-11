# This should contain important urls, such as:
# - where to get league info
# - where to get team info
# - where to get player info
# In addition to the urls, locations of important info within the document
# should be given.

_BASE_URL = 'http://games.espn.go.com'
_SPORTS = {
    'baseball': 'flb',
    'basketball': 'fba',
    'football': 'ffl',
    'hockey': 'fhl'
}
_MAP = {
    'league': {
    },
    'team': {
        'clubhouse': ''
    },
    'player': {
    }
}

class ESPNMap(object):

    sport = None
    abbr = None

    def __init__(self, sport):
        self.sport = sport
        self.abbr = _SPORTS[sport]

    @classmethod
    def for_sport(cls, sport):
        return cls(sport)
