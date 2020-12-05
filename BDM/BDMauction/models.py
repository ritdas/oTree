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
 import numpy as np
 import pandas as pd
 import re
 import time

author = 'Your name here'

doc = """
Your app description
"""

def lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, treatment):

    rewards = []
    risks = []

    counter = 1
    if treatment == 'A':
        while counter <= reward_lev:
            rewards.append(min_reward)
            min_reward *= scaler
            min_reward = round(min_reward, 2)
            counter += 1
    else:
        while counter <= reward_lev:
            rewards.append(round(min_reward))
            min_reward *= scaler
            min_reward = round(min_reward, 2)
            counter += 1

    counter = 1
    if treatment == 'A':
        while counter <= risk_lev:
            risks.append(min_risk)
            min_risk *= scaler
            min_risk = round(min_risk)
            counter += 1
    else:
        while counter <= risk_lev:
            risks.append(round(min_risk / 10) * 10)
            min_risk *= scaler
            min_risk = round(min_risk)
            counter += 1

    lottery_list = []

    for reward in rewards:
        for risk in risks:
            lottery_list.append([reward, risk])

    lottery_table = pd.DataFrame(lottery_list)

    columns = ['reward', 'risk']
    lottery_table.columns = columns


    return lottery_table

# The valus of these variables need to be kept same with those in the page.py
scaler = 2**0.5
min_reward = 7.85
min_risk = 41
reward_lev = 4
risk_lev = 3


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


class Constants(BaseConstants):
    name_in_url = 'BDMauction'
    players_per_group = None
    num_rounds = 1
    floor = 0
    ceiling = 100


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['endowment'] = 25 # $ assigned in one part
            self.session.vars['exchange'] = 5 # $/£
            # The above should be set in the REI test, they are put here for the convenience of testing only.

            for p in self.get_players():
                p.participant.vars['treatment'] = 'E'



class Group(BaseGroup):
    pass

class Player(BasePlayer):

    WTP = models.IntegerField()

    def WTP_error_message(self, value):


        if value >= Constants.ceiling:
             return "your bid price is above the reasonable price range."

        if value <= Constants.floor:
             return "your bid price is below the reasonable price range."

