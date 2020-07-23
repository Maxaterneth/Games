
def suma(num1 , num2):
    print(num1 +num2)

def welcome():
    print("""
    [+] suma
    [-] resta
    """)

if __name__ == "__main__":
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    suma(num1, num2)