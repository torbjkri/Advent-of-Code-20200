import itertools

def main():
    f = open("data.txt", 'r').read()

    my_list = f.splitlines()
    splitted_list = [list(y) for x, y in itertools.groupby(my_list, lambda z: z =='') if not x]
    totals = [ sum([int(y) for y in x])  for x in splitted_list]
    totals.sort()
    print(totals[-1])
    print(sum(totals[-3::]))


if __name__ == "__main__":
    main()





