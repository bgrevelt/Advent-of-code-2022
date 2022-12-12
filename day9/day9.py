class Rope:
    def __init__(self, knots):
        self.knots = [(0,0)] * knots
        self.tail_positions = {self.knots[-1]}

    def move(self, dir, dst):
        assert dir in ['R','U','L','D']
        if dir == 'R':
            dir = 1,0
        elif dir == 'U':
            dir = 0,1
        elif dir == 'L':
            dir = -1,0
        elif dir == 'D':
            dir = 0,-1

        for _ in range(dst):
            self.knots[0] = self.knots[0][0] + dir[0], self.knots[0][1] + dir[1]

            for n in range(1,len(self.knots)):
                self.knots[n] = self.move_tail(self.knots[n-1], self.knots[n])
            self.tail_positions.add(self.knots[-1])

    def move_tail(self, head, tail):
        hx, hy = head
        tx, ty = tail
        dx = hx-tx
        dy = hy-ty
        if abs(dx) <= 1 and abs(dy) <= 1:
            return tx,ty
        if dx < 0:
            dx = -1
        elif dx > 0:
            dx = 1
        if dy < 0:
            dy = -1
        elif dy > 0:
            dy = 1

        return tx+dx, ty+dy



test_input = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

test_input2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

def puzzle(input, knots):
    r = Rope(knots)
    for line in input.splitlines():
        dir, dst = line.split()
        r.move(dir, int(dst))

    return len(r.tail_positions)


assert puzzle(test_input, 2) == 13, "So, there are 13 positions the tail visited at least once."
assert puzzle(test_input, 10) == 1, "In this example, the tail never moves, and so it only visits 1 position."
assert puzzle(test_input2, 10) == 36, "Now, the tail (9) visits 36 positions (including s) at least once"

with open('input.txt') as f:
    txt = f.read()
    print(f'Puzzle 1: {puzzle(txt, 2)}')
    print(f'Puzzle 2: {puzzle(txt, 10)}')