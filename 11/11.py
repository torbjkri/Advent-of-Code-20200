from functools import reduce

def extract_items(data):
    data = data.split(':')
    data = data[1].split(',')
    items = [int(x.strip()) for x in data]
    return items

class Monkey:

    def __init__(self, description):
        self.items = extract_items(description[1])
        self.operation = description[2].split('=')[1]
        print(description[4])
        self.targets = []
        self.targets.append(int(description[5].split(' ')[-1][:]))
        self.targets.append(int(description[4].split(' ')[-1][:]))
        self.divisor = int(description[3].split(' ')[-1])
        self.thrown = 0

    def evaluate(self,old):
        return eval(self.operation)

    def devaluate(self, item):
        return int(item/3)

    def devaluate2(self, item):
        return item

    def find_target(self, item):
        if item % self.divisor == 0:
            return self.targets[1]
        else:
            return self.targets[0]

    def process(self, monkeys, max_val):
        for item in self.items:
            self.thrown += 1
            item = self.evaluate(item)
            item = self.devaluate2(item)
            item = item % max_val
            monkeys[self.find_target(item)].take_item(item)
        
        self.items = []


    def take_item(self, item):
        self.items.append(item)
    



def one():
    data = open("11/data", 'r').read().split('\n\n')

    monkeys = []
    for monkey in data:
        monkey = monkey.split('\n')
        monkeys.append(Monkey(monkey))

    max_val = reduce((lambda x, y: x *y), [l.divisor for l in monkeys])

    for _ in range(10000):
        for i in range(len(monkeys)):
            monkeys[i].process(monkeys, max_val)

    thrown = [ i.thrown for i in monkeys]
    thrown.sort()
    print('One')
    print(thrown[-1] * thrown[-2])


def main():
    one()

if __name__ == "__main__":
    main()
