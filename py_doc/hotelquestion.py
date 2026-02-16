
hotel = input("enter your hotel name: ")
menu = input("what you want to order? ")
quant = input("how much quantity? ")
price = input("price for the product? ")
print("-{:^100}-".format('-'*100))
print("|{:^100}|".format(f'Welcome to {hotel}'))
print("-{:^100}-".format('-'*100))
print("| {0:24} {1:24} {2:>24} {3:>24}|".format('sr','menu','quant','price'))
print("| {0:24} {1:24} {2:>24} {3:>24}|".format('1',menu,quant,price))
print("|{:^100}|".format(''))
print("|{:^100}|".format(''))
print("-{:^100}-".format('-'*100))
print("|{:>20} {:>79}|".format('total',str(int(quant)*int(price))))
print("-{:^100}-".format('-'*100))


