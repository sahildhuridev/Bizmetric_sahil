def my_decorator(func):

    def wrapper(*args , **kwargs):
        print("Before function runs")
        func(*args , **kwargs)
        print("After function runs")
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello {name}")

@my_decorator
def add(a,b):
    print(a+b)

say_hello('sahil')

add(3,4)


dict1 = {'name' : ['saguk','sahil'], 'age' : 25 , 'mobleno' : 2 }
dict2 = {'name' : ['ram','ron'], 'age' : 15}
combine_dict = {}
for key in set(dict1) | set(dict2):
    combine_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
print(combine_dict, set(dict1))


from collections import Counter

dict_1 = {"a": 10, "b": 20}
dict_2 = {"a": 5, "c": 30}

result = Counter(dict_1) + Counter(dict_2)

print(dict(result))



sahil_01 = ['shail','eam',23,23.23,3,14,["sahil", [12,343,121,232,'sahil']]]

print(sahil_01[6][1][4][2])

a = {12,324,4,34,'sahil',(23,23,23)}
b = {1,2,4,3}

print(a.intersection(b))
print(a.difference(b)) # difference
print(b.difference(a))
print(a.symmetric_difference(b)) # symetric difference
print(b.symmetric_difference(a))


sahil = {}
sahil["name"]='sahil dhuri'
sahil["mood"] = 'awesome'

print(sahil)

sahil["name"]+='rahul yadav'
sahil["mood"] += 'not awesome'


print(sahil)

# dict1 dict2 - common keys 
dict1 = {
    1 : ['sahil','dhuri'],
    2 : [1,2,3,4,5],
    3 : [2,3,4]
}
dict2 = { 1 : ['awesome'],2 : [9,10,11],'a' : [100,101,102]}

list1 = []
for key_1 in dict1 :
    for key_2 in dict2:
        if key_1 == key_2:
            list1.append(key_1)

print(list1)

combine_dict = dict1 | dict2
print(combine_dict)

d3 = dict1.copy()
for key , value in dict2.items():
    if key in d3 :
        d3[key] += value
    else:
        d3[key] = value

print(d3)


list2 = list(d3.keys())
print(list2[-1] , d3[list2[-1]])


d1 = {1 : [1,2,3,4,5], 2: [6,7,8,9,10],3:[11,12,13,14,15]}
import pandas as pd
df = pd.DataFrame(d1)
print(df)

list1 = [1,2,3,4,5]
name = 'sahil'
print(*name)
print(*list1)
# import time
# from datetime import datetime
# print('before sleep' , datetime.now())
# time.sleep(10)
# print('after sleep' , datetime.now())

import shutil
# shutil.copy('sahil.txt','backup/sahil.txt')


# shutil.move('sahil.txt','backup/sahil.txt')


#shutil.copytree('backup','copytree_23')

name = 'sahil'
last_str = lambda name : name[-1]
print(last_str(name))