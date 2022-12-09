import numpy as np


def check_horizontal(visible, forest):
    size = visible.shape
    for y in range(size[1]):
        tallest = -1
        for x in range(size[0]):
            if forest[x,y] > tallest:
                visible[x,y] = 1
                tallest = forest[x,y]
            if forest[x,y] == 9:
                break

        tallest = -1
        for x in reversed(range(size[0])):
            if forest[x,y] > tallest:
                visible[x,y] = 1
                tallest = forest[x,y]
            if forest[x,y] == 9:
                break

    return visible

def check_vertical(visible, forest):
    size = visible.shape
    for x in range(size[0]):
        tallest = -1
        for y in range(size[1]):
            if forest[x,y] > tallest:
                visible[x,y] = 1
                tallest = forest[x,y]
            if forest[x,y] == 9:
                break

        tallest = -1
        for y in reversed(range(size[1])):
            if forest[x,y] > tallest:
                visible[x,y] = 1
                tallest = forest[x,y]
            if forest[x,y] == 9:
                break


    return visible

def calculate_score(forest, xx, yy):
    # left
    height = forest[xx,yy]
    left = 0
    for x in reversed(range(xx)):
        if forest[x, yy] < height:
            left += 1
        if forest[x, yy] >= height:
            left += 1
            break

    right = 0
    for x in range(xx+1, forest.shape[0]):
        if forest[x, yy] < height:
            right += 1
        if forest[x, yy] >= height:
            right += 1
            break

    down = 0
    for y in range(yy+1, forest.shape[1]):
        if forest[xx, y] < height:
            down += 1
        if forest[xx, y] >= height:
            down += 1
            break

    up = 0
    for y in reversed(range(yy)):
        if forest[xx, y] < height:
            up += 1
        if forest[xx, y] >= height:
            up += 1
            break

    return left * right * up * down
        

def get_best_score(visible, forest):
    best = 0   

    for x in range(visible.shape[0]):
        for y in range(visible.shape[1]):
            if visible[x,y] == 1:
                score = calculate_score(forest, x, y)
                best = max(best, score)
    return best


def one():
    data = open("08/data.txt", 'r').read().split('\n')
    data = [[int(x) for x in list(line)] for line in data]
    data = np.array(data)
    visible = np.zeros_like(data)
    visible = check_horizontal(visible, data)
    visible = check_vertical(visible, data)
    print("One")
    print(visible.sum().sum())

    print("Two")
    score = get_best_score(visible, data)
    print(score)


def main():
    one()

if __name__ == "__main__":
    main()