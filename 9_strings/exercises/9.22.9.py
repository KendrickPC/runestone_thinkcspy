'''
Write a function that recognizes palindromes.
(Hint: use your reverse function to make this easy!).
'''


def is_palindrome(myStr):
    # your code here
    if myStr == ''.join(reversed(myStr)):
        return True
    else:
        return False


print(is_palindrome("blue"))
print(is_palindrome("racecar"))
