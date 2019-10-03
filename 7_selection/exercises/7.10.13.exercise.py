# Implement the calculator for the date of Easter.
'''
The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

Ask the user to enter a year. Compute the following:

    1. a = year % 19
    2. b = year % 4
    3. c = year % 7
    4. d = (19 * a + 24) % 30
    5. e = (2 * b + 4 * c + 6 * d + 5) % 7

dateofeaster = 22 + d + e

Special note: The algorithm can give a date in April. 
Also, if the year is one of four special years
(1954, 1981, 2049, or 2076) then subtract 7 from the date.

Your program should print an error message if the user provides
a date that is out of range.
'''

year = int(input("Please enter a year between 1900 and 2099: "))


def dateOfEaster(year):
    if year < 1900 or year > 2099:
        return ("\nDate out of range. Please try again.")
        
    elif year >= 1900 and year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7
        date_of_easter = 22 + d + e

        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            date_of_easter = date_of_easter - 7

        if date_of_easter > 31:
            return "April", date_of_easter - 31
        else:
            return "March", date_of_easter

print("\n" + str(year) + " is the year you input.")
print("\nThe date of Easter for " + str(year) + " is the following: ")

print(dateOfEaster(year))

'''
# Checking Easter Sunday dates:
https://kg.vkk.nl/english/organizations/lcc.gb/liturgy/easterdates.html
'''
