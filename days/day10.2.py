
try:
    import pyodbc

    server = r"LAPTOP-2HCHVK65\SQLEXPRESS"
    database = "EDUCATION_SYSTEM"  

    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    print("Connection Successful")

    cursor.execute('select * from EDUCATION_SYSTEM.[dbo].[Marks]')
    records = cursor.fetchall()
    for row in records:
        print(row)
except:
    print('error in connection')
finally:
    cursor.close()
    conn.close()

'''
task:
create menu table in the database (hotel_sahil) - make a fake menu to add
and 
fetch all the data of the menu from database and according to the menu take order from the user ( from console)
and once the data is entered then store that data into orders table in the hotel_sahil table, order table should have unique order id , also creation date of the order 
and then generate the bill from both orders and menu table - the bill should also be printed in console
'''


'''
creatation and delation time of the record being created and updated 

at what time it has transfered   ( whenever it is transfered from one place to other)
'''

''' ( TO DO THINGS)
lint in library
log in library (FSD)
module and package
'''

'''
numpy and pandas
dusk or dask 
polas and spark database
'''

