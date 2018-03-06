# Importing nltk package
import nltk
# importing word_tokenize, word_punct_tokenize and sent_tokenize from nltk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
# importing wordnetlammatizer
from nltk.stem import WordNetLemmatizer
# importing ngrams
from nltk import ngrams
# importing counter to count similar elements
from collections import Counter

# initialising lemmatizer
lemmatizer = WordNetLemmatizer()
# opening test file as f
with open('001.txt') as f:
    # striping trailing and leading white spaces
    lines = [line.rstrip('\n') for line in f]
    print("Sent Tokenizer: ")
    for line in lines:
        # tokenizing sentences
        print(sent_tokenize(line))
    print("Word Tokenizer: ")
    for line in lines:
        # tokenizing words
        li = [word_tokenize(t) for t in sent_tokenize(line)]
        print(li)
    print("Lemmatization: ")
    for i in range(len(li)):
        for j in range(len(li[i])):
            # performing lemmatization on words
            print(lemmatizer.lemmatize(li[i][j]), end=" ")
    print("\nBi-grams")
    bigr = []
    for line in lines:
        words = word_tokenize(line)
        # storing bigrams
        grams = ngrams(words, 2)
        for w in grams:
            bigr.append(w)
        print(bigr)
    print("Word Frequency bigram: ")
    # counting similar bigrams
    print(Counter(elem for elem in bigr))
    freqw = [['in','the'],['tree','.'],['Christmas', 'tree'],['can', 'receive']]
    setli = []
    # printing the sentences thta have the most frequently occurred bigrams
    print("Concatenated sentence with most frequent bigrams: ")
    for line in lines:
        wrep = sent_tokenize(line)
    for i in range(len(wrep)):
        for lis in freqw:
            if lis[0] in wrep[i] and lis[1] in wrep[i]:
                setli.append(wrep[i])
    print(*list(set(setli)))







