import pandas as pd
import numpy as np
a = [1,2,3]
b = [10,20,30]
series1 = pd.Series(a)
series2 = pd.Series(b)

print(series1 , series2)

print(series1.index)
series1.index = ['sahil','sadanand','dhuri']
print(series1.index)
print(series1)


# passing dict to series it makes keys as index and value as series value 
dict1 = {
    1 : ['sahil','sadanand','dhuri'],
    2 : [1,2,3],
    3 : [True , True, True],
    'mobile' : 7400220888,
    'fname' : 'godspeed'

}
series3 = pd.Series(dict1)
print(series3)

print(series3[1])
print(series3.mobile) # attribute style method : NOT RECOMMENDED


# loc : location based on the index name:

# if we want a specific range:
print(series3.loc[1:2])

# if we want specific column :
print(series3.loc[['fname','mobile']])

# iloc
print(series3.iloc[0:3]) # for slicing we need iloc ( slicing operation in series (pd))
print(series3.iloc[:]) # creates copy

# gives how many rows and column it has 
print(series3.shape , series3.ndim)


# we can also create numpy array to series 
c = np.array([1,2,3,4,5,6])
print(c)
series4 = pd.Series(c)
print(series4)

print(f"series1 : \n {series1} \n series2 : \n {series2} \n series3 : \n {series3} \n series4 : \n {series4} \n")

series5 = series2 + series4
print(series2 , '\n' , series4)
print(series5)

def fun_name(x):
    if pd.isna(x):
        return 0
    elif x % 5 == 0 :
        return x * 100
    else:
        return x * 10

for i in series5:
    print(fun_name(i))

print(series5)
print(series5.apply(fun_name))
print(series5)

# pandas help us store hetrogenous data 
# - series is homogenous type of data ,
#  if not then it return object or else it return the datatype
# in numpy all data should be homogenous

# ende iter , series iter 


print('-------------------DATAFRAMES--------------------------------------------')
# collection of series is the dataframe

df =  pd.DataFrame(np.random.randn(5,4))
print(df)


print(df.index , df.columns)

# changing index and column
df.index = [0,1,2,3,4]
df.columns = ['0A','1B','2C','3D']

print(df)


# generating new column based on previous two columns
df['TOTAL'] = df['0A'] + df['1B']+df['2C'] + df['3D']

print(df)


# generating dataframe using dictonary:
# we need to have same elements in the iterative object

d1 = {
    'A' : [1,2,3,4,5],
    'B': [6,7,8,9,10],
    'C' : [11,12,13,14,15],
    'D' : [16,17,18,19,20],
    'E' : {5 : 'sahil', 2: 'sadanand', 3 : "Dhuri" , 4 : "godspeed" , 8: "hero"}
}

#df1 = pd.DataFrame(d1, index = ['P','Q','R','S','T'])
#print(df1)
df1 = pd.DataFrame(d1, index=[1,2,3,4,5])
print(df1)


# resetting index ( we can reset index only twice)
print('orignal df \n' , df)
# RESET INDEX
df.reset_index(inplace=True)
print('reset inplace = true \n' , df)
# SET INDEX
# df.set_index('A', inplace=True)
# print('set_index inplace = true \n' , df)

# extracting record from dataframe 
# we use lock (loc)
print(df.loc[[0],['index','0A','1B']])
# we use iloc
print(df.iloc[2,1:4])
# setting a specific value as different value
print(df)
df.loc[3 , 'TOTAL'] = np.nan
print(df)
# adding new index and making some value different
df.loc[5 , 'TOTAL'] = 1000
print(df)

# drops complete row whenever there is null
df_deleted_row = df.dropna() # by default zero
print(df_deleted_row)

# drops complete column where there is null value
print('dropping before')
df_deleted_column = df.dropna(axis = 1)
print(df_deleted_column)
print('dropping after')

# drop a specific column
#df.drop('column_name', axis = 1)
#df.drop('0A', axis = 1)


print(df['TOTAL'] < -0.5) # output in true and false

print(df[df['TOTAL'] < -0.5]) # takes only true value and display all records

print(df[df['TOTAL'] < -0.5][['0A','1B','TOTAL']]) # takes only true value and display all 

print(df.loc[df['TOTAL'] < -0.5, ['0A','1B','TOTAL']]) # We can also do it using .loc




print('---------------------------- GROUP BY -------------------------------------')
sahil_dict = {
    "numbers": [1, 2, 3, 2, 4, 5, 1],
    "fruits": ["apple", "banana", "apple", "cherry", "mango", "banana", "apple"],
    "booleans": [True, False, True, True, False, True, False],
    "grades": ["A", "B", "A", "C", "B", "D", "A"]
}

df2 = pd.DataFrame(sahil_dict)
print(df2)

df2.describe()

abc = df2.groupby("fruits")["numbers"]
print(abc.mean())


result = df2.groupby("fruits")["numbers"].mean()
print(result)


result = df2.groupby("fruits").agg({"numbers": "mean"})
print(result)



print('---------------------------- MISSING DATA ----------------------------------')
df3 = pd.DataFrame({
    'A': [1,8 , np.nan, 4, 5],
    'B': [np.nan, 7, 8, 9, 10],
    'C': [11, np.nan, 13, 14, 15],
    'D': [16, 17, 18, np.nan, 20],
    'E': [21, 22, 23, 24, np.nan]
})

print(df3)

print(df.info())

print(df3.shape[1])

# formula to calculate missing value
print((df3.isna().sum()/df.shape[0])*100)



df3.fillna(100) # makes all the nan valye as 100


# filling the data using mean of the column values
df_filled_using_mean = df3[['A','B','C','D']].fillna(df3[['A','B','C','D']].mean())
print(df_filled_using_mean)


print('---------------------orignal---------------------')
print(df3)
# bfill : backward fil : previous value gets filled using bfill
print('-----------------bfill----------------------')
df3_bfill = df3.bfill()
print(df3_bfill)
print('-----------------bfill axis 1----------------------')
df3_bfill = df3.bfill(axis= 1)
print(df3_bfill)

print('---------------------orignal---------------------')
print(df3)
# ffill : next value gets filled using this function
print('-----------------ffill----------------------')
df3_ffill = df3.ffill()
print(df3_ffill)
print('-----------------ffill axis 1----------------------')
df3_ffill = df3.ffill(axis=  1)
print(df3_ffill)

print('------------------df3.ffill().bfill()-----------------------------------------')
df3_ffill_bfill = df3.ffill().bfill()
print(df3_ffill_bfill)


print('-----------------OPERATIONS ON DATA------------------------')
print('nunique')
print(df2['fruits'].nunique())
print('unique')
print(df2['fruits'].unique())
print('value_counts')
print(df2['fruits'].value_counts())


print('--------merging --- joining ---- concatination-------------')
# ------------------- DataFrame 1 -------------------
df1 = pd.DataFrame({
    'A': [1, 102, 103, 104, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15],
    'D': [16, 17, 18, 19, 20], # Unique
    'E': [21, 22, 23, 24, 25] # Unique
},index = [0,1,2,3,4])

# ------------------- DataFrame 2 -------------------
df2 = pd.DataFrame({
    'A': [101, 102, 103, 104, 105],
    'B': [106, 107, 108, 109, 110],
    'C': [111, 112, 113, 114, 115],
    'F': [116, 117, 118, 119, 120], # Unique
    'G': [121, 122, 123, 124, 125] # Unique
},index = [5,6,7,8,9])

# ------------------- DataFrame 3 -------------------
df3 = pd.DataFrame({
    'A': [201, 202, 203, 204, 205],
    'B': [206, 207, 208, 209, 210],
    'C': [211, 212, 213, 214, 215],
    'H': [216, 217, 218, 219, 220], # Unique
    'I': [221, 222, 223, 224, 225] # Unique
}, index = [10,11,12,13,14])

print("DF1")
print(df1)
print("\nDF2")
print(df2)
print("\nDF3")
print(df3)

# concating different elements
concat_df = pd.concat([df1,df2,df3])
print(concat_df)

concat_df = pd.concat([df2,df3,df1]) # changing order changes index value 
print(concat_df)

concat_df = pd.concat([df1,df2,df3], axis = 1) # indexes did not match so it create more columns 
print(concat_df)

print(df3.shape , df3.ndim)


# resetting index as index is jumbled
concat_df = pd.concat([df2,df3,df1]).reset_index()
print(concat_df)



print('------------------------MERGING-------------------------------------')

print('\n ---------------------------------inner-------------------------------')
df_merge = pd.merge(df1,df2, how = 'inner' ,on = ['A'], suffixes= ['__DF1','__L1'] )
print(df_merge)
print('-------------------right----------------------------------')
df_merge = pd.merge(df1,df2, how = 'right' , on = 'A' )
print(df_merge)
print('-------------------left----------------------------------')
df_merge = pd.merge(df1,df2, how = 'left' , on = 'A' )
print(df_merge)
print('-------------------outer----------------------------------')
df_merge = pd.merge(df1,df2, how = 'outer' , on = 'A' )
print(df_merge)
print('----------------cross product-------------------------------')
df_merge = pd.merge(df1,df2, how = 'cross' )
print(df_merge)

# how merge differ from concat and how join differ from concat

