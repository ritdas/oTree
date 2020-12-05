from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, bigger, lottery_generator

import numpy as np
import pandas as pd
import time

class Initial(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        endowment = self.session.vars['endowment']
        pound = endowment / self.session.vars['exchange']

        if pound.is_integer():
            pound = int(pound)

        reward = 12
        risk = 75

        risk_up = str(100 - risk)
        risk_up_px = ((100 - risk) / 100) * 300
        risk_down = str(risk)
        risk_down_px = (risk / 100) * 300

        bid = 8.5
        sell = 5.6
        win = endowment - sell + reward
        loss = endowment - sell

        return {
            'endowment': '$' + str(endowment),
            'pound': '£' + str(pound),

            'reward': '$' + str(reward),

            'risk_up': risk_up,
            'risk_up_px': str(risk_up_px)+"px",
            'risk_down': risk_down,
            'risk_down_px': str(risk_down_px)+"px",

            'risk_up_posi': str(risk_up_px * 0.5 - 20)+"px",
            'risk_down_posi': str(risk_down_px * 0.5 - 20)+"px",

            'bid': '$' + str(bid),
            'sell': '$' + str(sell),
            'win': '$' + str(win),
            'loss': '$' + str(loss),
        }

    def before_next_page(self):

        t = 1000 * time.time() # current time in milliseconds
        self.participant.vars['seed2'] = int(t) % 2**32



class Auction(Page):

    form_model = 'player'
    form_fields = ['WTP']


    def vars_for_template(self):
        floor = Constants.floor
        ceiling = Constants.ceiling


        return {

            'floor': '$' + str(floor),
            'ceiling': '$' + str(float(ceiling)),

        }




class FinishPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        wtp = self.player.WTP
        dice = np.random.randint(Constants.floor, Constants.ceiling)
        if dice > wtp:
            scenario_auc = 1
        else:
            scenario_auc = 2


        return {
            'scenario_auc': scenario_auc,
            'wtp': wtp,
            'dice' : dice,
                }

page_sequence = [
Initial,
Auction,
FinishPage
]
