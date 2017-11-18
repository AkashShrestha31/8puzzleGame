import heapq
import timeit

import itertools

initial_state = [1, 2, 5, 3, 4, 0, 6, 7, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
entry_finder={}
aStarFrontier=[]
path_finder={}
path_traced=[]
counter = itertools.count()  # unique sequence count

class Node:
    child_nodes = []
    current_child = []
    puzzle = None
    parent = None
    x = 0
    move = None
    depth = None

    def __init__(self, puzzle, moved, parent=None, move=None, depth=0):
        self.moved = moved
        self.puzzle = puzzle

    def move_to_left(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element % 3) > 0:
            temp = pc[element - 1]
            pc[element - 1] = pc[element]
            pc[element] = temp
            child = Node(pc, "Left")
            self.child_nodes.append(child)
            child.parent = state

    def move_to_right(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element % 3) < 2:
            temp = pc[element + 1]
            pc[element + 1] = pc[element]
            pc[element] = temp
            child = Node(pc, "Right")
            self.child_nodes.append(child)
            child.parent = state

    def move_to_up(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element - 3) >= 0:
            temp = pc[element - 3]
            pc[element - 3] = pc[element]
            pc[element] = temp
            child = Node(pc, "Up")
            self.child_nodes.append(child)
            child.parent = state

    def move_to_down(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element + 3) < 9:
            temp = pc[element + 3]
            pc[element + 3] = pc[element]
            pc[element] = temp
            child = Node(pc, "Down")
            self.child_nodes.append(child)
            child.parent = state

    def Expand_node(self):
        for index, node in enumerate(self.puzzle):
            if node is 0:
                self.x = index

        self.move_to_up(self.puzzle, self.x)
        self.move_to_down(self.puzzle, self.x)
        self.move_to_left(self.puzzle, self.x)
        self.move_to_right(self.puzzle, self.x)




def add_task(task, priority):
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(aStarFrontier, entry)

dict = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [1, 0], 4: [1, 1], 5: [1, 2], 6: [2, 0], 7: [2, 1], 8: [2, 2]}
def calculate_m_dist(node_state):
    # print("For state",node_state)
    manhattanDistanceSum = 0
    for i in node_state:
        if i != 0:
            targetX = i / 3  # expected    x - coordinate(row)
            targetY = i % 3  # expected    y - coordinate(col)
            coords = dict[node_state.index(i)]
            dx = coords[0] - targetX  # x - distance    to    expected    coordinate
            dy = coords[1] - targetY  # y - distance    to    expected    coordinate
            manhattanDistanceSum += abs(dx) + abs(dy)

    # print("This gives hurestic value", manhattanDistanceSum)
    return manhattanDistanceSum


def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while aStarFrontier:
        priority, count, task = heapq.heappop(aStarFrontier)
        del entry_finder[task]
        return task
    raise KeyError('pop from an empty priority queue')

class breadth_first_seach:
    path_tracing = []

    def breadth_first_search(self, root):
        depth = 0
        nodes_expanded = 0
        Frontire =[]  # openlist
        AstarExplored =[]  # bcloselist
        dist = calculate_m_dist(root.puzzle) +depth
        add_task(root, dist)
        Frontire.append(root)
        print(len(aStarFrontier))
        goal_found = False
        while not (len(aStarFrontier)==0) and not goal_found:
            depth=depth+1
            # print(AstarFrontire.size())
            current_node = pop_task()
            Frontire.remove(current_node)
            del current_node.child_nodes[:]
            AstarExplored.append(current_node)
            current_node.Expand_node()
            nodes_expanded = nodes_expanded + 1
            # print(nodes_expanded)
            length = len(current_node.child_nodes)
            for i in range(length):
                current_child = current_node.child_nodes[i]
                if current_child.puzzle == goal_state:
                    goal_found = True
                    print("Goal found")
                    print(depth)
                    path_traced.append(current_child.moved)
                    parent = current_child.parent
                    print(parent)
                    while parent!=initial_state:
                        parent=path_finder[tuple(parent)]
                        path_traced.append(parent.moved)
                        parent=parent.parent
                        print(parent)
                    return nodes_expanded,depth
                AstarFrontire_check = self.checkin_AstarFrontire(Frontire, current_child)
                AstarExplored_check = self.checkin_AstarFrontire(AstarExplored, current_child)
                if AstarFrontire_check == False and AstarExplored_check == False:
                    path_finder[tuple(current_child.puzzle)]=current_child
                    dist = calculate_m_dist(current_child.puzzle) +depth
                    add_task(current_child, dist)
                    Frontire.append(current_child)

    def checkin_AstarFrontire(self, list, child):
        contains = False
        for i in range(len(list)):
            if list[i].puzzle == child.puzzle:
                contains = True
        return contains


def Astar():

    root_node = Node(initial_state, None)
    uniform = breadth_first_seach()
    nodes_expanded,depth= uniform.breadth_first_search(root_node)
    return nodes_expanded,depth


start = timeit.default_timer()
nodes_expanded,depth = Astar()
stop = timeit.default_timer()
path_traced.reverse()
print("path_to_goal: ",path_traced)
print("cost_of_path: ")
print("nodes_expanded: ", nodes_expanded)
print("search_depth: ",depth)
print("max_search_depth:",depth)
print("running_time: ", stop - start)
print("max_ram_usage: ")


