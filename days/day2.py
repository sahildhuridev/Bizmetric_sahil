'''
Docstring for days.day2
1. String formatting using .format()
2. Formatting floating numbers with precision (e.g., {:.2f}, {:.3f})
3. String alignment formatting:
    - Left alignment {:20}
    - Right alignment {:>20}
    - Center alignment {:^20}

    4. Set data type usage:
        - Creating a set
        - add() method (adds single element)
        - update() method (adds iterable elements like list, tuple, dict)
        - intersection()
        - difference()
        - symmetric_difference()

        5. Book cost calculation system:
            - Takes student standard (class 1–10)
            - Takes book selection input (Hindi, Marathi, English, Science, Maths)
            - Calculates book price based on:
                - Selected subjects
                - Standard range (1–4, 5–8, 9–10)
                - Uses nested if-elif conditions
                - Uses logical operators (or)
                - Uses try-except for error handling
                - Displays total book amount
'''


# a =10
# b = 32.34434
# name = "world peace university"
# #print("{2:.7s} a, b {1:.2f}b & {0:10.3f}".format(a,b,name))

# # alignment of the string : (by default is the left alignment)
# print("'{:20}'".format('sahil'))

# # right alignment
# print("'{:>20}'".format('sahil'))

# # centre alignment
# print("'{:^20}'".format('sahil'))

# set 

# sahil = set()
# print(type(sahil))
# print(sahil)
# qwerty = [1,2,3,4,5,6,7,8,9,10]
# sahil.add("awesome")
# sahil.update(qwerty)
# print(sahil)

# we use add when we have to add single element
# we use update when we have to add a iterable object (list , tuple , dict)

a = {12,324,4,34,'sahil',(23,23,23)}
b = {1,2,4,3}

print(a.intersection(b))
print(a.difference(b)) # difference 
print(a.symmetric_difference(b)) # symetric difference



# question no. 14
while True:
    try:
        bookamount = 0

        standard = int(input("enter standard (only number): "))
        if standard > 10 or standard < 1:
            print('invalid standard')
        hindi = input("do you want hindi book? (Y/N) ")
        marathi = input("do you want marathi book? (Y/N) ")
        english = input("do you want english book? (Y/N) ")
        science = input("do you want science book? (Y/N) ")
        maths = input("do you want maths book? (Y/N) ")


        if maths == 'Y':
            if standard >= 9 and standard <= 10:
                bookamount += 250
            elif standard >= 5 and standard <= 8:
                bookamount += 140
            elif standard >= 1 and standard <= 4:
                bookamount += 100
            else:
                print("invalid standard")
        if science == 'Y':
            if standard >= 9 and standard <= 10:
                bookamount += 200
            elif standard >= 5 and standard <= 8:
                bookamount += 120
            elif standard >= 1 and standard <= 4:
                bookamount += 90
            else:
                print("invalid standard")
        if english == 'Y':
            if standard >= 9 and standard <= 10:
                bookamount += 150
            elif standard >= 5 and standard <= 8:
                bookamount += 100
            elif standard >= 1 and standard <= 4:
                bookamount += 80
            else:
                print("invalid standard")
        if marathi == 'Y' or hindi == 'Y':
            if standard >= 9 and standard <= 10:
                bookamount += 150
            elif standard >= 5 and standard <= 8:
                bookamount += 100
            elif standard >= 1 and standard <= 4:
                bookamount += 60
            else:
                print("invalid standard")
        print(f"your total cost is {bookamount}")
        break
    except:
        print("error in input! try again!")