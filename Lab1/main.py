from task1 import hello_world
from task2 import calculation
from task3 import even_list


def main():
    hello_world()

    print("Input 2 numbers:")
    print("Result: {}".format(calculation(input(), input(), input())))

    print(even_list([1, 2, 3, 4, 5, 6, 7, 5342, 654, 6453, 8768]))


if __name__ == "__main__":
    main()

