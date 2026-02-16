list1 = []

name = input("enter your word for password: ")
for i in range(0, len(name)-1,2):
    list1.append(name[i]+name[i+1])
list1.reverse()
password = "".join(x for x in list1)
print(f"your password for your word: {name} is {password}")