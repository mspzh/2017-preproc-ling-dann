import codecs
igbo = codecs.open('/Users/mariasapozhnikova/Downloads/wiki.txt', 'r', 'utf-8')
igbo_text = igbo.read()

text = []
words = []

counter_lines = 0
counter_characters = 0
counter_words = 0

text = igbo_text.split('. ')

for j in text:
    if j is not '':
        counter_lines += 1


for j in igbo_text:
    if j is not ' ':
        counter_characters += 1

words = igbo_text.split(' ')

for j in words:
    if j is not '—.,=+!?:':
        counter_words += 1

print('Number of lines: ' + str(counter_lines))
print('Number of words: ' + str(counter_words))
print('Number of characters: ' + str(counter_characters))
