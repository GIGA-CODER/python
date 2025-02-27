import random
import json
import pickle
import numpy as np
import nltk 
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer=WordNetLemmatizer

intents=json.load(open('intents.json').read())

words=[]
classes=[]
documents=[]
ignore_letters=['?','!','.',',']

for intent in intents['intents']:
    for pattern in intents['patterns']:
        word_list=nltk.word_tokenize(pattern)
        documents.append((word_list,intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)








