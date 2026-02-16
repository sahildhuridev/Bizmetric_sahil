# from datetime import datetime , date , time 
# # a = datetime.now()
# # print(a)

# # print(datetime.now().strftime('%A'))


# # print(a.strftime('%y-%m-%d    %D'))

# # dobyear = 2024
# # dobmonth = 2
# # dobdate = 6
# # dob = date(dobyear,dobmonth,dobdate)
# # dob_2 = datetime(dobyear,dobmonth,dobdate)
# # print ( dob , dob_2 , type(dob) )

# # # dob = input('ENTER YOUR DATE OF BIRTH YYYY-MM-DD')

# # # dob = datetime.strptime(dob , '%Y-%m-%d')
# # # print(dob)

# # login = 'see you 14-dec-2012 again it has been a long day without you my friend i will tell you all about it when i see you again'
# # print(datetime.strptime(login , 'see you %d-%b-%Y'))


# # '1-02-1970' 


# # dal = '2029-02-01'
# # print(dal.month , dal.year , dal.timestamp() , dal.weekday())


# # datetime.timestamp(datetime(2003-04-06))
# #datetime.fromtimestamp('2003-04-04')from datetime import datetime
# import time 
# print('before sleep' , datetime.now())
# time.sleep(10)
# print('after sleep' , datetime.now())


# print('using readline()')

# task = open('sahil.txt')
# for i in task.readline():
#  print(i)


# print('using readlines()')

# task = open('sahil.txt')
# for i in task.readlines():
#     print(i)


# print('using read()')

# task = open('sahil.txt')
# for i in task.read():
#     print(i)


# print('appending inside the file: ')


# print(task)
# with open('sahil.txt', 'a') as f :
#    f.write('this is sahil writing into the file \n')
# task = open('sahil.txt')
# print(task)

# print('appending list into the file: ')
# lines = [ 'saguk\n', 'asdbii\n', 'urre\n','qwerty\n'] 
# with open('sahil.txt','a') as f:
#    f.writelines(lines)


# shutil is a library shutil.copy - this is the source file path  
# shutil.copy('source','destination folder path')  
# .copy - it will copy to other location
# .move  - it will remove the file from orignal file location
# .copytree - also copies the folder sub folder structure 


import shutil
# shutil.copy('sahil.txt','backup/sahil.txt')


# shutil.move('sahil.txt','backup/sahil.txt')


shutil.copytree('backup','copytree_2')

# the file which are in kb - small folder , mb - medium folder , gb - large files