"""Program that generates click-bait titles"""

import random
import inflect

# use inflect for more correct plurals for tricky nouns
inf = inflect.engine()

# define the headline parts
OBJECT_PRONOUNS = ('her', 'him', 'them')
POSSESIVE_PRONOUNS = ('her', 'his', 'their')
PERSONAL_PRONOUNS = ('she', 'he', 'they')
NOUN_FILE = 'nouns.txt'
PLACES_FILE = 'places.txt'
STATES_FILE = 'states.txt'
WHEN_PAST = ('in the past', 'last month', 'last week', 'last year', 'previously', 'yesterday')
WHEN_PRESENT = (
    'immediately',
    'literally this very minute!',
    'now!',
    'right now!',
    'this month',
    'this week',
    'this year',
)
WHEN_FUTURE = (
    'in 24 hours',
    'in the future',
    'next month',
    'next week',
    'next year',
    'previously',
    'soon',
    'tomorrow',
)

# fetch nouns, places, states, and when words
with open(NOUN_FILE, 'r', encoding='utf-8') as f:
    NOUNS = tuple(x.strip().title() for x in f.readlines())

with open(PLACES_FILE, 'r', encoding='utf-8') as f:
    PLACES = tuple(x.strip().title() for x in f.readlines())

with open(STATES_FILE, 'r', encoding='utf-8') as f:
    STATES = tuple(x.strip().title() for x in f.readlines())


def main():
    headline_count = get_headline_number()

    # print a random headline as many times as the number of headlines requested
    for count in range(headline_count):
        # all possible headlines
        headlines = {
            1: make_big_company_haters(),
            2: make_do_not_want_you_to_know(),
            3: make_millennials_killing(),
            4: make_without_this_you_may_have_died(),
            5: make_without_this_you_will_die_later(),
            6: make_without_this_you_will_die_now(),
            7: make_you_will_not_believe(),
        }

        headline_num = random.randint(1, len(headlines))
        print(f'{count + 1}. {headlines[headline_num]}')


def get_headline_number():
    """Returns how many click-bait headlines to produce"""
    while True:
        try:
            headline_count = int(input('How many click-bait headlines do you need?: '))
        except ValueError:
            print('Please enter a valid number.')
        else:
            break
    return headline_count


def make_millennials_killing():
    noun = get_noun()
    return f'Are Millenials Killing the {noun} industry?'


def make_without_this_you_will_die_now():
    """Returns a headline about dying in the present without this one thing"""
    noun = get_noun()
    plural_noun = inf.plural(get_noun())
    when = get_when_present()
    return f'Without This {noun}, {plural_noun} Could Kill You {when}'


def make_without_this_you_will_die_later():
    """Returns a headline about dying in the future without this one thing"""
    noun = get_noun()
    plural_noun = inf.plural(get_noun())
    when = get_when_future()
    return f'Without This {noun}, {plural_noun} Could Kill You {when}'


def make_without_this_you_may_have_died():
    """Returns a headline about dying in the past without this one thing"""
    noun = get_noun()
    plural_noun = inf.plural(get_noun())
    when = get_when_past()
    return f'Without This {noun}, {plural_noun} Could\'ve Killed You {when}'


def make_big_company_haters():
    """Returns a 'big companies hate...' headline"""
    object_pronoun = get_object_pronoun()
    state = get_state()
    noun1 = get_noun()
    noun2 = get_noun()
    return f'Big Companies Hate {object_pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def make_you_will_not_believe():
    "Returns a 'you won't believe...' headline"
    state = get_state()
    noun = get_noun()
    possesive_pronoun = get_possesive_pronoun()
    place = get_place()
    return f'You Won\'t Believe What This {state} {noun} Found in {possesive_pronoun} {place}'


def make_do_not_want_you_to_know():
    """Returns a 'they don't want you to know...' headline"""
    plural_noun = inf.plural(get_noun())
    plural_noun2 = inf.plural(get_noun())
    return f'What {plural_noun} Don\'t Want You To Know About {plural_noun2}'


def get_noun():
    """Returns a random noun"""
    return random.choice(NOUNS)


def get_state():
    """Returns a random state"""
    return random.choice(STATES)


def get_personal_pronoun():
    """Returns a random personal pronoun"""
    return random.choice(PERSONAL_PRONOUNS)


def get_possesive_pronoun():
    """Returns a random possesive pronoun"""
    return random.choice(POSSESIVE_PRONOUNS)


def get_object_pronoun():
    """Returns a random object pronoun"""
    return random.choice(OBJECT_PRONOUNS)


def get_when_past():
    """Returns a random time in the past"""
    return random.choice(WHEN_PAST)


def get_when_present():
    """Returns a random time in the present"""
    return random.choice(WHEN_PRESENT)


def get_when_future():
    """Returns a random time in the future"""
    return random.choice(WHEN_FUTURE)


def get_place():
    """Returns a random place"""
    return random.choice(PLACES)


if __name__ == '__main__':
    main()
