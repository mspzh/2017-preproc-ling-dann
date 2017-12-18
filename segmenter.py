import codecs
import re
import sys
igbo = codecs.open('./wiki.txt', 'r', 'utf-8')
igbo_text = igbo.read()

text = []
words = []

counter_lines = 0
counter_characters = 0
counter_words = 0

igbo_text = re.sub(u'([.!?:])', u'\\1ə', igbo_text)
text = igbo_text.split(u'ə')

for j in text:
    if j is not '':
        j = j.strip()
        counter_lines += 1

for j in igbo_text:
    if j in '[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789]':
        counter_characters += 1

words = igbo_text.split(' ')

for j in words:
    j = j.strip
    if j is not '—.,=+!?:':
        counter_words += 1

print('Number of lines: ' + str(counter_lines))
print('Number of words: ' + str(counter_words))
print('Number of characters: ' + str(counter_characters))
