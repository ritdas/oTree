from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from random import shuffle

author = ''

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'qv'
    players_per_group = None
    num_rounds = 1

    # Survey parameters
    survey_default_title = 'Survey'
    vote_credits = 100
    import csv
    with open('quadvoting2/sample.csv', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    que = []
    for line in rows:
        que.append(line["ques"])
    shuffle(que)
    questions_labels = que[1:21]

    questions = [{'name': 'q' + str(n + 1), 'label': l} for n, l in enumerate(questions_labels)]


class Subsession(BaseSubsession):
    def creating_session(self):
        if 'Survey_Title' in self.session.config:
            self.session.vars['survey_title'] = self.session.config['Survey_Title']
        else:
            self.session.vars['survey_title'] = Constants.survey_default_title

        questions = Constants.questions.copy()
        for p in self.get_players():
            shuffle(questions)
            p.participant.vars['questions'] = questions


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    for q in Constants.questions:
        locals()[q['name']] = models.IntegerField(label=q['label'], min=0, max=10, initial=0)
        locals()[q['name'] + '_agree'] = models.BooleanField(blank=True)
        # locals()[q['name'] + '_text'] = q['label']
    del q

