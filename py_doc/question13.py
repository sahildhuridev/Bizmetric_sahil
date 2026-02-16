
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
    else: print("enter yes or no")
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
        
        break
            

        
    except:
        print("you have entered wrong value")


amount = 8
hr_a = input("do user want hr analytic (Y/N): ")

fn_a = input("do user want financing  analytic (Y/N): ")

mr_a = input("do user want marketing analytic (Y/N): ")

hostel = input("do you want hostel services?: (Y/N): ")





# list01 = [1,3,5,6,8,9,3,4,5,6,7,8,899,5,565,34,65,75,45,34,34]
# list02 = [['sahil', 'sadanand' , 'dhuri'], list01 ]

# print(list02)

# list02.remove(list01)


# a = ['sahil', 'abc', 'om']
# print(a)
# a.reverse()
# print(a)


# # creating a power list :
# powerlist = []
# for x in range(2,6):
#     print(x)
#     powerlist.append(2**x)
#     print(x, "--->",powerlist)
# powerlist

# powerlist_2 = [ 2**x for x in range(2,6)]
# powerlist_2


# # seperate elements from the list based on their data types

# list1 = [1,2,'a',3,4,'b','3','100',[1,2,3]]
# int_list = []
# str_list = []
# list_list = []
# for element in list1:
#     if type(element) == int: int_list.append(element)
#     if type(element) == str: str_list.append(element)
#     if type(element) == list: list_list.append(element)
# print(int_list , str_list , list_list)
    

# # list comprehension for the same code as above
# [[x for x in list1 if isinstance(x, t)] for t in (int, str, list) ]
# # list comprehension for even and odd
# ['even' if i%2==0 else 'odd' for i in range(10)]



# a = enumerate(list1)
# print(list(a))

# name = input("enter your full name: ")
# b_year = input("enter your birth date:(DD-MM-YYYY) ")
# print("enter password: (new password is your name + your birth year) ")
# password = 


# # generate the password on given logic: take last two letter 
# '''
# Data Science
# ceenci StaDa
# '''

# #range(starting_point , ending_point+1, step)

# a = input('enter your subject:')

# name = 'data science'
# for i in range(len(name)-1,2):
#     print(name[i]+name[i+1])



# val ='DATA'
# new_var = "-".join(val)
# print(new_var)

# for letter in 'hello world how are you':
#     if letter == 'h':
#         letter = 'w'
#     print(letter , end="")
#     count += 1

# name = 'chatarge'
# print(len(name)+1)
# for i in range(len(name)):
#     print(name[:i])
