
def is_overlap(pair):
    elf1 = pair[0]
    elf2 = pair[1]

    if elf1[0] <= elf2[0] and elf1[1]>=elf2[1]:
        return 1
    if elf2[0] <= elf1[0] and elf2[1]>=elf1[1]:
        return 1

    return 0

def is_overlap2(pair):
    elf1 = pair[0]
    elf2 = pair[1]

    if elf1[0] <= elf2[1] and elf1[1]>=elf2[0]:
        return 1
    if elf2[0] <= elf1[1] and elf2[1]>=elf1[0]:
        return 1

    return 0

def one():
    data = open("04/data.txt", 'r').read().split('\n')
    data = [ map(lambda x: x.split('-'), x.split(',')) for x in data]
    data = [ [[int(y) for y in x] for x in line] for line in data]

    total = 0
    for line in data:
        total += is_overlap(line)

    print(total)

def two():
    data = open("04/data.txt", 'r').read().split('\n')
    data = [x.split(',') for x in data]
    data = [ [x.split('-') for x in line]  for line in data]
    data = [ [[int(y) for y in x] for x in line] for line in data]

    total = 0
    for line in data:
        total += is_overlap2(line)

    print(total)

def main():
    one()
    two()





if __name__ == "__main__":
    main()