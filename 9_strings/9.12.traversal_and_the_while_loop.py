# 9.12 Traversal and the While Loop
'''
The while loop can also control the generation of the index values.
Remember that the programmer is responsible for setting up the initial
condition, making sure that the condition is correct, and making sure
that something changes inside the body to guarantee that the condition
will eventually fail.
'''

fruit = "apple"

position = 0
while position < len(fruit):
    print(fruit[position])
    position = position + 1

