def log_output(msg):
    print(msg)
    with open("sahil.txt", "a") as f:
        f.write(str(msg) + "\n")



a = int(input("Enter an integer: "))
log_output(str(a))
log_output(float(a))



marks = list(map(int, input("Enter marks separated by space: ").split()))
log_output(tuple(marks))
log_output(set(marks))



lst = []
val = input("Enter a value to append: ")
lst.append(val)
log_output(lst)






val2 = input("Enter characters to extend: ")
lst.extend(val2)
log_output(lst)



x = int(input("Enter x: "))
y = int(input("Enter y: "))
listx = list(range(x))
listy = list(range(y))
log_output(list(zip(listx, listy)))



nums = [x for x in range(201) if x % 13 == 0]
log_output(nums)



nums = [x for x in range(300, 401) if x % 4 == 0]
log_output(nums)



s1 = set(map(int, input("Enter set1 elements: ").split()))
s2 = set(map(int, input("Enter set2 elements: ").split()))
log_output(s1.union(s2))
log_output(s1.intersection(s2))
log_output(s1.difference(s2))


name = input("Enter name: ")
dob = input("Enter DOB (DD-MM-YYYY): ")
password = f"{name[:4]}@{dob[:2]}{dob[3:5]}"
log_output(password)



n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    log_output("*" * i)



val = input("Enter a string: ")
for i in range(len(val)+1):
    log_output(val[:i])



n = int(input("Enter limit: "))
odds = [x for x in range(n) if x % 2 != 0]
log_output(odds)



word = input("Enter word: ")
if word == word[::-1]:
    log_output("Palindrome")
else:
    log_output("Not Palindrome")



def fib_sahil(n):
    if n <= 1:
        return n
    return fib_sahil(n-1) + fib_sahil(n-2)
n = int(input("Enter number: "))
log_output(fib_sahil(n))



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
n = int(input("Enter number: "))
log_output(factorial(n))



nums = list(map(int, input("Enter numbers: ").split()))
freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

    log_output(freq)
