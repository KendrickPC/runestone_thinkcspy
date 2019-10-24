# What is the longest word in Alice in Wonderland? 
# How many characters does it have?


f = open('alice.txt', 'r')

count = {}

for line in f:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = count.keys()
# keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')

for word in keys:
    print(word)
    # out.write(word + " " + str(count[word]))
    # out.write('\n')


# print("The word alice appears " + str(count['word']) + " times in the book.")