import random

def search_number():
    range_ = int(input("range: "))
    size = random.randint(range_)
    number = int(input("number: "))

    for i in range(size):
        print(i)
        if i == number:
            print(f" es correcto {number}")
            break

if __name__ == "__main__":
    search_number()
    


    