import requests

api = "http://127.0.0.1:5000"

while(1):
    print("1. Ping")
    print("2. Login")
    print("3. Echo")
    command = input("Enter command: ").strip()

    if(command == "1"):
        print(requests.get(api + '/ping').content)    
    if(command == "2"):
        login = input("Enter login:")
        password = input("Enter password:")
        print(requests.get(api + '/login/' + login + "/" + password).content)  
    if(command == "3"):
        text = input("Enter text:")
        print(requests.get(api + '/echo/' + text).content)  