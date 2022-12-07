
def is_different(vals):
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            if vals[i] == vals[j]:
                return False
    
    return True

def one():
    data = open("06/data.txt", 'r').read()
    data = list(data)

    for i in range(len(data)):
        if is_different(data[i:i+4]):
            print(i+4)
            break

    print("one done")

def two():
    data = open("06/data.txt", 'r').read()
    data = list(data)

    for i in range(len(data)):
        if is_different(data[i:i+14]):
            print(i+14)
            break

    print("one done")


def main():
    one()
    two()

if __name__ == "__main__":
    main()