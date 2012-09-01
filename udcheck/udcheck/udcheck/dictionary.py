from collections import namedtuple

Term = namedtuple('Term', ['name', 'definitions'])

class DummyDictionary:
    terms = {
        'baloo': ['A funny name for a bear.'],
        'landmass': ['The area of land between New Orleans and Mobile, as referenced during Hurricane Isaac coverage by The Weather Channel. Also known as Mississippi.',
                     'n. a great and incredible unit of eight individual females brought together by common interests of wine, cheese, and dark chocolate among many other indulgences; also serves as an acronym for these eight beautiful individuals\' first names.'],
        'Old Man Strong': ["AKA Old Man Strength. Usually in Wyoming or some similar place, old men sit around in bars and drink. Young bucks come into town stirring up shit, and for some reason, it is often some old guy who just pounds the shit out of the young guy, much to the amazement of onlookers. Old men seem to possess a certain toughness or hardening process enabling them to give better than they get. Also, and most dangerously, the strongest ones are often quiet and reserved, just waiting to pound the crap out of some yahoo... Other circumstances can be in a construction work crew, the old guy will towards the end of the day when things slack off, just start working like a MoFo, and put the young bucks to shame. Hence, being Old Man Strong.",
                           "Relating to the inexplicable dieselness of of older men. This is usually on display in the gym when the burly gentleman in his 60s walks over to the flat bench, throws three 45 lbs. plates on each side (315 lbs. to those who can't add that fast), and proceeds to bang out 5 sets of 12 reps each with no warm-up. Other examples of this phenomenon are the inability to beat an old guy (particularly a father type) in a fair type regardless of your size compared to his and the seeming ability of old ass men to pick up and carry three times their weight."],
        }

    def __init__(self):
        self.terms = [Term(name=k, definitions=v) for k,v in DummyDictionary.terms.items()]

    def get_random_term(self):
        import random
        return self.terms[random.randint(0, len(self.terms) - 1)]

def create_dictionary():
    return DummyDictionary()