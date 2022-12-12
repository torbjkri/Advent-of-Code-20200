import math
import numpy as np

def get_lowest_distance(openset, distance):
    lowest = openset[0]
    for node in openset[1:]:
        if distance[node[0]][node[1]] < distance[lowest[0]][lowest[1]]:
            lowest = node

    return lowest

def get_neighbours(current, max_x, max_y):
    neighbours = [
        [current[0], current[1]-1],
        [current[0], current[1]+1],
        [current[0]+1, current[1]],
        [current[0]-1, current[1]]
    ]
    neighbours = [x for x in neighbours if x[0] >= 0 and x[1] >= 0 and x[0] < max_y and x[1] < max_x]
    return neighbours

def legal_move(current, neighbour, height):
    c = height[current[0]][current[1]]
    n = height[neighbour[0]][neighbour[1]]

    if n - c < 2:
        return True
    return False

def find_distance(start, ends, input):
    distance = [[math.inf for x in line] for line in input]
    distance[start[0]][start[1]] = 0

    max_y = len(input)
    max_x = len(input[0])

    openset = [start]
    count = 0
    while len(openset) != 0:
        count += 1
        current = get_lowest_distance(openset, distance)
        if current in ends:
            return distance[current[0]][current[1]]
        openset.remove(current)
        current_distance = distance[current[0]][current[1]]
        neighbours = get_neighbours(current, max_x, max_y)
        for n in neighbours:
            if legal_move(current, n, input):
                if distance[n[0]][n[1]] == math.inf:
                    distance[n[0]][n[1]] = current_distance + 1
                    openset.append(n)

    return 100000

def one():
    data = open("12/data", 'r').read().split('\n')
    data = [list(x) for x in data]

    input = []
    start = []
    end = []
    for j in range(len(data)):
        line = []
        for i in range(len(data[0])):
            if data[j][i] == 'S':
                start = [j,i]
                line.append(0)
            elif data[j][i] == 'E':
                end = [[j,i]]
                line.append(ord('z') - ord('a'))
            else:
                line.append(ord(data[j][i]) -  ord('a'))
        input.append(line)

    print("One")
    print(find_distance(start, end, input))


def two():
    data = open("12/data", 'r').read().split('\n')
    data = [list(x) for x in data]

    max_y = len(data)
    max_x = len(data[0])
    input = []
    start = []
    ends = []
    for j in range(len(data)):
        line = []
        for i in range(len(data[0])):
            if data[j][i] == 'S':
                line.append(ord('z') - ord('a'))
            elif data[j][i] == 'E':
                start = [j,i]
                line.append(0)
            elif(data[j][i]) == 'a':
                ends.append([j,i])
                line.append(ord('z') - ord('a'))
            else:
                line.append(ord('z') - ord(data[j][i]))
        input.append(line)

    shortest =  find_distance(start, ends, input)
    print("Two")
    print(shortest)


def main():
    one()
    two()

if __name__ == "__main__":
    main()