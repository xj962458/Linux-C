import jieba
textFile = open("1.txt", 'rt', encoding='utf8').read()
words = jieba.lcut(textFile)
counts = {}
for word in words:
    if word == "中国":
        counts[word] = counts.get(word, 0)+1
print(counts)
