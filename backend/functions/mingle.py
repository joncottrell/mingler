import typing
import random
import itertools


def generate_pairings(people: typing.List[str], weeks: int):
    '''Generate pairs of people for the given number of weeks.'''

    # Get all possible pair combinations.
    pairs = list(itertools.combinations(people, 2))

    # Pick one random seed pair for each week.
    # ToDo: Make sure these pairs don't repeat.
    starters = list(random.choices(pairs, k=weeks))

    recent = []
    result = []

    # For each week's starting pair, generate pairs that avoid recently
    # assigned pairs.
    for p in starters:
        pairings = __generate_from([p], recent, pairs)
        recent.append(pairings.copy())
        result.append(pairings.copy())

    return result


def __generate_from(choices, recent_pairings, pairs):
    '''Recursively add more pairs to the choices, excluding existing choices and recent 
    pairings. pairs are the set of all possible pairs.'''

    # Filter out all pairs that have someone already in the existing choices for the week.
    options = list(filter(lambda c: not any(a in c or b in c for (a, b) in choices), pairs))

    if not options:
            # If there are no more choices, we either have an odd number, or have paired 
            # everyone.
        return choices

    # Try to find the options that are least recent. Pop oldest recents as
    # we run out of new options.
    while True:
        valid_options = __filter_recent_pairs(options, recent_pairings)
        if len(valid_options) < 2 and len(recent_pairings) > 0:
            recent_pairings.pop(0)
        else:
            break
    
    # Pick a random choice from the remaining options.
    choice = random.choice(valid_options)
    choices.append(choice)

    return __generate_from(choices, recent_pairings, pairs)


def __filter_recent_pairs(options, recent_pairings):
    '''Filter out options which exist in recent pairings already.'''

    all_recent_pairings = [item for sublist in recent_pairings for item in sublist]
    return list(filter(lambda c: not any(c is a for a in all_recent_pairings), options))
