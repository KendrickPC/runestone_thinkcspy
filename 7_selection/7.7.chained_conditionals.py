# 7.7. Chained conditionals

x = 25
y = 25

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")



# select-7-2: What will the following code print if x = 3, y = 5, and z = 2?

if x < y and x < z:
    print("a")
elif y < x and y < z:
    print("b")
else:
    print("c")
