def suma():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    return print(num1 + num2)
    
def welcome():
    print("""
    Calculadora:

    (+) suma
    (-) resta
    (/) dividir
    (*) multiplicar
    
    """)

if __name__ == "__main__":
    welcome()
    comand = input("")

    if comand == "+":
        suma()
        
    elif comand == "-":
        resta()

    elif comand == "/":
        dividir()

    elif comand == ""

        