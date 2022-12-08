test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
def character_to_priority(char):
    priority = ord(char.lower()) - ord('a') + 1
    if char.isupper():
        priority += 26
    return priority

def group_gen(input):
    lines = input.splitlines()
    for n in range(0, len(lines), 3):
        yield lines[n:n+3]

def get_badge(group):
    commons = set.intersection(*[set(elf) for elf in group])
    assert len(commons) == 1, f'Items {commons} are common in group. Expected exactly one'
    return commons.pop()

def process_input(input):
    return sum(character_to_priority(get_badge(group)) for group in group_gen(input))

assert process_input(test_input) == 70, 'Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.'

with open('input.txt') as f:
    print(process_input(f.read()))