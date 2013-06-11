from collections import Counter
import re

def sanitize_text(text):
    return text.replace(u'\xa0', u'@').replace(', ', ',')

class Player(object):
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

class FantasyTeam(object):
    name = None
    players = []

    @classmethod
    def from_soup(cls, soup):
        team = cls()
        team.name = soup.select('tr.playerTableBgRowHead > th > a')[0].text
        team.players = [
            Player.from_soup(markup) for markup in
            soup.select('td.playertablePlayerName')
        ]
        return team

    def position_counts(self):
        return Counter([val for sub in self.players for val in sub.positions])

    def injured_players(self):
        return [player for player in self.players if player.injured]

    def __str__(self):
        return '%s has %d players' % (self.name, len(self.players))
