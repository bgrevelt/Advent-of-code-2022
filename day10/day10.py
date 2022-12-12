from functools import reduce

class Processor:
    def __init__(self):
        self._instructions = []
        self._pseudo_instructions = []
        self._program_counter = 0
        self._registerx = 1

    def load(self, input):
        for op in input:
            if op.startswith('addx'):
                # hacky way to implement an addition instruction taking two cycles
                self._pseudo_instructions.append('noop')
            self._pseudo_instructions.append(op)

    def registerx(self):
        return self._registerx

    def tick(self, count=1):
        for _ in range(count):
            r = self._tick()
        return r

    def sprite_on_pixel_pos(self, pos):
        return self._registerx -1 <= pos <= self.registerx()+1

    def _tick(self):
        prev_regx = self._registerx
        self._process_instruction()
        self._program_counter += 1
        return self._program_counter * prev_regx

    def _process_instruction(self):
        op = self._pseudo_instructions[self._program_counter]
        if op.startswith('noop'):
            return
        elif op.startswith('addx'):
            _, val = op.split(' ')
            val = int(val)
            self._registerx += val

test_input = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

p = Processor()
p.load(test_input.splitlines())

assert p.tick(20) == 420, 'During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420.'
assert p.tick(40) == 1140, 'During the 60th cycle, register X has the value 19, so the signal strength is 60 * 19 = 1140.'
assert p.tick(40) == 1800, 'During the 100th cycle, register X has the value 18, so the signal strength is 100 * 18 = 1800.'
assert p.tick(40) == 2940, 'During the 140th cycle, register X has the value 21, so the signal strength is 140 * 21 = 2940.'
assert p.tick(40) == 2880, 'During the 180th cycle, register X has the value 16, so the signal strength is 180 * 16 = 2880.'
assert p.tick(40) == 3960, 'During the 220th cycle, register X has the value 18, so the signal strength is 220 * 18 = 3960.'

def puzzle1(input):
    p = Processor()
    p.load(input.splitlines())

    return sum(p.tick(count) for count in [20,40,40,40,40,40])

def puzzle2(input):
    p = Processor()
    p.load(input.splitlines())

    for y in range(6):
        line = ""
        for x in range(40):
            line += '#' if p.sprite_on_pixel_pos(x) else ' '
            p.tick()
        print(line)


assert puzzle1(test_input) == 13140, "The sum of these signal strengths is 13140"

with open('input.txt') as f:
    txt = f.read()
    print(f'Puzzle1: {puzzle1(txt)}')
    puzzle2(txt)