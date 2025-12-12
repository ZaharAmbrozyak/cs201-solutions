import json
import string

with open('sherlock.txt', 'r') as file:
    text = file.read()

letters = dict.fromkeys(string.ascii_lowercase, 0)

for symbol in text:
    if symbol in letters.keys():
        letters[symbol] += 1
letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))

words = text.lower().replace('\n', '')
for i in string.punctuation:
    words.replace(i, '')
words = list(filter(lambda x: x != '' and len(x) > 4, words.split()))

word_count = {}
for word in words:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

top_5 = {}
for i in range(5):
    top_5[word_count[i][0]] = word_count[i][1]

words_but = text.replace('!', '.').replace('?', '.').replace('\n', '')
sentences = [sentence for sentence in words_but.split('.') if sentence != '']
sentences_len = []
for sentence in sentences:
    sentences_len.append(len(sentence))
max_sentence = ' '.join(sentences[sentences_len.index(max(sentences_len))].split())
output_max_sentence = {max_sentence, max(sentences_len)}

filename = 'output.json'

output= {"task 1": letters, "task 2": top_5, "task 3": max_sentence}
with open(filename, 'w') as file:
    json.dump(output, file)