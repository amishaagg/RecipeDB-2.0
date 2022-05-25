import nltk
from nltk.tag.stanford import StanfordNERTagger
import os
import pandas as pd

java_path = "C:/Program Files/Java/jre1.8.0_321/bin/java.exe"
os.environ['JAVA_HOME'] = java_path

with open('test.txt') as f:
    sentence = f.read()

jar = './stanford-ner-tagger/stanford-ner.jar'
model = './stanford-ner-tagger/recipedb-corpus.ser.gz'

ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

words = nltk.word_tokenize(sentence)
pred = ner_tagger.tag(words)

test = pd.read_csv("annotated_test - Sheet1 (1).csv")
dic = {}
dic2 = {}
for i, row in test.iterrows():
    dic[row['Word']] = row['Tag']
    dic2[row['Tag']] = 1
correct = 0
for i in pred:
    if len(i[0]) == 0 or i[1] == dic[i[0]]:
        correct += 1
print("Accuracy on Test", correct / len(pred) * 100, '%')