import requests


link = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'

result = requests.get(link)

unique_words = {}

punctuation = '.,?!:;\'\"[]()`-_'
for line in result.text.splitlines():
    for p in punctuation:
        line = line.replace(p, ' ')
    for word in line.split():
        word = word.lower()
        if len(word) > 4:
            unique_words[word] = unique_words.get(word, 0) + 1


print(unique_words['juliet'])

freq = list(unique_words.values())
freq.sort(reverse=True)
freq = freq[:10]
print(freq)

for f in freq:
    for key, values in unique_words.items():
        if values == f:
            print(key, values)