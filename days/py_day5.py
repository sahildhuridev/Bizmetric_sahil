# # (DOUBT) if we have one big function and two function inside that function how can we access the variables in the function

# def sahil_super(sahil : int):
#     num_1 = sahil
#     def super_two():
#         num_2 = 5
#         num_1 += num_2
#         return num_1

# print(sahil_super(10))    
    

# # (DOUBT) 

# # lazy binding issue: 
# funcs = []
# for i in range(3):
#     funcs.append(lambda  : i)
# for f in funcs:
# 	print(f())

# # why it is not printing the list when i convert using list function
# print(list(funcs))

# print('\n')

# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i : i)

# for f in funcs:
# 	print(f())

# # slicing
# a = 'sahil sadanand dhuri'
# print(a[:])
# print(a[:4])
# print(a[-5:-2])
# print(a[15:18])
# print(a[::-1])
# print()


# fibonacci series:
# def fibonac(n):
#     if n == 1 : return 1
#     if n == 0 : return 0
#     return fibonac(n-1) + fibonac(n-2)
# print(fibonac(4))
# '''

# '''


# def val_mobile(mobile):
#     if mobile.isdigit() and len(mobile)==10:
#         val =mobile
#         flag = True
#     else:
#         val = "Error"
#         flag = False
#     return val , flag

# def acceot_input():
#     name = input('enter name:')
#     mobile =input('enter mobile')
#     return name , mobile

# input_val = acceot_input()



# # try and except:
# import sys
# try:
#     xyz = int(input('enter number'))
# except:
#     print(sys.exc_info)
# finally:
#     print('this runs even after error occur')


while True:
    try:
        n = input('please enter an integer bet 1 to 9: ')
        print(n)
        n = float(n)
        print(n)
        if n > 9 or n < 1:
            raise Exception()
        else:
            break

    except ValueError:
        print('alphabets are entered')
    except Exception:
        print('enter number between 1 to 9: ')
    except AgeError:
        print('eefefe')
    finally:
        print('this code runs all the time')
print('you have successfully done this code')


class AgeError(Exception):
    pass

def setfv(age):
    if age < 0:
        raise AgeError("Age vannot be negative.")