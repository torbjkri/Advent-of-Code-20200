def extract_stacks(stack_data, num_symbols):
    stacks = [[] for x in range(num_symbols)]
    for line in stack_data:
        line = list(line)
        line.append(' ')
        symbols = [line[n+1] for n in range(0, 4* num_symbols, 4)]
        for i in range(num_symbols):
            if symbols[i] != ' ':
                stacks[i].insert(0,symbols[i])

    return stacks

def extract_commands(command_data):
    commands = []

    for line in command_data:
        line = line.split(' ')
        commands.append([int(line[1]), int(line[3])-1, int(line[5])-1])

    return commands



def one():
    data = open("05/data.txt", 'r').read().split('\n')
    num_symbols = int((len(data[0]) + 1)/ 4)

    idx = 0
    for line in data:
        if line[1] == '1':
            break
        idx += 1

    stack_data = data[:idx]
    command_data = data[idx+2:]


    stacks = extract_stacks(stack_data, num_symbols)
    commands = extract_commands(command_data)


    for command in commands:
        for i in range(command[0]):
            item = stacks[command[1]].pop()
            stacks[command[2]].append(item)

    output = ''.join([x[-1] for x in stacks])
    print(output)

def two():
    data = open("05/data.txt", 'r').read().split('\n')
    num_symbols = int((len(data[0]) + 1)/ 4)

    idx = 0
    for line in data:
        if line[1] == '1':
            break
        idx += 1

    stack_data = data[:idx]
    command_data = data[idx+2:]


    stacks = extract_stacks(stack_data, num_symbols)
    commands = extract_commands(command_data)


    for command in commands:
        items = []
        for i in range(command[0]):
            item = stacks[command[1]].pop()
            items.append(item)

        items.reverse()
        for item in items:
            stacks[command[2]].append(item)

    print(stacks)
    output = ''.join([x[-1] for x in stacks])
    print(output)

def main():
    one()
    two()





if __name__ == "__main__":
    main()