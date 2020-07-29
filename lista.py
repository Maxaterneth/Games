clients = ["Pedro", "Juan"]

def create_clients(new_clients):
    global clients

    if new_clients not in clients:
        clients.append = new_clients
        
    
    else:
        print("The client is ready")


def welcome():
    print("""
    Welcome of clients
    [C]reate clients
    [D]etele clients    
    
    """)

if __name__ == "__main__":
    welcome()

    comand = input("")
    
    if comand == "C":
        new_clients = input("name of client: ")
        create_clients(new_clients)
        print(clients)

        
    