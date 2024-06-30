price = input('WHat is the price $')
price = float(price)

if(price == 0):
    price('Enter price')
elif(price<0):
    print('Invalid price')
elif (price<10):
    price('Discount price', price*0.9)
else:
    print('The price is $', price)

