from pprint import pprint

'''
- find the dirs that have at most 100_000
- calculate the sum of their total sizes
- good candidate for a tree of some kind - depth count
- alternatively, init a dict for each new dir
- append the size of each listed file
- need to create the file structure
- cd .. needs to know which dir it will be in
- but there's no `cd ..` followed directly by a `$ ls` so that means i don't
  need to know infer the location of the files, ie i don't need to know the
  exact structure of the files

- encounter a cd <dir_name>
- init a dict with that cd
- not elegant to encounter all sums iteratively

- build the file tree, recursively do the counts using dfs
- can have many children...
'''

# class File:
#     def __init__(self, name, size):
#         self.parent = None
#         self.name = name
#         self.size = size

# class Dir:
#     def __init__(self, name):
#         self.parent = None
#         self.name = name
#         self.direct_files = {}
#         self.dirs = {}

# class FileTree:
#     def __init__(self):
#         self.head = Dir('/')

#     def add_dir(self, dir_name):
#         pass

#     def add_file(self):
#         pass


with open ('input/7_test') as file:
    x = [line.rstrip().split(' ') for line in file]

p = 0
c = 1
dirs = {}
while c < len(x):
    if x[p][0] == x[c][0] == '$' and x[p][1] == 'cd' and x[c][1] == 'ls':
        dir_name = x[p][-1]
        dirs[dir_name] = {'files': 0, 'dirs': {}}
        # jump into dir contents
        c += 1
        while x[c][0] != '$':
            if x[c][0] == 'dir':
                # add the dir names included
                dirs[dir_name]['dirs'][x[c][-1]] = 0
            else:
                # only going to be files and dirs
                file_size = int(x[c][0])
                dirs[dir_name]['files'] += file_size
            c += 1
            # short circuit
            if c >= len(x):
                break
    # reset
    p = c
    c += 1
pprint(dirs)

'''
- i have the file structure
- recursively search down each one...
'''

# pprint(dirs)
# # add the remaining dirs' sums
# # separate since can't find them in place (retroactive listing, etc)
# for d in dirs:
#     for od in dirs[d]['other_dirs']:
#         dirs[d]['other_dirs'][od] = dirs[od]['files']


# print('')
# pprint(dirs)
# # one more pass to get the nested ones
# for d in dirs:
#     for od in dirs[d]['other_dirs']:
#         # add to the dirs that have their own dirs
#         for nested_od in dirs[d]['other_dirs'][od]['other_dirs']:
#             # but this can't handle multiple layers?
#         # for nested_od in dirs[d]['other_dirs'][od]
#             # dirs[d]['other_dirs'][od] += 


