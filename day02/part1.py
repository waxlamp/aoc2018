import collections
import sys

def count_letters(word):
    count = collections.defaultdict(lambda: 0)

    for letter in word:
        count[letter] += 1

    return count


def check_count(value, count):
    for _, val in count.iteritems():
        if val == value:
            return 1

    return 0


def two_three_count(count):
    return [check_count(2, count), check_count(3, count)]


input = map(lambda x: x.strip(), sys.stdin.readlines())

counts = map(lambda x: two_three_count(count_letters(x)), input)
print sum(map(lambda x: x[0], counts)) * sum(map(lambda x: x[1], counts))
