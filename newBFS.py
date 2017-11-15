goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class Node:
    child_nodes = []
    current_node = []
    current_child = []
    puzzle = None
    parent = []
    x = 0

    move = None
    depth = None

    def __init__(self, puzzle, parent=None, move=None, depth=0):
        self.puzzle = puzzle

    def move_to_left(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element % 3) > 0:
            temp = pc[element - 1]
            pc[element - 1] = pc[element]
            pc[element] = temp
            child = Node(pc)
            self.child_nodes.append(child)
            child.parent = state
            print("The child parent is", child.parent)
            return state
        return None

    def move_to_right(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element % 3) < 2:
            temp = state[element + 1]
            state[element + 1] = state[element]
            state[element] = temp
            child = Node(pc)
            self.child_nodes.append(child)
            print("mess", self.child_nodes[0].puzzle)
            child.parent = state
            return state
        return None

    def move_to_up(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element - 3) >= 0:
            temp = state[element - 3]
            state[element - 3] = state[element]
            state[element] = temp
            child = Node(pc)
            self.child_nodes.append(child)
            child.parent = state
            return state
        return None

    def move_to_down(self, state, element):
        pc = []
        for data in state:
            pc.append(data)
        if (element + 3) < 9:
            temp = state[element + 3]
            state[element + 3] = state[element]
            state[element] = temp
            child = Node(pc)
            self.child_nodes.append(child)
            child.parent = state
            return state
        return None

    def Expand_node(self):
        # print("The puzzle is",self.puzzle)
        print("The value of x is ", self.x)
        for index, node in enumerate(self.puzzle):
            if node is 0:
                self.x = index

        self.move_to_right(self.puzzle, self.x)
        print("The puzzle before calling left", self.puzzle)
        self.move_to_left(self.puzzle, self.x)
        print("The puzzle after calling left", self.puzzle)
        self.move_to_up(self.puzzle, self.x)
        self.move_to_down(self.puzzle, self.x)

    def Issamepuzzle(self, puz):
        samepuzzle = True
        for i in range(len(puz)):
            if self.puzzle is not puz[i]:
                samepuzzle=False
        return  samepuzzle


class uniform_seach:
    def breadth_first_search(self, root):
        openlist = []
        closelist = []
        openlist.append(root)
        # print("The length of openlis is,", len(openlist))
        goal_found = False
        while len(openlist) > 0 and not goal_found:
            current_node = openlist[0]
            print("The current node is",current_node.puzzle)
            print("The current node child length is: ",len(current_node.child_nodes))
            closelist.append(current_node)
            openlist.pop(0)
            root.Expand_node()
            print("after this is called")
            length = len(current_node.child_nodes)
            print("the length is ",length)
            for i in range(length):
                print("This is called recently")
                current_child = current_node.child_nodes[i]
                if current_child.puzzle == goal_state:
                    goal_found = True
                    print("Goal found")
                print("The boolean check is ",self.contains(openlist, current_node))
                if (not self.contains(openlist, current_node) and not self.contains(closelist,current_child)):
                    print("this is not called")
                    openlist.append(current_child)
                #    print("The current child is ",current_child.puzzle)
                    openlist[0].Issamepuzzle(current_child)

    def contains(self, openlist, c):
        contains = False
        for i in range(len(openlist)):
            if openlist[i].Issamepuzzle(c.puzzle):
                contains = True
        return  contains


def dfs():
    initial_state = [6, 1, 2, 3, 4, 5, 7, 0, 8]
    root_node = Node(initial_state)
    uniform = uniform_seach()
    uniform.breadth_first_search(root_node)


dfs()
