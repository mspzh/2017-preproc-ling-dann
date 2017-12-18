import codecs
import sys
import re

igbo = codecs.open('wiki.txt', 'r', 'utf-8')
igbo_text = igbo.read()
sent = []
sent_words = []
counter = 0
counter_wordiness = 0
tokenis = codecs.open('./tokenized.txt', 'w', 'utf-8-sig')

#headers = 'Index;Surface form;Lemma;UPOS;XPOS;Morph. features;Head;Relation;Secondary dependencies;Miscellaneous;'
#tokenis = tokenis.write(headers + '\n')

igbo_text = re.sub(u'([.!?:])', u'\\1ə', igbo_text)
sent = igbo_text.split(u'ə')

for j in sent:
    if j is not '':
        counter += 1
        tokenis.write(u'#sent_id = ' + str(counter) + u'\n#text =' + j + u'\n')
        j = re.sub('([\(\)"?!.])', ' \\1', j)
        sent_words = j.split(' ')
        for k in sent_words:
            if k is not '':
                counter_wordiness += 1
                tokenis.write(str(counter_wordiness) + u';' + k + u';–;'*8 + u'\n')
                if '[?!.]' in k:
                    continue
        counter_wordiness = 0
