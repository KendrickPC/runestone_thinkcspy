'''
Modify this code so it prints each subtotal, the total cost,
and average price to exactly two decimal places.
'''

def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', "%.2f" % total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', "%.2f" % count)
    print('Total $', "%.2f" % total)
    print('Average price per item: $', "%.2f" % average)

checkout()
