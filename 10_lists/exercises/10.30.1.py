'''
Draw a reference diagram for a and b before and after the
third line of the following python code is executed:

    a = [1, 2, 3]
    b = a[:]
    b[0] = 5

'''

a = [1, 2, 3]
b = a[:] # <<< b = [1, 2, 3]
b[0] = 5 # <<< [5, 2, 3]

print(b) # <<< 5, 2, 3
