import itertools
import sys

input = map(int, sys.stdin.readlines())

freqs = set()
freq = 0
for i in itertools.cycle(input):
    freq += i

    if freq in freqs:
        print freq
        break

    freqs.add(freq)
