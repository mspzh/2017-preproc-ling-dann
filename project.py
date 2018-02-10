import re, codecs, sys
import fileinput

dic = ['\\le', '\\di', '\\src', '\\al', '\\var', '\\msp', '\\ps',
       '\\psr', '\\dfr', '\\smr', '\\dff', '\\smf', '\\dfe', '\\sme',
       '\\ex', '\\trr', '\\trf', '\\tre', '\\dt']
#не забыть про сортировку переводов

def articles(src):
    entry = []
    for line in src:
        line = line.strip()
        if (line == ''):
            yield entry
            entry = []
        else:
            [tag, *data] = line.split(' ', 1)
            entry.append((tag, data[0] if data else ''))
    yield entry

def normal_article(art):
    dictionary = []
    for tag in dic:
        match = [i for i in art if i[0] == tag]
        dictionary += match if len(match) else [(tag, '')]
    return dictionary

def write_dictionary(art):
    return '\n'.join((l[0] + ' ' + l[1] for l in art)) + '\n'

for art in articles(fileinput.input()):
    print(write_dictionary(normal_article(art)))
