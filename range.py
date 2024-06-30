# total = 0
# for num in range(0, 6, 2):
#     price = input('Price for item ' + str(num) + ': ')
#     total += float(price)

# print('Total price is', total)

total = 0
for x in range(50):
    total+= x
    print('total num ', total, 'x was ', x)
    if x>2:
        break
    print(x)
print('Total is ', total)