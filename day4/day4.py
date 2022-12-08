test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


def decode_pair(txt):
    return [[int(n) for n in range.split('-')] for range in txt.split(',')]


def one_contains_other(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    elif range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    else:
        return False


def one_overlaps_other(range1, range2):
    if range2[1] >= range1[0] >= range2[0]:
        return True
    elif range1[1] >= range2[0] >= range1[0]:
        return True
    else:
        return False


def puzzle1(txt, f):
    count = 0
    for line in txt.splitlines():
        r1, r2 = decode_pair(line)
        if f(r1, r2):
            count += 1
    return count


assert puzzle1(test_input, one_contains_other) == 2, 'In this example, there are 2 such pairs.'
assert puzzle1(test_input,
               one_overlaps_other) == 4, 'So, in this example, the number of overlapping assignment pairs is 4.'

with open('input.txt') as f:
    txt = f.read()
    print(puzzle1(txt, one_contains_other))
    print(puzzle1(txt, one_overlaps_other))
