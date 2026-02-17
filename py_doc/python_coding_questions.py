# comprehensive list:
# 1: ( squares in range 1 to 10)
print([x*x for x in range (1,11)])
# 2:
print([x for x in range(1,51) if x%2 == 0])
# 3:
list1 = ['sahil','sadanand','dhuri']
print([ x.upper() for x in list1])
# 4:
list2 = [-1,-2,-3,-4,-5,1,2,3,4,5]
print([x for x in list2 if x >= 0])
# 5: list of tuple (num , num*2) for 1 to 5
print([(x,x**2) for x in range(1,6)])
# 6: 
str1 = 'aslkdnadqoiwheqweruyoipqzrgnlekgnel'
print([x for x in str1 if x in ['a','e','i','o','u']])
# 7.
list3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print([num for row in list3 for num in row ])
# 8.
str2 = 'ergergergergegaqwezou'
print([x for x in str2 if x in ['a','e','i','o','u'] ])# 9.
str3 = ['egbe','rgegre','saguk','sahil','erergrgeger']
print([len(x) for x in str3])
# 10
str4 =['ahofe','wegw','Aoibneie','ojefoe']
print([x for x in str4 if x[0]== 'a' or x[0]=='A'])
# 11
listint1 = [1,2,3,4,5,6,7,8,9,10]
print(["even" if x % 2 == 0 else "odd" for x in listint1])
# 12
print([x for x in range(1,101) if x % 15 == 0])
# 13
print([[f'{i} x {j} = {i*j}' for j in range(1,11)] for i in range(1,6)])
# 14 convert dict key into list using comphrenesion
dict1 = {1 : 'a', 2 : 'sahil', 3 : 'sadanand', 4: 'dhuri'}
print([x for x in dict1.keys()])
# 15 extract numerical from string
str5 = '1qw23e3ed4455fssdv3434'
print([x for x in str5 if x.isdigit() == True])

# 16 remove all space from string

str6 = 'sahil sadanand dhuri'
a =[x for x in str6 if x.isalpha() == True]
print("".join(a))

# 17
str6 = 'sahil sadanand dhuri'
set_str6 = set()
unique = set()
for x in str6 :
    if x in set_str6:
        unique.add(x)
    else: 
        set_str6.add(x)
print(list(unique))

# 18
str6 = 'sahil sadanand dhuri'
print([x for x in str6.split(" ")])

#  19. same as 17

# 20. generate all pairs from list a and list b
list_a = [1,2,3,4,5]
list_b = ['a','b','c','d','e']
print([(x,y) for x in list_a for y in list_b])


# LAMBDA FUNCTIONS:
# 1
funct1 = lambda a, b: a + b
print(funct1(5, 3))

# 2
funct2 = lambda x : x % 2 == 0
print(funct2(4))

# 3
funct3 = lambda s: s[-1]
print(funct3("Sahil"))

#4
nums = [1,2,3,4]
funct4 = list(map(lambda x: x**2, nums))
print(funct4)

#5
nums = [1,2,3,4,5]
funct5 = list(filter(lambda x: x % 2 != 0, nums))
print(funct5)

#6

#7
funct6 = lambda s: s == s[::-1]
print(funct6("sds"))

#8
funct8 = lambda a,b,c: max(a,b,c)
print(funct8(10, 25, 15))

#9
funct9 = lambda s: s[::-1]
print(funct9("sahil dhuri"))

#10
nums = ["1","2","3"]
funct10 = list(map(lambda x: int(x), nums))
print(funct10)

#11
str_1 = ["sahil","","sadanand","","dhuri"]
funct11 = list(filter(lambda x: x != "", str_1))
print(funct11)

#12


#13
funct13 = lambda a,b: a if a>b else b
print(funct13(10, 20))

#14
funct14 = lambda x: x % 5 == 0
print(funct14(25))

#15
nums = [1,2,3]
funct15 = list(map(lambda x: x+10, nums))
print(funct15)

#16
dict_2 = [
    {"name":"A","age":25},
    {"name":"B","age":20}
]

funct16 = sorted(dict_2, key=lambda x: x["age"])
print(funct16)

#17
funct17 = lambda ch: ch.lower() in "aeiou"
print(funct17("A"))

#18
str4 = ["sahil","sadanand","developer","dhuri"]
funct18 = list(filter(lambda x: len(x) > 5, str4))
print(funct18)

# 19

# 20
nums = [1,2,2,3,3,4]
seen = set()
funct20 = list(filter(lambda x: x not in seen and not seen.add(x), nums))
print(funct20)












