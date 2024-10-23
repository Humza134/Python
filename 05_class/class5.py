
# data_base : list[tuple[str,str]] = [("Hamza", '123'),
#                                      ("Azan", '456'),
#                                      ("Hamid", '789')]

# for row in data_base:
#     print(row)


data_base : list[tuple[str,str]] = [("Hamza", '123'),
                                     ("Azan", '456'),
                                     ("Hamid", '789')]

input_user : str = input("Enter your name")
input_password : str = input("Enter your password")

for row in data_base:
    user,password = row
    if input_user == user and input_password == password:
     print("valid user")
    break

