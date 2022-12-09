def left(pos):
    pos[0] -= 1
    return pos

def right(pos):
    pos[0] += 1
    return pos

def up(pos):
    pos[1] += 1
    return pos

def down(pos):
    pos[1] -= 1
    return pos

def follow(head, tail):
    if abs(head[0] - tail[0]) == 1 and abs(head[1]- tail[1]) == 1:
        return tail

    if abs(head[0]-tail[0]) + abs(head[1] - tail[1]) > 1:
        x = head[0] -  tail[0]
        if x > 1:
            x = 1
        if x < -1:
            x = -1

        y = head[1] - tail[1]
        if y > 1:
            y = 1
        if y < -1:
            y = -1

        tail[0] += x
        tail[1] += y
    return tail

def one():
    data = open("09/data.txt", 'r').read().split('\n')
    data = [x.split(' ') for x in data]
    head = [0,0]
    tail = [0,0]
    visited = [tail[:]]

    for line in data:
        move = left
        if line[0] == 'D':
            move = down
        if line[0] == 'U':
            move = up
        if line[0] == 'R':
            move = right
        if line[0] == 'L':
            move = left
        for i in range(int(line[1])):
            head = move(head)
            tail = follow(head, tail)
            visited.append(tail[:])

    res = []
    [res.append(x) for x in visited if x not in res]
    print(len(res))

def two():
    data = open("09/data.txt", 'r').read().split('\n')
    data = [x.split(' ') for x in data]
    head = [0,0]
    tails = [[0,0] for _ in range(9)]

    visited = []

    for line in data:
        move = left
        if line[0] == 'D':
            move = down
        if line[0] == 'U':
            move = up
        if line[0] == 'R':
            move = right
        if line[0] == 'L':
            move = left

        for i in range(int(line[1])):
            head = move(head[:])
            tails[0] = follow(head[:], tails[0][:])
            for k in range(1, 9):
                tails[k] = follow(tails[k-1][:], tails[k][:])
            
            visited.append(tails[8][:])


    res = []
    [res.append(x) for x in visited if x not in res]
    print(len(res))


def main():
    one()
    two()

if __name__ == "__main__":
    main()