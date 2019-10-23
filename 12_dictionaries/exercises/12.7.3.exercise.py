'''
Write a program called alice_words.py that creates a text file named
alice_words.txt containing an alphabetical listing of all the words,
and the number of times each occurs, in the text version of Alice’s
Adventures in Wonderland. (You can obtain a free plain text version
of the book, along with many others, from http://www.gutenberg.org.)
The first 10 lines of your output file should look something like this:

    Word        Count

    a           631
    a-piece     1
    abide       1
    able        1
    about       94
    above       3
    absence     1
    absurd      2

'''


f = open('alice.txt', 'r')

# Empty dictionary to keep key/value pairs of letters and number of occurances
count = {}

for line in f:
    for word in line.split():
        # Removal of all punctuations.
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # Set to lower case
        word = word.lower()

        # Ignoring numbers inside text.
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

# Python3 sort documentation call
keys = sorted(count.keys())

# saving word count to a file.

out = open('alice_words.txt')

for word in keys:
    out.write(word +  ' ' + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")


# f.close()




