# Write a program that asks the user for a sentence in English
# and then translates that sentence to Pirate.

'''
English         Pirate

sir             matey
hotel           fleabag inn
student         swabbie
boy             matey
madam           proud beauty
professor       foul blaggart
restaurant      galley
your            yer
excuse          arr
students        swabbies
are             be
lawyer          foul blaggart
the             th’
restroom        head
my              me
hello           avast
is              be
man             matey
'''

# Global scope of pirate dictionary.
pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['madam'] = 'proud beauty'
pirate['professor'] = 'foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'fould blaggart'
pirate['the'] = "th'"
pirate['restroom'] = 'head'
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'bee'
pirate['man'] = 'matey'


def pirateTranslator():
    prompt = input("Please enter a sentence in English: ")
    prompt = prompt.lower()

    pirate_sentence = []

    words = prompt.split()
    
    for aword in words:
        if aword in pirate:
            pirate_sentence.append(pirate[aword])
        else:
            pirate_sentence.append(aword)

    print(" ".join(pirate_sentence))



pirateTranslator()




