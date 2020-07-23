import random

def search_list(num, size):
    size = int(input("size: "))
    num = int(input("num: "))

    for i in range(size):
        print(i)

if __name__ == "__main__":
    size = int(input("size: "))
    num = int(input("num: "))
    search_list(size, num)