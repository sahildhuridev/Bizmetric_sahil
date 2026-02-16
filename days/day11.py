# # # numpy and pandas

# # # np.array(iterable object) - converts any iterable object into numpy array

# # # numpy array is homogenous type of data ( cannot have different elements like list)
# # # if single element in character then all the elements will be in character 

# # a = [1,2,3,4,5]
# # b = [3,4,5,3,4]

# import numpy as np 
# # arr1 = np.array(a)
# # arr2 = np.array(b)

# # # arange(start , end - 1)
# # arr3 = np.arange(2,10) # ([2,3,4,5,6,7,8,9])

# # arr = np.array([[1,2,3],
# # [4,5,6],[1,2,3]])
# # print(arr)
# # print(arr.shape, arr.ndim)

# # arr2 = np.array(
# #     [
# #     [
# #         [1,2],[3,4]
# #     ],
# #     [
# #         [5,6],[7,8]
# #     ]
# # ])
# # print(arr2)
# # print(arr2.shape , arr2.ndim)


# # arr5 = np.array(
# #     [[
# #         [
# #             [1,2,3],[4,5,6],[3,4,5]
# #         ],
# #         [
# #             [1,2,3],[4,5,6],[7,8,9]
# #         ]

# #     ],
# #     [
# #         [
# #             [1,2,3],[4,5,6],[3,4,5]
# #         ],
# #         [
# #             [1,2,3],[4,5,6],[7,8,9]
# #         ]

# #     ],
# #     [
# #     [
# #         [1,2,3],[4,5,6],[3,4,5]
# #     ],
# #     [
# #             [1,2,3],[4,5,6],[7,8,9]
# #     ]
# #     ]]
# # )
# # print(arr5 , arr5.shape , arr5.ndim)


# # # np.nan - we put in the array where we do not know the value of it
# # # np.isnan(# iterable object) : it will return object into true or false

# # sahil = [23,23,23,23,np.nan , 34 , 43 ]
# # #np.isnan()
# # print(np.isnan(sahil))
# # print(sum(np.isnan(sahil)))

# # convert nan value : assign new value to nan value
# sahil[np.isnan[sahil]]= 100
# print(sahil) # changes nan value to 100




# arr2[1,1] = np.nan
# arr2[1,2] = np.inf
# print(arr2)
# cond = np.isnan(arr2) | np.isinf(arr2)
# print(cond)



import numpy as np
arr2 = np.random.randint(10,50 , size = (3,4))
arr2 = arr2.astype(float)
arr2[::-1,]
print(arr2)

# array 

sahil_3d_array = np.random.randint(
    0,        
    100,     
    size=(2, 3,6)  
)
print('new')
print(sahil_3d_array)
print("Shape:", sahil_3d_array.shape)
print("Dimensions:", sahil_3d_array.ndim)


# print(sahil_3d_array[1:5,1:2])
# print('with reverse')
# print(sahil_3d_array[-3:-1,-3:-1])
# print('bew')
print(sahil_3d_array[1:4,[1,1]])

# re-shape
sahil_3d_array = sahil_3d_array.reshape(6,6)
print(sahil_3d_array,sahil_3d_array.ndim, sahil_3d_array.shape)

# flatten 
# flatten is given 1 dimenstional data and re-shape is giving 2 dimensional data

a = sahil_3d_array.flatten()
print(a)
# ravel
b = sahil_3d_array.ravel()
print(b)

print('before change')
print(sahil_3d_array,a,b)

a[1] = 99
b[2] = 55
print('after change')
print(sahil_3d_array,a,b)


# what is the meaning of copy and deep copy ? assigment operator or deep copy



# copying a portion of main array using slicing and .copy()
print('slicing and copy')
sahil_3d_array_copy = sahil_3d_array[:2,:2].copy()
print(sahil_3d_array_copy)

# name wise marks scored by person in each subject
names = np.array([
    'sahil',
    'sadanand',
    'dhuri',
    'hero',
    'villian',
    'awesome',
    'goldenknight'
])
data = np.random.randint(30,100,size=(7,4))

print('shape of names', names.shape , names.ndim)
print('shape of data', data.shape , data.ndim)

print('names')
print(names)

print('data')
print(data)

# working on conditional statement of the array
print(names == 'sahil')
print(data[(names == 'sahil') | (names == 'dhuri')])
print(data[(names == 'sahil') & (names == 'dhuri')])

print(data[(names == 'sahil'),2])

co = names == 'sahil'
a = data[co,:][:,1:3]
print(a)

print(data[names == 'sahil'])
print(data[names == 'sahil'][0,3])
print('other')
print(data[(names == 'sahil') | (names == 'dhuri')])
print('-----------------')
print(data[(names == 'sahil') | (names == 'dhuri')][1,3])

print('----------------------')
print('input')
print(data[(names == 'sahil') | (names == 'dhuri')])
print('output')
print(data[(names == 'sahil') | (names == 'dhuri'), :][:,[1,3]])
print('other output')
print(data[(names == 'sahil') | (names == 'dhuri'),:][1,3])
print('other output')
print(data[(names == 'sahil') | (names == 'dhuri')][1,3])

# print('skipping element')
# input('input : orignal array')
# print(sahil_3d_array)
# print('output')
# print(sahil_3d_array[::-1,::-1])

# floor , ceil , roundoff , sqrt , isnan , isinf , np.maximum , np.mimimum , np.add , np.sub , eval 
# np.random.random(2,2) # generating any number from 0 to 1
# np.random.randn(5) : normal distribution data
# np.random.normal(4)

# i = 0
# while i < 20:
#     print(np.random.random(2,2))
#     i +=1
print(np.random.randn(5))
print(np.random.random((2,2)))
print(np.random.normal(size = 4))

# centre point should be 15 and variance should be 2 and take all the data coming under this
print(np.random.normal(15 , 2))

# randint
# np.random.seed - stores the data that has been generated
# np.random.seed(34)# always an integer

print('------------------------------')
# array.min() , max() , mean()  
print(' min() max() mean()')
print(sahil_3d_array.min())
print(sahil_3d_array.max())
print(sahil_3d_array.mean())
print('------------------------------')

print(sahil_3d_array)
print('axis 0')
print(np.amin(sahil_3d_array,axis=0))
print('axis 1')
print(np.amin(sahil_3d_array,axis=1))


# np.full() , np.eye()
# zeros_likes() , ones_like() 

# np.zeros((2,3)) -> create a new array of zeroes
# np.ones((2,3))

# array addition and subraction ( require same dimensions and shapes)
# array multiplication and array boardcast

# reversing rows and columns and from -3 row take everything onwards
sahil_3d_array[::-1,::-1][-3:,:]
sahil_3d_array[-3:,:][::-1,::-1]

# np.flipr()

print(sahil_3d_array.shape,sahil_3d_array.ndim)

print('orignal')
print(sahil_3d_array)
print('diagonal')
print(sahil_3d_array.diagonal())
print('flipud')
print(np.flipud(sahil_3d_array).diagonal())
print('fliplr')
print(np.fliplr(sahil_3d_array).diagonal())

print('position of max value: ', np.argmax(sahil_3d_array))

# np.where(condition)
print(np.where(sahil_3d_array > 90, 'A',np.where(sahil_3d_array > 60 , 'B',np.where(sahil_3d_array > 40 , 'C','D'))))
print(sahil_3d_array[np.where(sahil_3d_array > 60)])


# data type:
# 1. numeric : continous , discrete
# 2. categorical : nominal , binary , ordinal 
#  


# create two arrays of same shape
# np.concatenate()
# np.hstack()
# np.c_
sahil_3d_array = np.random.randint(
    0,
    100,
    size=(1, 3,6)
)

sahil_3d_array_part2 = np.random.randint(
    0,
    100,
    size=(1, 3,6)
)

print('array 1')
print(sahil_3d_array)
print('array 2')
print(sahil_3d_array_part2)
print('concatenate: ')
print(np.concatenate([sahil_3d_array,sahil_3d_array_part2],axis=0))
print('hstack')
print(np.hstack([sahil_3d_array,sahil_3d_array_part2]))
print('__c')
print(np.c_[sahil_3d_array,sahil_3d_array_part2])

print('sorting')
print('orignal')
print(sahil_3d_array)
print('sorting')
print(np.sort(sahil_3d_array))
print('sorting axis 0')
print(np.sort(sahil_3d_array, axis= 0))
print('sorting axis 1')
print(np.sort(sahil_3d_array, axis= 1))


sahil_3d_array = np.random.randint(0,100,size=(2,3,6))
print('input: ')
print(sahil_3d_array)
print('sorting using axis = 0')
print(np.sort(sahil_3d_array, axis=0))

# argsort the first column
sorted_system = sahil_3d_array[:,2].argsort()
print(sorted_system)

#print(sahil_3d_array[sorted_system])
lexsorted_index = np.lexsort((sahil_3d_array[2,:],sahil_3d_array[1,:]))
