import codecs
import sys
import re

igbo = codecs.open('wiki.txt', 'r', 'utf-8')
igbo_text = igbo.read()
sent = []
sent_words = []
counter = 0 #This is the counter for IDs
counter_wordiness = 0 #This is the counter for words inside the sentences
tokenis = codecs.open('./tokenized.txt', 'w', 'utf-8-sig')

igbo_text = re.sub(u'([.!?:])', u'\\1ə', igbo_text)
sent = igbo_text.split(u'ə')

for j in sent:
    j = j.strip()
    if j is '':
        continue
    else:
        counter += 1
        tokenis.write(u'#sent_id = ' + str(counter) + u'\n#text = ' + j + u'\n')
        j = re.sub('([\(\)"?!.])', ' \\1', j)
        sent_words = j.split(' ')
        for k in sent_words:
            if k is '':
                continue
            else:
                k = k.strip()
                counter_wordiness += 1
                tokenis.write(str(counter_wordiness) + u'\t' + k + u'\t_'*8 + u'\n')
                print(str(counter_wordiness) + u'\t' + k + u'\t_'*8 + u'\n')
                if '[?!.]' in k:
                    continue
        counter_wordiness = 0
