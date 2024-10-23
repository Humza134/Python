name : tuple[str,int,float] = ("Pakisatn", 45, 0.4)
print(name) # print
print(type(name)) # type
print(id(name)) # physical adress
print([i for i in dir(name) if "__" not in i]) # methods and attributes

