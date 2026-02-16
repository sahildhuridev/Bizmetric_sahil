'''
Docstring for days.day8
This code demonstrates concepts related to *args, return vs yield, and generators:

    1. *args usage
    - Functions accept variable number of arguments using *d
    - Iterating over arbitrary positional arguments

    2. Function with return (sub2)
    - Calculates cumulative total
    - Prints current value and running total
    - Returns total immediately in first loop iteration
    - Because return is inside loop, function stops after first element

    3. Generator function with yield (sub3)
    - Uses yield instead of return
    - Produces multiple values for each iteration
    - Execution pauses and resumes at each yield
    - Generates multiple strings per loop iteration
    - Does not stop after first iteration like return

    4. Difference between return and yield
    - return → ends function completely
    - yield → pauses function and continues from same state next time
    - yield makes the function a generator

    5. Generator behavior
    - Calling sub3() returns a generator object
    - Values are produced one by one using next() or by converting to list()

    Overall, this code explains the difference between normal functions and generator functions using return vs yield with *args.

'''


d = [1,2,3,4,5]

def sub2(*d):
    tot = 0
    for i in d:
        tot += i
        print(i,tot)
        return tot
    

def sub3(*d):
    tot = 0
    for i in d:
        tot += i
        print(i,tot)
        yield f'{tot} first time'
        yield f'{tot} second time'
        yield f'{tot} third time'
        yield f'this is the fourth time'

