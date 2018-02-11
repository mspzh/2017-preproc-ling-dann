import re

PUNCT_ARR = '".!?:,()'

def inf_to_sentences(text):
    text = text.replace("\n", "")
    text = re.sub('([.!?:])', '\\1ə', text)
    sentences = text.split("ə")
    return sentences


def sentences_processing(sentence, counter):
    words_to_write = []
    sentence = sentence.strip()
    if sentence:
        j = 0
        sent_to_write = '#sent_id = ' + str(counter+1) + '\n#text = ' + sentence + '\n'
        for word in sentence.split(" "):
            new_word = word.strip(PUNCT_ARR)
            if word[0] in PUNCT_ARR:
                j+=1
                words_to_write.append(str(j) + '\t' + word[0] + '\t_'*8 + '\n')
            j+=1
            words_to_write.append(str(j) + '\t' + new_word + '\t_'*8 + '\n')
            if word[-1] in PUNCT_ARR:
                j+=1
                words_to_write.append(str(j) + '\t' + word[-1] + '\t_'*8 + '\n')
    else:
        return '', ['']
    return sent_to_write, words_to_write

if __name__ == '__main__':
    with open("wiki.txt") as infile:
        text = infile.read()
        igbo_text = inf_to_sentences(text)
        with open('tokenized.txt', 'w') as outfile:
            for i, sentence in enumerate(igbo_text):
                sent, words = sentences_processing(sentence, i)
                outfile.write(sent)
                outfile.write(''.join(words))
                outfile.write('\n')
