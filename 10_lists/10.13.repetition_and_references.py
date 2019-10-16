# 10.13 Repetition and References
'''
With a list, the repetition operator creates copies of the references. 
When we allow a list to refer to another list, a subtle problem can arise.
'''

print("\nNew Reference:")
origlist = [45, 76, 34, 55]
print(origlist * 3) # <<< [45, 76, 34, 55, 45, 76, 34, 55, 45, 76, 34, 55]

newlist = [origlist] * 3

# Note the problem below from referencing the original list:
print(newlist) # <<< [[45, 76, 34, 55], [45, 76, 34, 55], [45, 76, 34, 55]]

'''
newlist is a list of three references to origlist that were created by the
repetition operator. The reference diagram is shown below.

What happens if we modify a value in origlist?
'''

print("\nNew Reference:")
origlist = [45, 76, 34, 55]

newlist = [origlist] * 3

print(newlist) # <<< [[45, 76, 34, 55], [45, 76, 34, 55], [45, 76, 34, 55]]

origlist[1] = 99

print(newlist) # <<< [[45, 99, 34, 55], [45, 99, 34, 55], [45, 99, 34, 55]]


print("\nNew Reference:")
alist = [4, 2, 8, 6, 5]
blist = alist * 2
blist[3] = 999

print(blist)
print(alist)
