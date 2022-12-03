def find_same(rucks):
    return [c for c in rucks[0] if c in rucks[1]][0]

def priority(same):
    if same.isupper():
        return ord(same) - ord('A') + 27
    else:
        return ord(same) - ord('a') + 1


def one():
    data = open("03/data.txt", 'r').read().split('\n')

    data = [[x[:len(x)//2], x[len(x)//2:]] for x in data]
    total = sum([priority(find_same(x)) for x in data])

    print(total)

def find_badge(lists):
    return [c for c in lists[0] if c in lists[1] and c in lists[2]][0]

def two():
    data = open("03/data.txt", 'r').read().split('\n')
    data = [ data[n:n+3] for n in range(0, len(data), 3)]
    total = sum([priority(find_badge(x)) for x in data])

    print(total)


def main():
    one()
    two()


if __name__ == "__main__":
    main()


