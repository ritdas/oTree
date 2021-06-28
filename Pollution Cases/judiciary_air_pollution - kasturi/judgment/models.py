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
    name_in_url = 'judgment'
    players_per_group = None

    import csv
    with open('judgment/cases.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    judlink = []
    for line in rows:
        judlink.append(line["Kanoon_id"])


    with open('judgment/autofill.csv', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        judgment_db = [
            {"sl":        row["sl_no"],
             "judge_name" :  row["judge_name"].title(),
             "districts" : row["districts"],
             "states" : row["states"],
             "not_in_db" :   False }
            for row in reader]
        judge_names = list(set([r["judge_name"] for r in judgment_db]))
        districts = list(set([r["districts"] for r in judgment_db]))
        states = list(set([r["states"] for r in judgment_db]))


    num_repetitions = 1
    num_participants = 16
    num_rounds = int(len(judlink) / num_participants) * num_repetitions
    print('num_rounds', num_rounds)
    print('len(judlinks)', len(judlink))


class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        round_number = self.round_number
        if round_number == 1:
            tripled = Constants.judlink * Constants.num_repetitions
            start = 0
            for p in players:
                end = start+Constants.num_rounds
                p.participant.vars['judlinks'] = tripled[start:end]
                start = end

        for p in players:
            p.judlink = p.participant.vars['judlinks'][round_number - 1]
            if round_number == Constants.num_rounds:
                del p.participant.vars['judlinks']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    judlink = models.StringField()
    caseid = models.StringField(blank=True)
    judge1 = models.StringField()
    judge2 = models.StringField(blank=True)
    judge3 = models.StringField(blank=True)
    petitioners = models.StringField()
    respondents = models.StringField()
    appeal = models.StringField(label="Appeal Case?", choices=["Yes", "No"])
    constitutional = models.StringField(label="Constitutional Case?", choices=["Yes", "No"])
    petn_advocate = models.StringField()
    resp_advocate = models.StringField()
    company = models.StringField(blank=True)
    state = models.StringField(blank=True)
    district = models.StringField(blank=True)
    # river = models.StringField(blank=True)
    govrole = models.StringField(label="Government's Role", choices=["Petitioner", "Respondent", "Both", "None"])
    socimp = models.StringField(label="Is this judgment likely to have a positive impact on the environment?", choices=["Yes", "No"])
