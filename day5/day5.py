test_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

def parse_stacks(txt):
    columns = []
    for n, line in enumerate(reversed(txt.splitlines())):
        if n==0:
            number_of_stacks = int(line.split()[-1])
            columns = [[] for _ in range(number_of_stacks)]
        else:
            for column_index, crate_index in enumerate(range(1, len(line), 4)):
                if line[crate_index] != ' ':
                    columns[column_index].append(line[crate_index])
    return columns

def parse_move(txt):
    _, count, _, from_, _, to = txt.split(' ')
    return (int(count), int(from_)-1, int(to)-1)

def parse_moves(txt):
    return [parse_move(line) for line in txt.splitlines()]


def parse_input(txt):
    stacks, moves = txt.split('\n\n')
    stacks = parse_stacks(stacks)
    moves = parse_moves(moves)
    return stacks, moves

def process_move(move, stack, can_move_multiple):
    count, from_, to = move
    if can_move_multiple:
        stack[to] += stack[from_][-1*count:]
    else:
        stack[to] += reversed(stack[from_][-1*count:])
    stack[from_] = stack[from_][:-1*count]
    return stack

def process_moves(moves, stack, can_move_multiple):
    for move in moves:
        stack = process_move(move, stack, can_move_multiple)

    return "".join([col[-1] for col in stack])

def puzzle(txt, puzzle_nr):
    stack, moves = parse_input(txt)
    return process_moves(moves, stack, can_move_multiple=(puzzle_nr == 2))

assert puzzle(test_input, 1) == 'CMZ', 'The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.'
assert puzzle(test_input, 2) == 'MCD', 'In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.'

with open('input.txt') as f:
    txt = f.read()
    print(puzzle(txt, 1))
    print(puzzle(txt, 2))