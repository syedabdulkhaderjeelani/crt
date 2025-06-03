def hourglass(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "X " * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "X " * i)

hourglass(5)

def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "X " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "X " * i)

diamond(5)

def butterfly(n):
    for i in range(1, n + 1):
        print("X " * i + "  " * (n - i) * 2 + "X " * i)
    for i in range(n, 0, -1):
        print("X " * i + "  " * (n - i) * 2 + "X " * i)

butterfly(5)



def pascal_triangle(n):
    
    for i in range(n):
        print(' ' * (n - i), end='')
        val = 1
        for j in range(i + 1):
            print(val, end=' ')
            val = val * (i - j) // (j + 1)
        print()

pascal_triangle(5)




def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

floyd_triangle(5)





def zero_one_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end=' ')
        print()

zero_one_triangle(5)
