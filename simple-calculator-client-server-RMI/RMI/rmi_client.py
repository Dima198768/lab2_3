import Pyro4

uri = input("Введіть Server Uri: ").strip()
remote_service = Pyro4.Proxy(uri)       

while(1):
    print("1. Ping")
    print("2. Login")
    print("3. Echo")
    command = input("Введіть команду: ").strip()


    if(command == "1"):
        print(remote_service.ping())    
    if(command == "2"):
        login = input("Введіть login:")
        password = input("Введіть password:")
        print(remote_service.login(login, password))
    if(command == "3"):
        text = input("Введіть текст:")
        print(remote_service.echo(text))