# 10.10 Objects and References
'''
Since strings are immutable, Python can optimize resources by making two
names that refer to the same string literal value refer to the same object.
'''

a = "banana"
b = "banana"

print(a is b) # <<< True


print("\nNew Reference:")
a = [81, 82, 83]
b = [81, 82, 83]

print(a is b) # <<< False
print(a == b) # <<< True



