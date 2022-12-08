test_input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''


class FileSystemItem:
    def __init__(self, name, parent):
        self.children = []
        self._parent = parent
        self._name = name

    def qualified(self):
        r = str(self)
        parent = self._parent
        while parent is not None:
            r = f'{parent._name}/{r}'
            parent = parent._parent
        return r


class Directory(FileSystemItem):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)

    def size(self):
        return sum(child.size() for child in self.children)

    def add(self, child):
        self.children.append(child)

    def move_up(self):
        return self._parent

    def root(self):
        parent = self
        while parent.move_up() is not None:
            parent = parent.move_up()
        return parent

    def __str__(self):
        return f'{self._name} (dir, size={self.size()})'

    def print(self, indent=0):
        print(f'{" " * indent * 2}- {str(self)}')
        for child in self.children:
            child.print(indent + 1)


class File(FileSystemItem):
    def __init__(self, name, size, parent):
        super().__init__(name, parent)
        self._size = size

    def size(self):
        return self._size

    def __str__(self):
        return f'{self._name} (file, size={self._size})'

    def print(self, indent=0):
        print(f'{" " * indent * 2}- {str(self)}')


def change_dir(command, cwd):
    assert command[0:5] == '$ cd '
    dir = command[5:]
    if dir == '/':
        return cwd.root()
    if dir == '..':
        return cwd.move_up()
    else:
        dir = Directory(dir, parent=cwd)
        cwd.add(dir)
        return dir


def traverse_tree(node):
    r = [node]
    for child in node.children:
        r.extend(traverse_tree(child))
    return r


def build_tree(txt):
    cwd = Directory('/')

    for line in txt.splitlines():
        if line[0] == '$':
            # command
            if line[2:4] == 'cd':
                cwd = change_dir(line, cwd)
            elif line[2:4] == 'ls':
                pass  # No need to act on this, we're only interested in the output of the command
        elif line[0:3] == 'dir':
            pass  # We can ignore these items since we're only interested in the directories we cd into
        else:
            size, file = line.split(' ')
            cwd.add(File(file, int(size), cwd))

    return cwd.root()


def puzzle1(input):
    tree = build_tree(input)
    return sum(node.size() for node in traverse_tree(tree) if type(node) == Directory and node.size() <= 100000)


assert puzzle1(test_input) == 95437, "he sum of their total sizes is 95437 (94853 + 584)"

with open('input.txt') as f:
    print(puzzle1(f.read()))


def puzzle2(input):
    total_space = 70000000
    required_space = 30000000

    tree = build_tree(input)
    used_space = tree.size()
    to_clean = required_space - (total_space - used_space)
    return min(node.size() for node in traverse_tree(tree) if type(node) == Directory and node.size() >= to_clean)


assert puzzle2(test_input) == 24933642, "Between these, choose the smallest: d, increasing unused space by 24933642."

with open('input.txt') as f:
    print(puzzle2(f.read()))
