# 2.13 Exercises

print("\n1. Evaluate the following numerical expressions in your head, then use the active code window to check your results:")
print(5 ** 2) # <<< 25
print(9 * 5) # <<< 45
print(15 / 12) # <<< 1.25
print(12 / 15) # <<< 0.8
print(15 // 12) # <<< 1
print(12 // 15) # <<< 0
print(5 % 2) # <<< 1
print(9 % 5) # <<< 4
print(15 % 12) # <<< 3
print(12 % 15) # <<< 12
print(6 % 6) # <<< 0
print(0 % 7) # <<< 0


print("\n2. What is the order of the arithmetic operations in the following expression. Evaluate the expression by hand and then check your work.")
# 2 + (3 - 1) * 10 / 5 * (2 + 3)
# 2 +    2    *    2   *  5 
# <<< 22
print(2 + (3 - 1) * 10 / 5 * (2 + 3)) # <<< 22.0


print("\n3. Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.")

# Working code for question #3 below:
'''
current_time_24_hours = input("\nWhat time is it right now (in hours) on a 24 hour clock? *Do Not Input Minutes* ")
setting_alarm = input("\nHow many hours would you like to have pass by before sounding the alarm? ")
alarm_goes_off_at = int(setting_alarm) % 24 + int(current_time_24_hours)
print("The alarm goes off at: " + str(alarm_goes_off_at))
'''

print("\n4. It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.")

# Working code for question #4 below:
'''
print("\nStarting date #")
print("Sunday = 0")
print("Monday = 1")
print("Tuesday = 2")
print("Wednesday = 3")
print("Thursday = 4")
print("Friday = 5")
print("Saturday = 6")

prompt = input("\nWhat day will you be leaving on your vacation? Note: Please enter starting date # referenced above: ")
question = input("\nHow many days will your vacation be? ")

travel_return_date = (int(prompt) + int(question)) % 7
if travel_return_date == 6:
    print("\nYour return date is Saturday.")
elif travel_return_date == 5:
    print("\nYour return date is Friday.")
elif travel_return_date == 4:
    print("\nYour return date is Thursday.")
elif travel_return_date == 3:
    print("\nYour return date is Wednesday.")
elif travel_return_date == 2:
    print("\nYour return date is Tuesday.")
elif travel_return_date == 1:
    print("\nYour return date is Monday.")
elif travel_return_date == 0:
    print("\nYour return date is Sunday.")
'''


print("\n5. Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.")
a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
i = "dull"
j = "boy"
print(a + " " + b + " " + c + " " + d + " " + e + " " + f + " " + g + " " + h + " " + i + " " + j + ".")


print("\n6. Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.")
print(6 * 1 - 2) # <<< 4
print(6 * (1 - 2)) # <<< -6


print("\n7. The formula for computing the final amount if one is earning compound interest is given on Wikipedia as:")
# Note: Check compound_interest.png picture to see mathematical formula
print("\tWrite a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.")

# Working solution for problem #7
'''
P = 10000 # Principal amount invested
r = 0.08 # interest rate of 8%
n = 12 # number of times the interest rate is compounded per year
t = input("\nNumber of years the money will be compounded: ")
# print(int(t) * n)

A = P * (1+(r/n)) ** (int(t) * n)
print(A)
'''


print("\n8. Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.")

# Working solution for problem #8
'''
# Area = π * r^2
pi = 3.14159265359
r = input("\nWhat is your input radius for the circle? ")
area_of_circle = pi * (int(r) ** 2)
print("\nThe area of your circle is approximately: " + str(area_of_circle))
'''


print("\n9. Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.")

'''
width = input("\nWhat is the width of your rectangle? ")
height = input("What is the height of your rectangle? ")
area = int(width) * int(height)
print("The area of your rectangle is: " + str(area))
'''


print("\n10. Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.")

'''
miles = input("\nHow many miles are driven for the car? ")
gallons = input("How many gallons have been used? ")
miles_per_gallon = int(miles) / int(gallons)
print("The fuel efficiency for the car is: " + str(miles_per_gallon) + " mpg")
'''


print("\n11. Write a program that will convert degrees celsius to degrees fahrenheit.")
# To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
'''
celcius = input("\tPlease input a degrees Celsius you would like to convert: ")
conversion_to_farenheit = int(celcius) * 1.8 + 32
print("\tThe conversion from " + celcius + " degrees Celcius to Farenheit is: " + str(conversion_to_farenheit))
'''


print("\n12. Write a program that will convert degrees fahrenheit to degrees celsius.")
# T(°C) = (T(°F) - 32) / 1.8
farenheit = input("\tPlease input a degrees Farenheit you would like to convert: ")
conversion_to_celcius = (int(farenheit) - 32) / 1.8
print("\tThe conversion from " + farenheit + " degrees Farenheit to Celcius is: " + str(conversion_to_celcius))




