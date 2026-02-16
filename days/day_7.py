
# # handling image file with matplotlib
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# import os
# BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)
# data = os.path.join(BASE_DIR, 'almight.png')

# img = mpimg.imread(data)
# print(type(img))
# plt.imshow(img)

# plt.show()


# from PIL import Image
import os
BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)
# data = os.path.join(BASE_DIR, 'almight.png')
# img2 = Image.open(data)
# img2.show()
# print(img2.format)

# BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)
# data = os.path.join(BASE_DIR, 'sahil.txt')
# with open(data) as f:
#     while True:
#         str1 = f.readline()
#         if str1:
#             print(str1)
#             print('position in loop =',f.tell())
#         else:
#             break


# with open(data) as f:
#     str1 = f.readline()
#     f.seek(15)
#     print('current position = ',f.tell())
#     print(f.read())


# try:
#     filename = os.path.join(BASE_DIR, 'data.txt')
#     total = 0
#     count = 0

#     with open(filename , 'r') as file:
#         for line in file:
#             numbers = line.split()
#             print(numbers)
#             for number in numbers:
#                 try:
#                     num = float(number)
#                     total += num 
#                     count += 1
#                 except:
#                     print('error invalid value found')
    
#     if count > 0:
#         average = total/count
#         print(f'average is: {average}')
#     else:
#         print('no value in the file')

# except:
#     print('error')










# find all the numbers in the string 
import re
name = '''jl kgd v ler o34r940i2-0492304302493049304934ngiongstngiengoenrgoierng '''
pattern = r'\d+'
name_list = re.findall(pattern,name)
print(name_list) 


ageDict = {
    1 : {
        'name': 'sahil',
        'rollno' : 21,
        'status' : 'awesome'
    },
    2: {
    'name': 'bhushan',
    'rollno' : 1,
    'status' : 'medium awesome'
    },
    3: {
    'name': 'evil',
    'rollno' : 21,
    'status' : 'not awesome'
}
}
# converting dictonary into series 
import pandas as pd 
series_agedict = pd.Series(ageDict)

df = pd.DataFrame.from_dict(ageDict, orient='index')
print(df)


string = 'we need to inform him with the latest information: '
allinform = re.findall('inform',string)
print(allinform)
for i in allinform:
    print(i)

if re.search('inform',string): print('exist') 
else: print('not')

print(re.search('inform',string))
print(list(re.finditer('inform',string)))


# create a file , open that file and take all the content in it
with open(os.path.join(BASE_DIR, 'data.txt')) as f :
    data = f.read()
print(data)
data_them = re.findall("(sahil|them)",data)
print(data_them)

# save the enrollment dict into 
# the name , mobile , pan , 10th , 12th , gradmarks - input user will add
# 1. this input first validate all input information
# 2. after validation add into the dict and will return the roll no 
# 3. save this info in a file 
# 4. on the next record check if already record exist then add with new id
# 
# 
# i want you to generate me a code :
# take name , mobile , pan , 10th marks , 12th marks , graduation marks from the user ,
# always validate the information ( the loop will not end until the user has entered right marks or typed exit (something like that))
# once the user has entered the valid input save it into the file , all data should have a unique id per data record
#  
def get_next_id(file_name):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            if not lines:
                return 1
            last_line = lines[-1]
            last_id = int(last_line.split(",")[0])
            return last_id + 1
    except:
        return "error"


def get_input(prompt, validate_fn):
    while True:
        value = input(prompt)
        if value.lower() == "exit":
            return None
        try:
            if validate_fn(value):
                return value
            else:
                print("Invalid input. Try again or type 'exit'.")
        except:
            print("Invalid input. Try again or type 'exit'.")


def sahil_name(x):
    return x.replace(" ", "").isalpha()


def sahil_mobile(x):
    return x.isdigit() and len(x) == 10


import re
def sahil_pan(x):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    return bool(re.match(pattern, x.upper()))

def sahil_marks(x):
    m = float(x)
    return 0 <= m <= 100


file_name = os.path.join(BASE_DIR, "student_data.txt")

while True:
    name = get_input("Enter name: ", sahil_name)
    if name is None:
        break

    mobile = get_input("Enter mobile (10 digits): ", sahil_mobile)
    if mobile is None:
        break

    pan = get_input("Enter PAN: ", sahil_pan)
    if pan is None:
        break

    marks_10 = get_input("Enter 10th marks (0-100): ", sahil_marks)
    if marks_10 is None:
        break

    marks_12 = get_input("Enter 12th marks (0-100): ", sahil_marks)
    if marks_12 is None:
        break

    graduation = get_input("Enter graduation marks (0-100): ", sahil_marks)
    if graduation is None:
        break

    record_id = get_next_id(file_name)

    with open(file_name, "a") as f:
        f.write(
            f"{record_id},{name},{mobile},{pan},{marks_10},{marks_12},{graduation}\n"
        )

        print("saved successfully!")
