from aoc_func import read_input_text

filesystem = read_input_text("input.txt")
print(filesystem)

directory_size = {}

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.contents = {}

    def __repr__(self):
        repr = f"dir {self.name}"
        return repr

    def add_file(self, filename, size):
        self.contents[filename] = size
        self.size += size
        directory_size[self.get_file_path()] = self.size
        self.add_size_to_parents(size)

    def add_size_to_parents(self, size):
        ref = self.parent
        if ref:
            ref.size += size
            directory_size[ref.get_file_path()] = ref.size
            ref.add_size_to_parents(size)

    def get_file_path(self):
        path = self.name
        ref = self.parent
        if ref:
            path = f"{self.parent.get_file_path()}/{path}"
        return path

    def return_parent(self):
        return self.parent

    def add_directory(self, name):
        self.contents[name] = Directory(name, self)


home = Directory("/", None)
pwd = home

for instruction in filesystem:
    if instruction.startswith("$"):
        if instruction == "$ ls":
            pass
        elif instruction.endswith("cd /"):
            pwd = home
        elif instruction.endswith("cd .."):
            pwd = pwd.return_parent()
        elif instruction.startswith("$ cd"):
            dir_name = instruction.split(" ")[-1]
            pwd = pwd.contents[dir_name]
    elif instruction.startswith("dir"):
        dir_name = instruction.split(" ")[-1]
        pwd.add_directory(dir_name)
    else:
        size, filename = instruction.split(" ")
        pwd.add_file(filename, int(size))

total = 0
space_needed = 30000000 - (70000000 - home.size)
deletion_candidate_size = []
for size in directory_size.values():
    if size <= 100000:
        total += size
    if size >= space_needed:
        deletion_candidate_size.append(size)

print(total)
print(directory_size)
print(min(deletion_candidate_size))
