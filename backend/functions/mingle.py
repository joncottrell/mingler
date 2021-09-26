import typing
import random
import itertools


def generate_pairings(people: typing.List[str]):
    '''Generate pairs of people for the given number of weeks.'''

    # Get all possible pair combinations. We want to go through each one.
    pairs = list(itertools.combinations(people, 2))
    # Shuffle so it's random!
    random.shuffle(pairs)

    meetings_by_week = []

    while len(pairs) > 0:
        meetings = []

        not_used = []
        candidates = list(pairs)
        for pair in candidates:
            # Don't include a pair this week if either of the participants is already scheduled.
            if not any(pair[0] in meeting or pair[1] in meeting for meeting in meetings):
                meetings.append(pair)
            else:
                not_used.append(pair)

        meetings_by_week.append(meetings)
        pairs = not_used

    return meetings_by_week