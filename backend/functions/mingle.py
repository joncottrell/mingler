import typing
import random
import itertools


def generate_pairings(people: typing.List[str], weeks: int):
    pairs = list(itertools.combinations(people, 2))
    starters = list(random.choices(pairs, k=weeks))
    recent = []
    result = []
    for p in starters:
        pairings = __generate_from([p], recent, pairs)
        recent.append(pairings.copy())
        result.append(pairings.copy())
    return result


def __generate_from(choices, recent_pairings, pairs):
    options = list(filter(lambda c: not any(a in c or b in c for (a, b) in choices), pairs))
    if not options:
        return choices
    while True:
        valid_options = __filter_recent_pairs(options, recent_pairings)
        if len(valid_options) < 2 and len(recent_pairings) > 0:
            recent_pairings.pop(0)
        else:
            break
    choice = random.choice(valid_options)
    choices.append(choice)
    return __generate_from(choices, recent_pairings, pairs)


def __filter_recent_pairs(options, recent_pairings):
    all_recent_pairings = [item for sublist in recent_pairings for item in sublist]
    return list(filter(lambda c: not any(c is a for a in all_recent_pairings), options))

