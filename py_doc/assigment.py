
# 1
name = '''
Hi How are you?
Starterd learning python.
It's really interesting.
'''
name[:]
name[-10:-5]
name[3:12]
name[5:6]
name[-4:-12]
name[::2]
name[::-2]

l1 = ['a','b',20,30,'t',100,300,400,'happy','major']
l1[:]
l1[::3]
l1[::-2]

# based on index
l1[8]
# based on negative index
l1[-2]

# checking type of data on 4th position
type(l1[3])

l1[5:8]

# question 03
l2 = [1,2,3,5,['a','b','work hard'],100,200,'success']
l2[4]
l2[1:5]
l2[7]
l2[7][2]
l2[7][2:]
l2[:3]
l2[3:]


# question 04
# changing b to BEE
l2[4][1] = 'BEE'
l2[4][1]

# Question 05: discard BEE from l2
l2.remove("BEE")
print(l2)

#  question 06:
l2.append({'insect':['bee','moth'],'bird':['parrot','sparrow']})
l2

# question 07: (extract insect information)
l2[8]['insect']

# question 08:
d1 = {'a' : 10 ,'b' : 20 , 'c' : 30}
l2.append(d1)
print(l2)

# question 09:
l2[9]['a']

# question 10:
l2 = [1,2,3,5,(90,40,50,10),"python",400, ['a','b','work','hard'],100,200,"success",(200,300,"hundreds")]

l2[4][2]
l2[5][:]
l2[2] [:]
l2[1:5]
l2[5]
l2[5][3:-1]
l2[-1]
l2[-4:-3]
l2[-4: -10]
l2[7][2]
l2[-7][2:]
l2[ :- 3]
l2[-3:]

# question 11
while True:
    try:
        student_marks = float(input("enter your percentage / marks out of 100 "))
        if student_marks > 100 :
            print("number out of bonds")
        elif student_marks >= 80 :
            print("distinction")
        elif student_marks >= 70 :
            print("first class")
        elif student_marks >= 50 :
            print("second class")
        elif student_marks > 35 :
            print("pass")
        elif student_marks <= 35 and student_marks >= 0: 
            print("fail")
        else:
            print("enter proper marks")
            break
    except:
        print("the marks you entered was wrong data ")



# question 12 to 14 in day1.py and day2.py





# 16 (DOUBT)
string_01 = "In most organized forms of writing, such as essays, paragraphs contain a topic sentence. This topic sentence of the paragraph tells the reader what the paragraph will be about. Essays usually have multiple paragraphs that make claims to support a thesis statement, which is the central idea of the essay.     "

# TYPE CASTING

#  17
a = 100
# convert a to string
str(a)
# convert to a list
list(a) # error : int not iterable
# convert a to dict
dict(a) # error : int not iterable
# convert a to set
set(a) # error : int not iterable
# convert a to float
float(a)

marks = [20,18,15,17,18]
# convert to int
int(marks) # must be string or int
# convert to float
float(marks) # must be string or int
# convert list
list(marks)
# convert tuple
tuple(marks)
# convert dict
dict(marks) # error: requires key value pair
# covert set
set(marks)

# 10
sname = []
sname.append(20)
sname.extend(30)
sname.append(20,20,30)
sname.extend("WORK")
combo = [1,'a','b',2,3]
combo += sname
sname.append(combo)
sname.extend(combo)

# 11
l1 = [1,2]
l2 = [1,2,3,4,5,6,7]
l2.append(4)

# 12
list_01 = [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ]
for x in list_01 : 
    if type(x) == int or type(x) == float:
        x*5

# list_01.remove("Nisha")
for i , j in enumerate(list_01):
    if j == 20.50:
        print(i)


# 14
a = [x for x in range(201) if x % 13 == 0]           
print(a)

# 15
b = [x for x in range(300,401) if x % 4 == 0]
print(b)

#  16
x = int(input("enter x: "))
y = int(input("enter y: "))
listx = [i for i in range(x)]
listy = [j for j in range(y)]
print(listx)
print(listy)

listxy = list(zip(listx,listy))
print(listxy)

# 17 difference between add and update method in set:
'''
add - adds single element , update - adds multiple elements
'''
# 18
'''
append - adds single element
extend - adds multiple elements from an iterable object
'''

# 19 and 20:
'''
discard - removes specific value without error if not found
remove - same as above but gives error if value not found
pop - removes value (random if not specificed) also returns the value
'''

# 21
empty_set = set()
type(empty_set)

# 22
s1 = {"red", "green", "orange",1,2,3}
s2 = {1,2,3,4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))

l2 = {1,2,3,4,5,6}
print(s1.union(l2))
print(s1.intersection(l2))
print(s1.symmetric_difference(l2))
print(s1.difference(l2))


# 24
name = input("enter your name: ")
dob = input("enter your dob: (DD-MM-YYYY)")
print(f'your password is: {name[:4]}@{dob[:2]}{dob[3:5]}')

# 25
name = input("enter your name: ")
dob = input("enter your dob: (DD-MM-YYYY)")
print(f'your password is: {name[:4]}@{dob[6:]}')

# 26
for i in range(4):
    print('*'*i)

# 27
for i in reversed(range(4)):
    print('*'*i)

# 28
val = "ABCD"
for i in range(len(val)+1):
    print(val[:i])

# 29
for i in range(1,len(val)+1):
    print(val[i-1]*i)

#30
val_2 =[1,2,3,4]
for i in range(1,len(val_2)+1):
    print(str(val_2[i-1])*i)

#31 
val = "ABCD"
r_val = list(val)
r_val.reverse()
r_str_val = "".join(r_val)
for i in range(len(r_str_val)+1):
    print(r_str_val[:i])

#32 
val_4 = 'UPGRAD'
r_list_val_4 = list(val_4)
r_list_val_4.reverse()
str_4 = "".join(r_list_val_4)
for i in range(len(str_4)+1):
    print(str_4[:i])

#33 odd number from 1 to 10
# using loop
list_1 = []
for i in range(10):
    if i % 2 != 0:
        list_1.append(i)
print(list_1)
# using list comprehension
a= [x for x in range(10) if x % 2 != 0]
print(a)

# 34
b = [x for x in range(200,251) if x % 2 == 0]
print(b)

#35 (DOUBT)
list2 = [2,70,'work','para',2.5,[1,2,3],(1,2),{1:'a',2:'b'},3,10,302.5]
print(list2)
list04 = []
for item in list2:
    if type(item) == int or type(item) == float : list04.append(item * 2 )
    elif type(item) == str : list04.append(f'{item}{item}')
    elif type(item) == list : list04.append(item * 2)
   #elif type(item) == dict : list04.append(item *2) 
    else: list04.append(item)
print(list04)


# 36 (same as above)

# 37
while True:
    try:
        marks = int(input("enter marks: "))
        if marks < 0 or marks > 100:
            print("invalid marks")

        break
    except:
        ("error in input")

# 38
while True:
    try:
        firstname = (input("enter your first name: " ))
        lastname = (input("enter your last name: " ))
        
        if firstname.isalpha() and lastname.isalpha():
            print("valid input")
        else:
            print("invalid input")
        
        break
    except:
        print("enter only alphabets")

# 39
while True:
    try:
        phoneno = int(input("enter phone number: (10 digit only)"))
        if len(phoneno) == 10:
            print("valid phone number.")
        else:
            print("invalid phone number.")
        break
    except:
        ("enter valid input")

# 40
name = "enter your name: "
dob = "enter your birth date: DD-MM-YYYY: "
def autogeneratepass(name,dob):
    return f'{name[:4]}{dob[:2]}{dob[3:5]}'
password = autogeneratepass(name,dob)

print(f'your password is: {password}')
cust_dict = {}
# 41
name = input("enter your name: ")
dob = input("enter your birth date: DD-MM-YYYY: ")
phoneno = input("enter your phone number: ")

try:
    cust_dict
except:
    cust_dict = {}

key = len(cust_dict)+1
cust_dict[key]={
'name':name,
'dob':dob,
'phoneno':phoneno
}
print(f'customer database : {cust_dict}')


# 42 (DOUBT)

# 43 (DOUBT)

# 44 (DOUBT)


# 45 (DOUBT)
dict1 = {'key':{'subkey':20},
         'k2':{'sub2':5},
         'k3':{'sub4':16},
         'k4':{'sub4':6}}

# 46 (DOOUBT)

# 47 (DOUBT)

# 48 
name = input("enter word to check if it is palindrome or not")
r_name = name[::-1]
if name == r_name :
    print('it is palindrome ')
else:
    print('it is not palindrome')


# 49
def fib_sahil(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_sahil(n-1) + fib_sahil(n-2)

fib_sahil(3)


# 50
def factorial(n):
    if n == 1:
        return 1
    return n *  factorial(n-1)
factorial(5)

#51
a = [1,2,3,4,500,6,7,8,9,10]

a.sort()
print(a[len(a)-1])

#52
a = [1,1,1,2,2,2,3,3,3,3,3,3,7,8,9,10,56,56,56,8]
a_dict = {}
for num in a:
    if num not in a_dict: a_dict[num] = 1
    else: a_dict[num] += 1
print(a_dict)


# 53
l1 = [1,2,3,4,5]
l2 = [3,2,8,7,9]
print(list(set(l1).intersection(set(l2))))


# to do problems:  (35 36)done 42 43 44 45 46 47



# additional questions:

# 1. create a function to calculate age till now



from datetime import datetime as dt

dob = input('enter your date of birth to calculate the age: ')
dob = dt.strptime(dob , '%YY-%mm-%d')





