import random

def game():
    random_number = random.randint(1, 100)
    vidas = int(input("cuantas vidas quieres: "))
    input_number = int(input("number: "))


    while input_number != random_number:

        if input_number < random_number:
            print("Es mas grande")
            vidas -= 1
        else:
            print("Es mas pequeño")
            vidas -= 1

        if vidas == 0:
            print(f"perdiste el numero era {random_number}")
            break
        
        input_number = int(input("number: "))


    if input_number == random_number:
        print(f"ganaste el numero era {random_number}")

if __name__ == "__main__":
    game()