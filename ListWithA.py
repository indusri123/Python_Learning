names_list = []
for i in range(0,5) :
    name = input("Enter a name : ")
    names_list.append(name)

print(names_list)  
for item in names_list :
    if item.lower().startswith("a") :
          print(item)