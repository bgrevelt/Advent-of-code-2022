test_input = '''A Y
B X
C Z'''

def result(mine, theirs):
    r = {
('rock', 'rock') : 'draw',
('rock', 'paper') : 'loss',
('rock', 'scissors') : 'win',
('paper', 'rock') : 'win',
('paper', 'paper') : 'draw',
('paper', 'scissors') : 'loss',
('scissors', 'rock') : 'loss',
('scissors', 'paper') : 'win',
('scissors', 'scissors') : 'draw',
}
    return r[(mine, theirs)]

def code_to_move(code):
    r = {
    'A':'rock',
    'B':'paper',
    'C':'scissors',
    'X':'rock',
    'Y':'paper',
    'Z':'scissors'
    }
    return r[code]

def codes_to_moves(code1, code2):
    return code_to_move(code1), code_to_move(code2)

def shape_to_score(move):
    scores = {
        'rock':1,
        'paper':2,
        'scissors':3
    }
    assert move in scores
    return scores[move]

def outcome_to_score(outcome):
    scores = {
        'win':6,
        'draw':3,
        'loss':0
    }

    assert outcome in scores
    return scores[outcome]


def compute_round_score(moves, codes_to_moves_f):
    theirs, mine = moves
    theirs, mine = codes_to_moves_f(theirs, mine)
    outcome = result(mine, theirs)
    return outcome_to_score(outcome) + shape_to_score(mine)

def compute_score(input, puzzle_nr):
    return sum(compute_round_score(round.split(), codes_to_moves if puzzle_nr == 1 else codes_to_moves_new) for round in input.splitlines())

assert compute_score(test_input, 1) == 15, "In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6)."

with open('input.txt') as f:
    print(compute_score(f.read(), 1))

def codes_to_moves_new(theirs, mine):
    winners = {
        'rock' : 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    losers = {v:k for k,v in winners.items()}

    their_move = code_to_move(theirs)

    if mine == 'X': #We want to lose
        return their_move, losers[their_move]
    elif mine == 'Y': #We want to tie
        return their_move, their_move
    else: #We want to win
        return their_move, winners[their_move]

assert compute_score(test_input, 2) == 12, "Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12."

with open('input.txt') as f:
    print(compute_score(f.read(), 2))