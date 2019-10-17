'''
Create a list called myList with the following six items:
76, 92.3, “hello”, True, 4, 76. Do it with both append and with
concatenation, one item at a time.
'''

myList_1 = []

myList_1.append(76)
myList_1.append(92.3)
myList_1.append('hello')
myList_1.append(True)
myList_1.append(4)
myList_1.append(76)

print("\nmyList_1 using append:")
print(myList_1)


list_a = [76, 92.3, 'hello']
list_b = [True, 4, 76]

myList_2 = list_a + list_b

print("\nmyList_2 using concat:")
print(myList_2)
