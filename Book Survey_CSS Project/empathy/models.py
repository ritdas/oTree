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


# class Constants(BaseConstants):
#     name_in_url = 'empathy'
#     players_per_group = None
#     num_rounds = 1
#
#
# class Subsession(BaseSubsession):
#     pass
#
#
# class Group(BaseGroup):
#     pass
#
#
# class Player(BasePlayer):
#     pass

class Constants(BaseConstants):
    name_in_url = 'empathy'
    players_per_group = None

    import csv
    with open('empathy/webpage.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    weblink = []
    for line in rows:
        weblink.append(line["link"])
    import csv
    with open('empathy/webpage.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    labels = []
    for line in rows:
        labels.append(line["label"])

    # with open('judgment/autofill.csv', encoding="utf-8") as file:
    #     reader = csv.DictReader(file)
    #     judgment_db = [
    #         {"sl":        row["sl_no"],
    #          "judge_name":  row["judge_name"].title(),
    #          "not_in_db":   False }
    #         for row in reader]
    #     judge_names = list(set([r["judge_name"] for r in judgment_db]))

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