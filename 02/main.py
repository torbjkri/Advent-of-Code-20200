
def choice_point(choice):
    if (choice == 'X'):
        return 1
    if (choice == 'Y'):
        return 2
    if (choice == 'Z'):
        return 3

    print("NOT VALID CHOICE")
    return 0

def translate(game):
    elf = ord(game[0]) - ord('A')
    me = ord(game[1]) - ord('X')
    res = [elf, me]
    return res


def play_points(game):
    game = translate(game)
    if (game[0] ==  game[1]):
        return 3

    if (game[0] == 0 and game[1] == 2):
        return 0
    if (game[0] == 2 and game[1] == 0):
        return 6

    if (game[1] > game[0]):
        return 6
    
    return 0

def play_points_2(game):
    game = translate(game)

    if (game[1] == 0):
        if (game[0] == 0):
            return 3
        return game[0]
    if (game[1] == 1):
        return game[0] + 1 + 3

    if (game[0] == 2):
        return 6 + 1

    return game[0] + 2 +6


    

def main():
    f = open("02/data.txt", 'r').read().split('\n')

    total = 0
    total2 = 0
    for line in f:
        l = line.split(' ')
        total += choice_point(l[1])
        total += play_points(l)

        total2 += play_points_2(l)


    print(total)
    print(total2)

if __name__ == "__main__":
    main()
