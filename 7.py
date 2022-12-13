from pprint import pprint

'''
- it's an n-ary tree
- build it out
- postorder traversal - need to visit the base most children first, then
  determine the size of the parent from that - recursively
'''

class Node:
    def __init__(self, name, size, parent, is_dir):
        self.parent = parent
        self.name = name
        self.size = size
        self.children = []
        self.is_dir = is_dir

class FileTree:
    def __init__(self):
        self.root = Node('/', 0, None, True)

    def preorder(self):
        def dfs(node):
            if node:
                res.append({'name': node.name, 'size': node.size, 'is_dir': node.is_dir})
                for child in node.children:
                    dfs(child)
        res = []
        dfs(self.root)
        return res

    def cd(self, curr, name):
        for node in curr.children:
            if node.name == name:
                return node

    def find_sizes(self):
        # post order dfs (children before parent)
        def dfs(node):
            if node:
                for child in node.children:
                    dfs(child)
                    node.size += child.size
        dfs(self.root)

with open ('input/7') as file:
    input = [line.rstrip().split(' ') for line in file]

files = FileTree()
curr = files.root
for i in range(1, len(input)):
    x = input[i]
    if x[0] == '$':
        if x[1] == 'cd':
            cd_name = x[2]
            if cd_name == '..':
                curr = curr.parent
            else:
                curr = files.cd(curr, cd_name)
        elif x[1] == 'ls':
            parent = curr
            i += 1
            # jump into list of dir contents
            while i < len(input) and input[i][0] != '$':
                x = input[i]
                name = x[1]
                size = x[0] if x[0] != 'dir' else 0
                is_dir = bool(x[0] == 'dir')
                new_node = Node(name, int(size), parent, is_dir)
                if curr:
                    curr.children.append(new_node)
                i += 1

files.find_sizes()
file_sizes = files.preorder()
dirs = {dir['name']: dir['size'] for dir in file_sizes if dir['is_dir']}

# part1
part1_dir_sizes = [file['size'] for file in file_sizes if file['is_dir'] and file['size'] <= 100_000]
print(sum(part1_dir_sizes))

# part2
amount = 30000000 - (70000000 - dirs['/'])
options = {name: size for name, size in dirs.items() if size >= amount}
print(min([dirs[dir] for dir in options]))

