'''
Docstring for days.day4
and higher-order functions:

    1. itertools module usage:
        - islice() for slicing iterables
        - count() for infinite counting
        - cycle() for repeating sequence
        - repeat() for repeating element fixed times
        - accumulate() for cumulative operations
        - chain() for combining iterables
        - compress() for filtering using boolean selectors
        - dropwhile() to drop elements while condition is true
        - filterfalse() opposite of filter()

    2. zip() usage:
        - Combining multiple iterables element-wise

    3. Difference between chain() and zip()

    4. eval() function:
        - Evaluating string expressions
        - Evaluating mathematical expressions dynamically

    5. Argument unpacking:
        - *args unpacking
        - **kwargs unpacking
        - Passing dictionary as keyword arguments

    6. Nested functions:
        - Function inside function
        - Calling inner function
        - Returning function resul
    7. Lambda functions:
        - Conditional lambda (ternary operator)
        - Mathematical calculations
        - Length checking logic
        - Default argument in lambda (lambda i=i)
        - Solving late binding problem in 
        8. map() usage:
            - Applying function to list elements
            - Handling mixed data 
        9. reduce() from functools:
            - Reducing list to single value
            - Difference between reduce() and accumulate()

        10. Higher-order functions:
            - Passing function as argument
        	- Returning function results based on condition
        11. Variable scope basics:
            - Local vs global variables



'''



print("sahil")
count = 10
print(count)
def sahilcount():
    count = 30
    count += 10
    print(count)
sahilcount()
#print(globals())

from itertools import islice
list1 = [x for x in range(200)]
print(list1)
i = 0
while i <10:
    print(list(islice(list1,3,6)))
    i += 1

from itertools import count
list2 = count(10,2)
print(list2,type(list2))

i = 0
while i <10:
    print(list(islice(list2,3,6)))
    i += 1
print(list(list2))


from itertools import cycle
count = 1
for item in cycle('XYZ'):
    if count > 17:
        break
    print(item,count)
    count = count+1



from itertools import repeat
repeat_obj = repeat("this is awesome sahil",3)

print(type(repeat_obj))
try:
    x = 0
    while x < 10:
        print(next(repeat_obj))
except:
    print("limit reached")



from itertools import accumulate
import operator
# by default it is addition
iterator = accumulate(range(1,11))
print(list(iterator))
iterator = accumulate(range(1,11),operator.sub)
print(list(iterator))
iterator = accumulate(range(1,11),operator.mul)
print(list(iterator))
print(iterator , type(iterator))


# list

# tuple

# set

# string 


a = {1,2,3}
b = {4,5,6}

c = list(list(x) for x in zip(a,b))
print(c)

from itertools import chain
c = list(list(x) for x in chain(a,b))
print(c)

# why cant i run chain here
d = list(chain(a,b)) 
print(d)

from itertools import chain
a = [1,2,3,4,5]
b = ('sahil','dhuri','21',21,'awesome')
c = {1,2,3}
d = {1:'sahil',2:12,'hero':21}
print(list(chain(a,b,c,d)))
print(list(zip(a,b,c,d)))



from itertools import compress
letters = 'ABCDEFfwwewewfwefewf'
bools = (False , 90 , True, "element", False,None , '','ji')
list(compress(letters,bools))
list(compress(bools,letters))


from itertools import dropwhile
a = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
print(a)
b = list(dropwhile(lambda x: x<5 , a))
print(b)


# FILTER

# FILTERFALSE
from itertools import filterfalse
print(list(filterfalse(lambda x:x>5,a)))
e = '34'
eval(e)

m = 4
x = 2.5
c = 0.5
y = 'm*x+c'
eval(y)
print(y)
print(m * x + c )

a = 5
b = 10

x = 'a + b'
y = a + b

print(eval(x))
print(eval(y))
print(eval(a+b))


nums = (1,2)
print(*nums)

data = {'a':1,'b':2}
print(*data)


def show(a, b):
    print(a, b)

data = {'a': 1, 'b': 2}
show(**data)



def outer():
	def inner():
		print("Hello")
	inner()
outer()


sahil = {
	'a' : 'sahil',
	'b' : 'is',
	'c' : 'awesome'
}
def sahil_funct(**a):
	print(a)
	return a
print(sahil_funct(a = 'sahil', b = 'is', c = 'super', d = 'awesome'))
sahil_funct(**sahil)




funcs = []
for i in range(3):
    funcs.append(lambda : i)

for f in funcs:
	print(f())


funcs = []
for i in range(3):
    funcs.append(lambda i=i : i)

for f in funcs:
	print(f())

# lambda dunction
basic = lambda x : x*100 if x%2 == 0 else x*2
print(basic(20))
print(basic(11))


mat_amt = lambda damt , int_rate : (damt + (damt*int_rate))
print(mat_amt(1000,0.6))

length1 = lambda x : len(x) if type(x) not in (int,float,bool) else x
print(length1('ergbgreigbeoigberugi'))

l2 = [True, False , 12 , 23 ,23.232, 'sahil','dhuri']
a=list(map(length1,l2))
print(a)
# We cannot use list comprehension on data frame so we use it on map()

nums = ['1', '2', '3', 'saguk']

result = list(map(lambda x: int(x) if x.isdigit() else 0, nums))
print(result)

from functools import reduce
# reduce return only one element where accumulate return cumulative operations
summation = reduce((lambda x , y : (x+y)),[1,2,3,4,5])
print(summation)

from itertools import accumulate
summation = accumulate([1, 2, 3, 4, 5], lambda x, y: x + y)
print(list(summation))

def abc(a1):
	outcome = 'inside abc' , a1
	return f'hello abc {a1}'

def pqr(a2):
	print('inside pqr' , a2)
	return f'hello pqr {a2}'

def calling(a4):
	print('calling the inside function')
	var1 = 40
	return a4(var1)

calling(abc)


	


def main_fun(n):
    def fun1():
        return "inside_fun1"
    def fun2():
        return "inside_fun2"

    if n == 1:
        return fun1()
    else:
        return fun2()

x = main_fun(1)
print(type(x))
print(x)
print(main_fun(1))

