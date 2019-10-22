# 12.4 Aliasing and Copying
'''
Because dictionaries are mutable, you need to be aware of aliasing (as we saw
with lists). Whenever two variables refer to the same dictionary object,
changes to one affect the other. For example, opposites is a dictionary that
contains pairs of opposites.
'''

print("\nExample 1:")
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

# Aliasing is assigned opposites
print(alias is opposites)

# Right is assigned left. Dictionary values are mutable.
# Value assigned to key
alias['right'] = 'left'
print(opposites['right'])

# ------------------------------------------------------------

'''
As you can see from the is operator, alias and opposites refer to the
same object.

If you want to modify a dictionary and keep a copy of the original, use the
dictionary copy method. Since acopy is a copy of the dictionary, changes to
it will not affect the original.

        acopy = opposites.copy()
        acopy['right'] = 'left'    # does not change opposites
'''

print("\nExample 2:")
acopy = opposites.copy()
#  Dictionary values are mutable. Value assigned to key
acopy['right'] = 'left'

print(acopy)

