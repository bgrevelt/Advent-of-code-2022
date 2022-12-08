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

def process_line(line):
    split = len(line) // 2
    first_compartment = line[:split]
    second_compartment = line[split:]
    dups = {c for c in first_compartment if c in second_compartment}
    assert len(dups) == 1, f'{len(dups)} items in both compartiments ({dups}). Expected one'
    return character_to_priority(dups.pop())

def process_input(input):
    return sum(process_line(line) for line in input.splitlines())

assert process_input(test_input) == 157, '''In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157'''

with open('input.txt') as f:
    print(process_input(f.read()))