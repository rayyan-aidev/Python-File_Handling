def number_triangle():
    rows = input("Enter number of rows to print: ")
    for i in range(1, rows+1):
        print(str(i) * i)


def reverse_number_triangle():
    rows = int(input("Enter number of rows to print: "))
    for i in range(1, rows+1):
        print(" " * (rows-i), end="")
        print(str(i) * i, end="")
        print("")


def number_ladder():
    rows = int(input("Enter number of rows to print: "))
    for i in range(1, rows + 1):
        for k in range(1, i + 1):
            print(k, end="")
        print()


def reverse_number_ladder():
    rows = int(input("Enter number of rows to print: "))
    for i in range(1, rows + 1):
        for j in range(rows-i, 0, -1):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        print()


def star_triangle():
    rows = input("Enter number of rows to print: ")
    for i in range(1, rows+1):
        print("*" * i)


def middle_star_triangle():
    rows = int(input("Enter number of rows to print: "))
    for i in range(1, rows+1):
        print(" " * (rows-i), end="")
        print("*" * (2*i-1), end="")
        print("")


def reverse_star_triangle():
    rows = int(input("Enter number of rows to print: "))
    for i in range(1, rows+1):
        print(" " * (rows-i), end="")
        print("*" * i, end="")
        print("")
