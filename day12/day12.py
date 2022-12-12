from datetime import datetime

test_input = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''

class Graph:
    def __init__(self, nodecount):
        self._nodecount = nodecount
        self._neighbours = [[] for _ in range(nodecount)]
        self._weights = [[0 for column in range(nodecount)]
                      for row in range(nodecount)]

    def get_node_count(self):
        return self._nodecount

    def add_edge(self, a, b, weight):
        self._neighbours[a].append(b)
        self._weights[a][b] = weight

    def get_adjacent_nodes(self, node):
        return self._neighbours[node]

    def get_weight(self,a,b):
        return self._weights[a][b]

def get_minimum_distance_not_in_path(graph, path, distances):
    min = 999999999
    min_index = None
    for n in range(graph.get_node_count()):
        if distances[n] < min and not path[n]:
            min = distances[n]
            min_index = n
    return min_index


def get_shortest_paths(graph, root):
    distances = [999999999] * graph.get_node_count()
    distances[root] = 0
    path = [False] * graph.get_node_count()\

    for n in range(graph.get_node_count()):
        '''
        Dijkstra's algorithm: 
        -Choose the node that is not in the path with minimum distance
        -Add the node to the path
        -Update the distance value of all nodes adjacent to that node (if needed) 
        '''
        next_up = get_minimum_distance_not_in_path(graph, path, distances)
        if next_up is None:
            return distances
        path[next_up] = True
        for node in graph.get_adjacent_nodes(next_up):
            weight = distances[next_up] + graph.get_weight(next_up, node)
            if weight < distances[node]:
                distances[node] = weight

    return distances

def input_to_graph(input, dir='up'):
    grid = []
    start = None
    end = None
    for y, line in enumerate(input.splitlines()):
        row = []
        for x, c in enumerate(line):
            if c == 'S':
                row.append(ord('a'))
                start = x,y
            elif c == 'E':
                row.append(ord('z'))
                end = x,y
            else:
                row.append(ord(c))
        grid.append(row)

    height = len(grid)
    width = len(grid[0])
    graph = Graph(width*height)

    start = start[0]+start[1]*width
    end = end[0]+end[1]*width

    for x in range(width):
        for y in range(height):
            current_height = grid[y][x]
            possible_moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            possible_moves = [(x, y) for x, y in possible_moves if 0 <= x < width and 0 <= y < height]
            for x_, y_ in possible_moves:
                if grid[y_][x_] <= (current_height + 1):
                    if dir == 'up':
                        graph.add_edge(x+y*width, x_+y_*width, 1)
                    else:
                        graph.add_edge(x_+y_*width, x+y*width, 1)
    return start, end, graph

def puzzle1(input):
    start, end, graph = input_to_graph(input)
    distances = get_shortest_paths(graph, start)
    return distances[end]

assert puzzle1(test_input) == 31, 'This path reaches the goal in 31 steps, the fewest possible'



def puzzle2(input):
    start, end, graph = input_to_graph(input, dir='down')
    distances = get_shortest_paths(graph, end)

    is_a = [c in ['a','S'] for line in input.splitlines() for c in line]
    options = [distances[n] for n in range(len(is_a)) if is_a[n]]
    return min(options)

assert puzzle2(test_input) == 29, 'This path reaches the goal in only 29 steps, the fewest possible'


with open('input.txt') as f:
    txt = f.read()
    print(f'Puzzle1: {puzzle1(txt)}')
    print(f'Puzzle2: {puzzle2(txt)}')