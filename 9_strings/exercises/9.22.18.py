'''
Write a function that implements a substitution cipher. In a substitution
cipher one letter is substituted for another to garble the message.
For example A -> Q, B -> T, C -> G etc. your function should take two
parameters, the message you want to encrypt, and a string that represents
the mapping of the 26 letters in the alphabet. Your function should return
a string that is the encrypted version of the message.
'''

# Reference Research:
# https://stackoverflow.com/questions/36188226/substitution-cipher-python

import random


alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
message = 'Please encrypt this message. Thanks.'

# print(len(alphabet)) # <<< 30
# print(len(key))


def makeKey(alphabet):
    alphabet = list(alphabet)
    random.shuffle(alphabet)
    return ''.join(alphabet)


def encrypt(message, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in message)


def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)


cipher = encrypt(message, key, alphabet)


print(message)
print(cipher)
print(decrypt(cipher, key, alphabet))
