test_input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

def get_max_calories_per_elf(text):
    return max(sum([int(snack) for snack in elf.split('\n')]) for elf in text.split('\n\n'))

assert get_max_calories_per_elf(test_input) == 24000, "In the example above, this is 24000 (carried by the fourth Elf)."

with open('input.txt') as f:
    print(get_max_calories_per_elf(f.read()))

def get_sum_calories_top_three_elves(text):
    return sum(sorted([sum([int(snack) for snack in elf.split('\n')]) for elf in text.split('\n\n')])[-3:])

assert get_sum_calories_top_three_elves(test_input) == 45000, "The sum of the Calories carried by these three elves is 45000."

with open('input.txt') as f:
    print(get_sum_calories_top_three_elves(f.read()))