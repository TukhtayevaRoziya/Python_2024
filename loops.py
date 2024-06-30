total = 0

while input('Continue? (Y/N) ') == 'Y':
    qty = int(input('Enter quantitie: '))
    if (qty < 0 ):
        break
    total += qty
else:
    print(total)