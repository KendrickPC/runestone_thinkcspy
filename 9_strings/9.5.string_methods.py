# 9.5 String Methods

'''
ss = "    Hello, World    "
els = ss.count("l")

print(els)

print("***" + ss.strip() + "***")
print("***" + ss.lstrip() + "***")
print("***" + ss.rstrip() + "***")

news = ss.replace("o", "***")
print(news)
'''

'''
food = "banana bread"
print(food.capitalize())

print("*" + food.center(25) + "*")
print("*" + food.ljust(25) + "*")     # stars added to show bounds
print("*" + food.rjust(25) + "*")

print(food.find("e"))
print(food.find("na"))
print(food.find("b"))

print(food.rfind("e"))
print(food.rfind("na"))
print(food.rfind("b"))

print(food.index("e"))
'''

'''
person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

person = input('Enter your name: ')
print('Hello {}!'.format(person))
'''

'''
# There can be multiple substitutions, with data of any type. Next
# we use floats. Try original price $2.50 with a 7% discount:

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)


# Format strings can give further information inside the braces showing how to
# specially format data. In particular floats can be shown with a specific number
# of decimal places. For two decimal places, put :.2f inside the braces for
# the monetary values:
'''

a = 5
b = 9
setStr = 'The set is  {{ { }, {} } }.'.format(a, b)
print(setStr)
