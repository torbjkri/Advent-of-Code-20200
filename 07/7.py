
idx = 1
g_total = 0
smallest = []
g_remainder = 0

class File:
    def __init__(self, data):
        self.ss = int(data[0])
        self.name = data[1]
    
    def size(self):
        return self.ss

class Folder:
    def __init__(self, data, ii, name):
        global idx
        self.name = name
        self.folders = {}
        self.files = []
        for ii in range(idx, len(data)):
            if idx == len(data):
                return
            line = data[idx]
            idx += 1
            line = line.split(' ')
            if line[0].isnumeric():
                self.files.append(File(line))
            if  line[0] == "dir":
                self.folders[line[1]] = None
            if line[1] == "ls":
                continue
            if line[1] == "cd":
                if line[2] == "..":
                    return
                self.folders[line[2]] = Folder(data, idx, line[2])
                ii = idx
    def size(self):
        total = 0
        for f in self.folders:
            total += self.folders[f].size()
        for f in self.files:
            total += f.size()
        return total
    
    def add_total(self):
        global g_total
        if self.size() <= 100000:
            g_total += self.size()

        for keys in self.folders:
            self.folders[keys].add_total()
    
    def traverse(self):
        global g_remainder
        global smallest
        if self.size() >= g_remainder:
            smallest.append(self.size())

        for key in self.folders:
            self.folders[key].traverse()




def one():
    data = open("07/data.txt", 'r').read().split('\n')
    global idx
    root = Folder(data, idx, '/')

    global g_total
    root.add_total()

    print("one")
    print(g_total)

    print("two")
    global g_remainder
    global smallest
    g_remainder = 70000000 - root.size()
    g_remainder = 30000000 - g_remainder
    root.traverse()
    kk = 1000000000000
    for v in smallest:
        if v < kk:
            kk = v

    print(kk)





def main():
    one()

if __name__ == "__main__":
    main()