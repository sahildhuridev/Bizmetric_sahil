s = int(input('Enter Standard:(1-10): '))
if s == 1 or s == 2 or s == 3 or s == 4:
    standard = '1-4'
elif s == 5 or s == 6 or s == 7 or s == 8:
    standard = '5-8'
elif s == 9 or s == 10:
    standard = '9-10'  

subject = []
print('Hindi, Marathi, English, Science, Maths ')
subject = (input('Enter the book you want to buy:(seprated by space) ').lower()).split(' ')

notebook = []
notebook = input('''enter the book you want:
                 (if you have more then one quantity use - eg: 1-3 -> for 3 square 100 pages )
                 (1) square 100 pages (40 ruppee)
                 (2) square 200 pages (70 ruppee)
                 (3) 4line 100 pages (30 ruppee)
                 (4) 4lines 200 pages (50 ruppee)
                 (5) single_line 100 pages (30 ruppee)
                 (6) single_line 200 pages (50 ruppee)
                 (7) A4 notebook 100 pages (60 ruppee)
                 (8) A4 notebook 200 pages (100 ruppee)
                 please enter the number you want the book of (seprated by space)
                 ''').split(' ')

notebook_dict = {
    '1' : 40,
    '2' : 70,
    '3' : 30,
    '4' : 50,
    '5' : 30,
    '6' : 50,
    '7' : 60,
    '8' : 100
}

book_dict = {
    "1-4":{
        "hindi": 60,
        "marathi": 60,
        "english" : 80,
        "science" : 90,
        "maths" : 100
        },
    "5-8":{
        "hindi": 100,
        "marathi": 100,
        "english" : 100,
        "science" : 120,
        "maths" : 140      
        },
    "9-10":{
        "hindi": 150,
        "marathi": 150,
        "english" : 150,
        "science" : 200,
        "maths" : 250
    }
}

total_amount = 0

for i in subject:
    j = i.split('-')
    book_amount = book_dict[standard][j[0]]
    book_quantity = int(j[1])
    total_amount += book_amount * book_quantity

for i in notebook:
    j = i.split('-')
    book_amount = notebook_dict[j[0]] 
    book_quantity = int(j[1])
    total_amount += book_amount * book_quantity 

print(f"you have to pay :{total_amount} ")



details = {}

details['standard'] = standard
details['subjects'] = {}
details['notebooks'] = {}
details['total_amount'] = total_amount

for i in subject:
    j = i.split('-')
    details['subjects'][j[0]] = int(j[1])


for i in notebook:
    j = i.split('-')
    details['notebooks'][j[0]] = int(j[1])

print(details)




print("\n----- BILL -----")
print(f"Standard : {details['standard']}")
print("\nBooks:")

book_total = 0
for sub, qty in details['subjects'].items():
    price = book_dict[details['standard']][sub]
    amount = price * qty
    book_total += amount
    print(sub, qty, price, amount)

print("\nNotebooks:")
notebook_total = 0
for code, qty in details['notebooks'].items():
    price = notebook_dict[code]
    amount = price * qty
    notebook_total += amount
    print(code, qty, price, amount)

print("\nTotal Amount :", details['total_amount'])
print("--------------")



