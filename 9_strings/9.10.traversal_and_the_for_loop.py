# 9.10 Traversal and the for loop
'''

'''

names = ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

for name in names:
    invitation = "Hi " + name + ".  Please come to my party on Saturday!"
    print(invitation)

for avalue in range(10):
    print(avalue)

'''
Since a string is simply a sequence of characters, the for loop iterates
over each character automatically.
'''

for achar in "Go Spot Go":
    print(achar)

'''
The loop variable achar is automatically reassigned each character in
the string “Go Spot Go”. We will refer to this type of sequence iteration
as iteration by item. Note that it is only possible to process the
characters one at a time from left to right.
'''

fruit = "apple"
for idx in range(5):
    currentChar = fruit[idx]
    print(currentChar)

# <<< a
# <<< p
# <<< p
# <<< l
# <<< e

'''
The index positions in “apple” are 0,1,2,3 and 4. This is exactly the same
sequence of integers returned by range(5). The first time through the for loop,
idx will be 0 and the “a” will be printed. Then, idx will be reassigned to
1 and “p” will be displayed. This will repeat for all the range values up to
but not including 5. Since “e” has index 4, this will be exactly right to
show all of the characters.

In order to make the iteration more general, we can use the len function to
provide the bound for range. This is a very common pattern for traversing any
sequence by position. Make sure you understand why the range function behaves
correctly when using len of the string as its parameter value.
'''

fruit = "apple"
for idx in range(len(fruit)):
    print(fruit[idx])


s = "python rocks"
for idx in range(len(s)):
    if idx % 2 == 0:
        print(s[idx])
