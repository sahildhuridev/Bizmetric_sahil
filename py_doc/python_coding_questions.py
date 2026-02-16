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

