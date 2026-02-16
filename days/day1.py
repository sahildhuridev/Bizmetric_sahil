'''
PYTHON FUNDAMENTALS!!!
1. User input handling using input()
2. String methods: isalnum(), isdecimal(), isdigit(), isalpha()
3. String manipulation: lower(), upper(), split(), slicing
4. Name validation (only alphabets allowed)
5. Mobile number validation (10 digits check)
6. Salary categorization using if-elif-else
7. Student marks classification (distinction, first class, etc.)
8. Use of while loop with try-except for input validation
9. List operations: append(), extend(), remove(), indexing, slicing
10. Nested list indexing and modification
11. Dictionary creation and nested dictionary access
12. Tuple indexing and slicing
13. Salary increment system using match-case and conditions
14. College fee calculation system using functions and user input
15. Logical operators (and, or, not)
16. Pattern matching (match-case)
17. Exception handling (ValueError)
18. String formatting using f-strings and .format()
19. Floating number formatting using {:.3f}
'''


name = input("enter your name: ")
# Sahil Dhuri
type(name)

marks = int(input("enter the value: ").isdecimal())
print(marks)

name.isalnum()
name.isdecimal()
name.isalpha()

print(name)
print(name.lower())
print(name.upper())
print(name.split(" "))


# activity : ask user to input name ( name should be all aplhabets )
# if not then write as wrong name

name = input("enter your name: ")
if name.isalpha():
    print('thankyou for entering')
else:
    print("enter only aplhabets")


# ask user to enter mobile number if he has 10 digit if more or less then mark wrong number

mobile = input("enter your mobile number: ")
if len(mobile) == 10 and mobile.isdigit():
    print("right number")
else:
    print("wrong number")
    

# ask user to enter the salary 
# if salary is less then 5k make grade as "low" 
# if salary is less then 10k make grade as "ok"
# if salary is less then 20k make grade as "mid"
# if salary is less then 30k make grade as "high"
# otherwise "very high"

while True:
    try:
        salary = int(input("enter salary: "))
        if salary >= 30000: print("very high")
        elif salary >= 20000: print("high")
        elif salary >= 10000: print("mid")
        elif salary >= 000: print("ok")
        else: print("low")
        break
    except:
        print("invalid number, please enter number")

# ask user to enter marks and make groups like distinction , first class , second class , pass , fail based on marks . 80 - distinction 70 => first class 50 second 35 > pass else fail

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
        elif student_marks <= 35 and student_marks >= 0
            print("fail")
        else:
            print("enter proper marks")
        break
    except:
        print("the marks you entered was wrong data ")


# other method

marks = input("enter the marks")
if (not marks.isalnum() and not marks.isalpha()) or marks.isdigit():
    marks = int(marks)

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
elif student_marks <= 35 and student_marks >= 0
    print("fail")
else:
    print("enter proper marks")

list_01 = ['sahil' , 'sadanand', 'rockon' , 'dhuri']

list_01.append(3)
list_01.extend('world')

print(list_01)



sahil_01 = ['shail','eam',23,23.23,3,14,["sahil", [12,343,121,232,'sahil']]]

sahil_01[6][1][5][2]

# if else 
# 14th
# 








# assigment no. 01

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
        elif student_marks <= 35 and student_marks >= 0
            print("fail")
        else:
            print("enter proper marks")
        break
    except:
        print("the marks you entered was wrong data ")


# question 12

while True:
    try:
        salary = float(input("Enter your salary amount (in LPA): "))
        rating = input("Enter your rating (A, B, C, D): ").upper()

        if rating not in ('A', 'B', 'C', 'D'):
            print("Invalid rating")
            continue

        if 15 < salary <= 23:
            match rating:
                case 'A': inc = 0.07
                case 'B': inc = 0.05
                case 'C': inc = 0.04
                case 'D': inc = 0.00

        elif 10 < salary <= 15:
            match rating:
                case 'A': inc = 0.08
                case 'B': inc = 0.06
                case 'C': inc = 0.04
                case 'D': inc = 0.00

        elif 5 < salary <= 10:
            match rating:
                case 'A': inc = 0.14
                case 'B': inc = 0.10
                case 'C': inc = 0.08
                case 'D': inc = 0.06

        elif 0 < salary <= 5:
            match rating:
                case 'A': inc = 0.16
                case 'B': inc = 0.12
                case 'C': inc = 0.10
                case 'D': inc = 0.06
        else:
            print("We do not have data for your salary")
            continue

        new_salary = salary + salary * inc
        print(f"Your salary increased from {salary} LPA to {new_salary:} LPA (Rating {rating})")
        break

    except ValueError:
        print("Please enter a valid numeric salary")


# question 13: l1 = ["HR","Finance","Marketing","DS"]

l1 = ["HR","Finance","Marketing","DS"]
# HR core and HR analytics 
# marketing core and analytics
# analytics is optional , added extra fees 
# DS do not have analytics

# core subject have 2 lac fee and analytic have 2 lac + 10 percent 
# for hostel : 2 lac 
# for food : 2000 * 12
# 13000 per semester for travel 

# calculate annual money

annual_amount = 0
HR_core =  2 
marketing_Core = 2
DS_Core = 2

annual_amount = HR_core + marketing_Core + DS_Core

def yes_or_no(sub_analytics,amount_y,amount_n):
    amount = 0
    if sub_analytics == 'Y':
        annual_amount += amount_y
        print(f"total amount after adding this service ({amount_y}) is: {annual_amount}")
    elif sub_analytics == 'N':
        annual_amount += amount_n
    else: print("yes or no")
    return 

while True:
    try:
        hr_analytic = input("do you want hr analytics? Y/N").upper()
        yes_or_no(hr_analytic,2.2,0) 

        marketing_analytic = input("do you want marketing analytics? Y/N ").upper()
        yes_or_no(marketing_analytic,2.2,0)

        finance_analytic = input("do you want marketing analytics? Y/N ").upper()
        yes_or_no(finance_analytic,2.2,0)

        hostel = input("do you want hostel:(Y/N) ")
        yes_or_no(hostel,2,0)

        trans_1 = input("do you want transportation for sem 1: (Y/N) ")
        yes_or_no(trans_1,0.13,0)

        trans_2 = input("do you want transportation for sem 2: (Y/N) ")
        yes_or_no(trans_2,0.13,0)

        food = input("do you want monthly food service? (Y/N): ").upper()
        if food == 'Y':
            while True:
                try:
                    month_food = int(input("how many months are you looking for: "))
                    break
                except:
                    print("print a number")
            annual_amount += month_food * 2000
            print(f"total expense after adding this food service for ({month_food}) month : {annual_amount}")
        elif food == 'N':
            print("food is not included now , apna khana khud banao! ")
        else:
            print("enter valid value: (Y/N)")
        print(f"Total expense for the year is {annual_amount}")
            

        
    except:
        print("you have entered wrong value")









# string format:
name = "sahil sadanand dhuri : \"Hey how are you?\" " # using backslash
name = 'sahil sadanand dhuri : "Hey how are you?" ' # using single qoute

a = "sahil"
b= "hero"
c = "villian"

name = f"{a} is a {b} who defeated {c}" # F string (mostly used like this)

name = f"{a} is a {b} who defeated {c}".format(a = "sahil", b= "hero", c = "villian")
name = f"{0} is a {1} who defeated {2}".format(0 = "sahil", 1= "hero", 2 = "villian")


a = 10.76
b = 220.2432432432
print("values a , b {:.3f} and {:.3f}".format(a,b))

print("sahil")