import timeit

goal_state = [0, 1, 2, 3, 4,5,6,7,8]


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


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)





class breadth_first_seach:
    path_tracing = []

    def breadth_first_search(self, root):
        nodes_expanded = 0
        dfsFrontire = Stack()  # openlist
        dfsExplored = []  # bcloselist
        dfsFrontire.push(root)
        # print(dfsFrontire.size())
        goal_found = False
        while not(dfsFrontire.isEmpty()) and not goal_found:
            # print(dfsFrontire.size())
            current_node = dfsFrontire.items[dfsFrontire.size()-1]
            print("This is current puzzle",current_node.puzzle)
            del current_node.child_nodes[:]
            dfsExplored.append(current_node)
            dfsFrontire.pop()
            current_node.Expand_node()
            current_node.child_nodes.reverse()
            # print("akash")
            nodes_expanded = nodes_expanded + 1
            # print(nodes_expanded)
            length = len(current_node.child_nodes)
            for i in range(length):
                current_child = current_node.child_nodes[i]

                print("This is expanded puzzle",current_child.puzzle)
                if current_child.puzzle == goal_state:
                    goal_found = True
                    print("Goal found")
                    # self.path_trace(current_child)
                    return nodes_expanded
                dfsFrontire_check = self.checkin_dfsFrontire(dfsFrontire.items, current_child)
                dfsExplored_check = self.checkin_dfsFrontire(dfsExplored, current_child)
                if dfsFrontire_check == False and dfsExplored_check == False:
                    dfsFrontire.push(current_child)

    def path_trace(self, current_child):

        self.path_tracing.append(current_child.moved)
        while current_child.parent is not None:
            current_child = current_child.parent
            print("parent is ", current_child.moved)

    def checkin_dfsFrontire(self, list, child):
        contains = False
        for i in range(len(list)):
            if list[i].puzzle == child.puzzle:
                contains = True
        return contains


def dfs():
    initial_state = [1,2,5,3,4,0,6,7,8]
    root_node = Node(initial_state, None)
    uniform = breadth_first_seach()
    nodes_expanded = uniform.breadth_first_search(root_node)
    return nodes_expanded


start = timeit.default_timer()
nodes_expanded = dfs()
stop = timeit.default_timer()
print("path_to_goal: ")
print("cost_of_path: ")
print("nodes_expanded: ", nodes_expanded)
print("search_depth: ")
print("max_search_depth:")
print("running_time: ", stop - start)
print("max_ram_usage: ")

