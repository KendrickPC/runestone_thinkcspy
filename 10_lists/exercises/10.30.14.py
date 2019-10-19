'''
Write a function replace(s, old, new) that replaces all
occurences of old with new in a string s:

Hint: use the split and join methods.

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')

'''

string = 'MIssIssIppI'


def replace(string, old, new):
    words = string.split(old)
    glue = new
    new = glue.join(words)
    return new

print(replace(string, 'I', 'i'))
