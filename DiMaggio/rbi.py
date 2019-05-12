import numpy as np
import itertools


# return the longest "streak" of values in an array
# that are greater than 0
def max_streak(bits):
    maxvalue=0
    for bit, group in itertools.groupby(bits):
        if bit:
            maxvalue=max(maxvalue,sum(group))
    return maxvalue


# Batting average of each hitter
hitters = [.200, .250, .300, .350, .400, .500]

# Career parameters
seasons = 20
games = 160
at_bats = 4
num_sims = 10000
streak_to_beat = 56


# for each hitter
for c, hitter in enumerate(hitters):

    # Create a random array, consisting of a uniform random draw
    # for each career at-bat
    if c == 5:
        seasons = 10

    draws = np.random.uniform(0, 1, (num_sims, seasons*games, at_bats))

    # Fill array with 1/0 signifying a hit/miss
    # based on that hitters batting average
    draws[draws <= hitter] = 1
    draws[draws < 1] = 0


    # consolidate the third(?) dimension of the array to just a
    # 1/0 based on whether or not the hitter got a hit in any
    # of the four at-bats
    sims = draws.max(axis=2)

    # Number of times the hitter breaks the 56-game streak
    x = [1 if max_streak(sim) > streak_to_beat else 0 for sim in sims]

    print(f"The {hitter} hitter beat the {streak_to_beat}-game streak "\
            f"{sum(x)} times in {num_sims} simulations. ({(sum(x) / num_sims * 100)}%)")


