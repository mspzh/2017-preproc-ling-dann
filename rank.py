import codecs

file = codecs.open('./wiki.txt', 'r', 'utf-8-sig')
filee = file.read()
words = []

frequency = {}

words = filee.split(' ')

for j in words:
    if j is not ' ':
        j = j.strip('[.?!,"]')
        if j not in frequency:
            frequency[j] = 1
        else:
            frequency[j] += 1

freq = []
for j in frequency:
    freq.append((frequency[j], j))

freq.sort(reverse=True)

rank = 1
min = freq[0][0]
ranks = []
for i in range(0, len(freq)): 
	if freq[i][0] < min: 
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))


filee2 = codecs.open('./ranked.txt', 'w', 'utf-8-sig')
for j in ranks:
    filee2.write(str(j[0]) + ' ' + str(j[1]) + ' ' + j[2] + '\n')
filee2.close()
