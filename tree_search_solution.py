class Node:
    """node objects that can represent a tree"""
    def __init__(self, name, children):
        self.name = name
        self.children = children
    def __str__(self):
        return self.name

#instantiate graph nodes:
h = Node("h", [])
g = Node("g", [h])
d = Node("d", [])
e = Node("e", [])
f = Node("f", [])
c = Node("c", [g])
b = Node("b", [d, e, f])
a = Node("a", [b, c])

def depth_first_searcher(root, term):
    """depth-first serch through a tree of node objects"""
    visited = set()
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node not in visited:
            stack = stack + node.children[::-1]
            visited.add(node)
        if node.name == term:
            return node


print(depth_first_searcher(a,"h"))



from queue import Queue

def breadth_first_searcher(root, term):
    """breadth-first search through a tree of node objects"""
    visited = set()
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node not in visited:
            for el in node.children:
                q.put(el)
            visited.add(node)
        if node.name == term:
            return node


print(breadth_first_searcher(a, "c"))





