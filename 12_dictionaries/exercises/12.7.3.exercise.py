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


import string

infile = open('alice.txt', 'r')

text = infile.readlines()

counts = {}

for line in text:
    for word in line:
        counts[word] = counts.get (word, 0) +1
'''
if word != " ":
    if word != ".":
'''         

word_keys = sorted(counts.keys())


infile.close()

outfile = open("alice_words.txt", 'w')
outfile.write("Word \t \t Count \n")
outfile.write("======================= \n")

for word in word_keys:
    outfile.write("%-12s%d\n" % (word.lower(), counts[word]))

outfile.close()

