# Let's attempt to learn A* pathfinding
import heapq


with open("input.txt") as file:
    grid = [list(x.strip()) for x in file.readlines()]

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]

def astar(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    adjacent_squares = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        if current_node == end_node:
            return return_path(current_node)

        children = []

        for new_position in adjacent_squares:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) \
                    or node_position[0] < 0 \
                    or node_position[1] > (len(maze[len(maze) - 1]) - 1) \
                    or node_position[1] < 0:
                continue

            current_height = maze[current_node.position[0]][current_node.position[1]]
            current_height = 'a' if current_height == 'S' else current_height
            node_height = maze[node_position[0]][node_position[1]]
            node_height = 'z' if node_height == 'E' else node_height
            if ord(node_height) > ord(current_height) + 1:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + \
                      ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue

            heapq.heappush(open_list, child)


start = end = None
for row_index, row in enumerate(grid):
    for col_index, col in enumerate(row):
        if col == 'S':
            start = (row_index, col_index)
        elif col == 'E':
            end = (row_index, col_index)

print(f"{start} --> {end}")
path = astar(grid, start, end)
print(path)
print(len(path) - 1)

for r, c in path:
    grid[r][c] = '.'

for row in grid:
    print(' '.join(row))