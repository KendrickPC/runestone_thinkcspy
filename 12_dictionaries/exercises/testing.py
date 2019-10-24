pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
# and so on

sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))
