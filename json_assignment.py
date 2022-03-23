import json
file_path = "assignment.json"

print("\nWelcome\n")
print("Enter the number of what you want to do:\n")
print("1. Register")
print("2. Log in")
print("3. Exit")

try:
    mode = int(input("\n"))
except:
    print("Invalid input.")
    quit()

if mode == 1:
    print("\nREGISTER")
    name = input("Enter name: ")
    password = input("Enter password: ")
    user = {
        "name": name,
        "password": password
    }

    with open(file_path,"r") as file:
        users = json.load(file)
        
        users.append(user)
        
        with open(file_path,"w") as file:
            json.dump(users, file)

    # with open(file_path, "a") as my_file:
    #     json.dump(user, my_file)
    
    print("\nWelcome, "+name)
    

elif mode == 2:
    print("\nLOG IN")
    name = input("Enter name: ")
    password = input("Enter password: ")
    
    with open(file_path, "r") as my_file:
        json_dict = json.load(my_file)
                 
    try:
        user_to_get = list(filter(lambda user: user["name"] == name and user["password"] == password, json_dict))[0] #to get the user that matches the details
        print(name+", welcome back.")
    except:
        print("You are either not registered or you inputted a wrong name or password.")

        


        # try:
        # for key,value in json_dict.keys(), json_dict.values():
        #     if name == key and password == value:
        #         print (name+", welcome back.")
        #         True
        #     else: False
        # if False:
        #     print("You are not registered.")
        
        # except:
        #       print("You are not registered.")

elif mode == 3:
    print("Goodbye.\n")
    quit()

else:
    print("\n Invalid Input\n")
    quit()



