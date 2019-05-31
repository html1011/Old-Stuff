import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)
imdb = keras.datasets.imdb
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
# num_words = 10000 keeps 10,000 most frequently occurring words; the rest are discarded.
print("Training entries: {}, Labels: {}".format(len(train_data), len(train_labels)))
word_index = imdb.get_word_index()
word_index = {k:(v+3) for k,v in word_index.items()} 
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
def decode_review(text):
    return ' '.join([reverse_word_index.get(i, "?") for i in text])

train_data = keras.preprocessing.sequence.pad_sequences(train_data,
value = word_index["<PAD>"],
padding="post",
maxlen=256)
test_data = keras.preprocessing.sequence.pad_sequences(test_data,
value = word_index["<PAD>"],
padding="post",
maxlen=256)
print(len(train_labels))