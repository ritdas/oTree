from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):
        return dict(link="https://www.youtube.com/embed/{}".format(self.player.weblink)
                    )


# class ResultsWaitPage(WaitPage):
#     pass


class Results(Page):
    pass


page_sequence = [MyPage, Results]
