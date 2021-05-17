from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Results(Page):
    form_model = 'player'
    form_fields = ['judge1',
                   'judge2',
                   'judge3',
                   'petitioners',
                   'onbehalf',
                   'respondents',
                   'petn_advocate',
                   'resp_advocate',
                   'company',
                   'state',
                   'river',
                   'appeal',
                   'constitutional',
                   'govrole',
                   'socimp'
                   ]
    def vars_for_template(self):
        return dict(link='Kanoon_html/{}.html'.format(self.player.judlink)
                    )

    def js_vars(self):
        return dict(
            judges=Constants.judge_names,
        )

class End(Page):
    pass

page_sequence = [
                 Results,
                 ]