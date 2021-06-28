from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Results(Page):
  form_model = 'player'
  form_fields = ['caseid',
           'judge1',
           'judge2',
           'judge3',
           'petitioners',
           'respondents',
           'petn_advocate',
           'resp_advocate',
           'company',
           'district',
           'state',
           'appeal',
           'constitutional',
           'govrole',
           'socimp',
           'reflection'
           ]
  def vars_for_template(self):
    return dict(link='Kanoon_html/{}.html'.format(self.player.judlink)
          )

  def js_vars(self):
    return dict(
      judges=Constants.judge_names,
      districts=Constants.districts,
      states=Constants.states,
    )

  def post(self):
    post_data = self.request.POST.dict()
    # append pettioners data
    for i in range(2,11):
      petitioner = 'petitioners' + str(i)
      try:
        if post_data[petitioner]:
          petitioners_string = str(post_data['petitioners']) + ', ' + str(post_data[petitioner])
          post_data.update({'petitioners': petitioners_string})
      except:
        pass
    # append respondents data
    for i in range(2,11):
      respondent = 'respondents' + str(i)
      try:
        if post_data[respondent]:
          respondents_string = str(post_data['respondents']) + ', ' + str(post_data[respondent])
          post_data.update({'respondents': respondents_string})
      except:
        pass
    # append pettioners advocate data
    for i in range(2,11):
      petitioneradv = 'petn_advocate' + str(i)
      try:
        if post_data[petitioneradv]:
          petitionersadv_string = str(post_data['petn_advocate']) + ', ' + str(post_data[petitioneradv])
          post_data.update({'petn_advocate': petitionersadv_string})
      except:
        pass
    # append respondents advocate data
    for i in range(2,11):
      respondentadv = 'resp_advocate' + str(i)
      try:
        if post_data[respondentadv]:
          respondentsadv_string = str(post_data['resp_advocate']) + ', ' + str(post_data[respondentadv])
          post_data.update({'resp_advocate': respondentsadv_string})
      except:
        pass

    self.request.POST = post_data
    return super().post()


class End(Page):
  pass

page_sequence = [
         Results,
         ]