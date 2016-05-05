#!/usr/bin/python
# coding: utf-8
# nlp process of twitter data using nltk package

__author__ = "x-web"

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
import re

inputf = open('tweets.txt', 'r')
outputf = open('tweets_segment.txt', 'w')
# record every valid tweet's id
tidf = open('tid.txt', 'w')

english_stopwords = stopwords.words('english')
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', "#", '$', '%']
st = LancasterStemmer()
reword = re.compile(r'^[\w]+$', re.I)
noiseword = ['http', 'rt']
count = 1

def isWord(word):
    mword = reword.match(word)
    if mword and word not in noiseword:
        return True
    else:
        return False

for tweet in inputf:
    # 小写化
    tweet_lower = [word for word in tweet.lower().split()]
    # 分词
    tweet_tokenized = [word.lower() for word in word_tokenize(tweet.decode("utf-8"))]
    # 去停用词
    tweet_filtered_stopwords = [word for word in tweet_tokenized if not word in english_stopwords]
    # 去标点符号
    tweet_filtered = [word for word in tweet_filtered_stopwords if not word in english_punctuations]
    # 词干化
    tweet_stemmed = [st.stem(word) for word in tweet_filtered]
    # 抽取有意义的单词
    tweet_filtered_nword = [word for word in tweet_stemmed if isWord(word)]
    result = " ".join(tweet_filtered_nword)
    if result != '':
        outputf.write(result + "\n")
        tidf.write(str(count) + "\n")

    print count
    count += 1

inputf.close();
outputf.close();
tidf.close();

print 'Done'
