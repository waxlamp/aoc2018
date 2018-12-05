import itertools
import sys

def common_letters(w1, w2):
    assert len(w1) == len(w2)

    return ''.join(map(lambda x: x[0], filter(lambda x: x[0] == x[1], zip(w1, w2))))

input = map(lambda x: x.strip(), sys.stdin.readlines())

print filter(lambda x: len(x) == len(input[0]) - 1, map(lambda x: common_letters(x[0], x[1]), itertools.product(input, input)))[0]
