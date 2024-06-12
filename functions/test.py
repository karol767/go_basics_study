x = 13

def one():
    global x
    x += 1

def two(x):
    x += 3

def main():
    one()
    two(x)
    print(x)

if __name__ == '__main__':
    main()