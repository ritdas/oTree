from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'public_policy'
    players_per_group = None
    import csv
    with open('public_policy/webpage.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    weblink = []
    for line in rows:
        weblink.append(line["link"])
    import csv
    with open('public_policy/webpage.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    labels = []
    for line in rows:
        labels.append(line["label"])


    num_repetitions = 1
    num_participants = 225
    num_rounds = int(len(weblink) / num_participants) * num_repetitions
    print('num_rounds', num_rounds)
    print('len(weblinks)', len(weblink))




class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        round_number = self.round_number
        labels = Constants.labels
        for p, label in zip(players, labels):
            p.participant.label = label
        if round_number == 1:
            tripled = Constants.weblink * Constants.num_repetitions
            start = 0
            for p in players:
                end = start+Constants.num_rounds
                p.participant.vars['weblinks'] = tripled[start:end]
                start = end

        for p in players:
            p.weblink = p.participant.vars['weblinks'][round_number - 1]
            if round_number == Constants.num_rounds:
                del p.participant.vars['weblinks']



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    weblink = models.StringField()
