# -*- coding: utf-8 -*-
#!/usr/bin/env python

from transl import transl
import sys

PUNCT_ARR = '".!?:,()'

def translate_word(word):
	if word in PUNCT_ARR:
		transliterated_word = word
	else:
		transliterated_word = ''
		for symbol in word:
			transliterated_word += transl.get(symbol, '')
	return transliterated_word

if __name__ == '__main__':
	inf = sys.stdin
	with sys.stdout as outfile:
		for line in inf:
			if line != '\n':
				if line[0] == "#":
					outfile.write(line)
				else:
					trans_word = translate_word(line.split("\t")[1])
					line = line.replace("_\n", "")
					appendix = "Transl=" + trans_word
					line += appendix
					outfile.write(line)
					outfile.write('\n')
			else:
				outfile.write(line)
	inf.close()
