'''
Docstring for days.day3
1. Dictionary operations:
    - Creating dictionary and adding key-value pairs
    - Updating dictionary values
    - Adding list inside dictionary
    - Appending elements to list inside dictionary
    - Nested dictionary access
    - Looping through dictionary using items()
    - Checking value types (int, float, dict)

    2. Sorting complex list:
        - Sorting list of dictionaries
        - Using lambda function as key
        - Using reverse=True

    3. Taking user input and storing into dictionary:
        - Creating structured dictionary with rollno, name, marks
        - Appending values dynamically
        - Using try-except for input validation

        4. Dynamic dictionary key creation:
            - Generating new key using len(dict)+1
            - Adding nested dictionary values

        5. Converting dictionary to pandas DataFrame:
            - Importing pandas
            - Creating DataFrame from dictionary

        6. Dynamic variable creation:
            - Using globals() to create variables dynamically
            - Storing variable names in list
            - Concept of global keyword

        7. While loop with continue:
            - Printing numbers in reverse
            - Skipping numbers divisible by both 3 and 5

        8. Iterators:
            - Using iter() function
            - Using next() to manually iterate
            - Converting iterator to list

        9. itertools module usage:
            - Importing count, islice, cycle, repeat, accumulate, chain
            - Using islice() to slice iterable
            - Basic understanding of infinite iterators
'''


sahil = {}
sahil["name"]='sahil dhuri'
sahil["mood"] = 'awesome'

print(sahil)

sahil["name"]+='rahul yadav'
sahil["mood"] += 'not awesome'


sahil["name"]+=["yadav","jadhav","pranav"]
sahil["mood"] += 4343

sahil["list_name"]=["rahul"]

sahil["list_name"].append("sahil")



# # s = set()
# # q = set([])
# # r = {}
# # print(s,q, r)
# # print([type(x) for x in [s ,q , r]])


# # heros ={
# #     'name': ['superman','duperman','batman','catman'],
# #     'occupation' : ['dance','singing','pothole']
# # }

# # print(heros['name'])


# # stock1 = {
# #     "tata" : 123.234,
# # "info": 200.12,
# # "nifty50" : {
# #     "adani":900,
# #     "bajaj" :23
# # },
# # "tcs":[1,2,3]
# # }

# # for i,j in stock1.items():
# #     if type(j) == int or type(j) == float:
# #         print(f'key: {i} and value : {j}')
# #     elif type(j) == dict:
# #         print(f'key: {i} and value : {j}')


# # my_list = [
# #     {'key': {'subkey':1}},
# #     {'key': {'subkey':10}},
# #     {'key': {'subkey':5}}
# #     ]
# # my_list.sort(key=lambda e: e['key']['subkey'],reverse=True)
# # print(my_list)

# # # (revise lambda function)

# # ask user to enter information and that has to go into dictonary
# # while True:
# #         try:
# #             rollno = int(input("enter roll no: "))
# #             name = input("enter name: ")
# #             marks = int(input("enter marks: "))
# #             dict_detail ={
# #                   'rollno':[],
# #                   'name':[],
# #                   'marks':[]
# #             }
# #             dict_detail['rollno'].append(rollno)
# #             dict_detail['name'].append(name)
# #             dict_detail['marks'].append(marks)
            
# #             print(dict_detail)
# #         except:
# #               print("error in input")


# # dict_2 = {1:{'name':'sahil sadanand dhuri','rollno':'8979898989'}}
# # new_key = len(dict_2)+1

# # name = input("enter name: ")
# # phoneno = int(input("enter phone no : "))
# # dict_2[new_key] = {
# #     'name' : name,
# #     'phoneno' : phoneno
# # }
# # print(dict_2)



# # d1 = {

# #     "class": [12,12,12,12],           
# #     "rollno": [1,2,3,4],
# #     "name": ["A","B","C","D"],
# #     "physics": [90,50,79,23],
# #     "biology": [23,23,23,45]          
# # }

# # import pandas as pd

# # print(pd.DataFrame(d1))




# # l1= []
# # for i in range(10):
# #     var = 'a_'+str(i)
# #     globals()[var]=i*100
# #     l1.append(var)
# # # we have degined variable in local but we can access it in global
# # print(var)

# # # global keyword : runtime dynamic varriable (search for it)






# # a,b = 0,20
# # while a<b:
# #     b = b-1
# #     if b%5==0 and b%3==0:
# #         continue
# #     print(b,end='\t')



# # iter() function:

# # while loop and for loop are block function and if i want to use outside the box we have to use generator and iter()
# # l1 = [1,2,4,45,23,213]
# # iter_l1 = iter(l1)

# # print(type(iter_l1))

# # print(list(iter_l1))

# # print(next(iter_l1))

# # print(next(iter_l1))

# # print(next(iter_l1))

# # print(next(iter_l1))


# # itertools package:
# from itertools import count , islice , cycle , repeat , accumulate , chain
# import operator
# #count(start = 5 , step = 3) # syntax ( where to end is not mentioned in the function) we use break keyword to come out of the function

# # abc = count(100,5)
# # help(type(abc))

# help function:
l2 = [3,5,6,7,5,3,5,6,6,4,5,6,4,34,3434,343]
iobj = islice(l2,3,8)
print(list(iobj))