from os import environ


SESSION_CONFIGS = [
    dict(
        name='quadvoting',
        display_name="Quadratic Voting Survey",
        num_demo_participants=1,
        app_sequence=['quadvoting'],
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='quadvoting',
        display_name='Quadratic Voting Survey',
    ),

]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """
# DEMO_PAGE_INTRO_HTML = """
# Here are some oTree games.
# """

# don't share this with anybody.
SECRET_KEY = '--vyf%1v4#(s5^($acrrfdp2j=+gv)y9g#c9w$=p!cq5%%3nx_'

INSTALLED_APPS = ['otree']

