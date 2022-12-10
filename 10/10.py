
def one():
    data = open("10/data.txt", 'r').read().split('\n')

    register = 1
    cycle = 0
    points = [20,60,100,140,180,220]
    signal_sum = 0

    for line in data:
        if line == 'noop':
            cycle += 1
            if cycle in points:
                signal_sum += cycle * register
        else:
            [_, val] = line.split(' ')
            val = int(val)
            cycle += 1
            if cycle in points:
                signal_sum += cycle * register
            cycle += 1
            if cycle in points:
                signal_sum += cycle * register
            register += val
    
    print(signal_sum)

def match(cycle, register):
    pos = cycle % 40
    if pos == register -1 or pos == register or pos == register+1:
        return True
    return False

def draw(drawn):
    image =[]
    for i in range(6):
        line = []
        for x in range(40):
            pos = i * 40 + x
            if pos in drawn:
                line.append('#')
            else:
                line.append('.')
        image.append(line[:])
    
    for line in image:
        print(''.join(line))

def two():
    data = open("10/data.txt", 'r').read().split('\n')

    register = 1
    cycle = 0
    drawn = []

    for line in data:
        print(register)
        if line == 'noop':
            if match(cycle, register):
                drawn.append(cycle)
            cycle += 1
        else:
            [_, val] = line.split(' ')
            val = int(val)
            if match(cycle, register):
                drawn.append(cycle)
            cycle += 1
            if match(cycle, register):
                drawn.append(cycle)
            cycle += 1
            register += val
    
    draw(drawn)




def main():
    #one()
    two()

if __name__ == "__main__":
    main()