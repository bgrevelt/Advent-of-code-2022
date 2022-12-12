import math

test_input = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

class Monkey:
    def __init__(self, number, items, operation, test, monkey_pass, monkey_fail, auto_realx):
        self.number = number
        self._items = items
        self._operation = operation
        self._test = test
        self.monkey_throw = {False:monkey_fail, True:monkey_pass}
        self.inspection_count = 0
        self._auto_relax = auto_realx
        self._max = None

    def add_item(self, item):
        self._items.append(item)

    def setmax(self, max):
        self._max = max

    def take_turn(self):
        r = []
        self.inspection_count += len(self._items)
        for item in self._items:
            '''Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.'''
            item = self._operation(item)
            if self._auto_relax:
                item = item // 3
            item = item % self._max
            if self._test(item) != self._test(item % self._max):
                print('bla')
            throw_to = self.monkey_throw[self._test(item)]
            r.append((item,throw_to))
        self._items = []
        return r

def parse_input(input, auto_relax):
    monkeys = []
    # These items are really only used for determining if they're divisible by x,y,or z
    # if N is divisible by X,Y,or Z, so is N % (X*Y*Z). This means we only have to to
    # store that remainder. Which makes life a whole lot eaier when we get to really large numbers
    # in puzzle 2. divider_product contains a running sum of all these dividers and is fed to all monkeys after all
    # input has been processed.
    divider_product = 1
    for monkey in input.split('\n\n'):
        id, items, operation, test, true, false = monkey.splitlines()
        id = int(id.split(' ')[1][:-1])
        items = [int(n) for n in items[len('  Starting items: '):].split(',')]

        assert operation.startswith('  Operation: new = ')
        operation = operation[len('  Operation: new = '):]
        a,op,b = operation.split(' ')

        assert a == 'old'
        assert op in ['+', '*'], op
        if op == '+':
            if b == 'old':
                operation = lambda a: a+a
            else:
                val = int(b)
                operation = lambda a, val=val: a + val
        else: # op == '*'
            if b == 'old':
                operation = lambda a: a*a
            else:
                val = int(b)
                operation = lambda a,val=val: a * val

        assert test.startswith('  Test: divisible by ')
        test = test[len('  Test: divisible by '):]
        test_value = int(test)
        test = lambda x,test_value=test_value: x%test_value == 0
        divider_product *= test_value

        assert true.startswith('    If true: throw to monkey ')
        true = int(true[len('    If true: throw to monkey '):])
        assert false.startswith('    If false: throw to monkey ')
        false = int(false[len('    If false: throw to monkey '):])


        monkeys.append(Monkey(id, items, operation, test, true, false, auto_relax))

    for monkey in monkeys:
        monkey.setmax(divider_product)
    return monkeys

def puzzle(input, rounds, auto_relax, verbose=False):
    monkeys = parse_input(input, auto_relax)
    monkeys_by_id = {monkey.number:monkey for monkey in monkeys}
    for n in range(rounds):
        for monkey in monkeys:
            for worry_level, thrown_to in monkey.take_turn():
                monkeys_by_id[thrown_to].add_item(worry_level)
        if verbose:
            print(f'End of round {n+1}')
            for monkey in monkeys:
                print(f'Monkey {monkey.number} inspected {monkey.inspection_count} times')
    inspection_counts = sorted([monkey.inspection_count for monkey in monkeys])
    monkey_business_level = inspection_counts[-1] * inspection_counts[-2]
    return monkey_business_level

def puzzle1(input):
    return puzzle(input, rounds=20, auto_relax=True)

assert puzzle1(test_input) == 10605, "The level of monkey business in this situation can be found by multiplying these together: 10605."

def puzzle2(input):
    return puzzle(input, rounds=10000, auto_relax=False)

assert puzzle2(test_input) == 2713310158, '''After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of monkey business in this situation is now 2713310158.'''

with open('input.txt') as f:
    txt = f.read()
    print(f'Puzzle 1: {puzzle1(txt)}')
    print(f'Puzzle 2: {puzzle2(txt)}')