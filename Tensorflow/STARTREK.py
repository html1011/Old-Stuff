import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import re
import json
import requests
import copy
import re
try:
        print("Fetching offline text...")
        with open("offline.txt", "r") as f:
                # r.text = f.read()
                r = "\r\n".join(f.read().split("\n"))
except:
        inputIt = input("Save for offline use? (Y/N) ")
        URL = "http://www.chakoteya.net/NextGen/219.htm"
        r = requests.get(url = URL)
        if inputIt == "Y":
                with open("offline.txt", "w") as f:
                        f.write(r.text)
                        f.close()
r = re.sub(r'<.*?>', '', r.text if hasattr(r, "text") else r)
# r = r[0:30]

chars = str.maketrans(dict.fromkeys(',?.!\''))
lines = []
indexThing = {
        "<NEW_LINE>": 0
}
characters = {
        "<NEW_LINE>": 0
}
try:
        with open("newList.json", "r") as f:
                indexThing = json.load(f)
except:
        print("")
def code(txt, decoder):
    return [decoder.get(i.lower(), "<NEW_LINE>") for i in txt]

def decode(txt, decoder):
    reverse = {decoder.get(i, 0): i for i in decoder}
    return "".join([reverse.get(i, "<NEW_LINE>") for i in txt])

def add(r):
        r = r.split("\r\n")
        r = r[20:len(r)]
        for i in range(len(r)):
                string = r[i].split(": ")
                if len(string) == 2:
                        # We begin dialogue here.
                        if string[0] not in characters:
                                characters[string[0]] = len(dict.items(characters))
                stringA = list(string[0])
                for ii in range(len(stringA)):
                        newStr = stringA[ii]
                        if newStr.lower() not in indexThing:
                                indexThing[newStr.lower()] = len(dict.items(indexThing))
        return (characters, indexThing)
(characters, indexThing) = add(r)
print(characters)
print(indexThing)
# print(characters)
# So. Right now we've added our characters and our indexThing.
# Now we're going to train the code, line by line, to respond to something talking to it,
# Given the name of the person and what they said.
# print(indexThing)
r = r.split("\r\n")
r = r[20:len(r) - 13]
charactersII = []
textII = []
for i in range(len(r)):
        string = r[i].split(": ")
        if len(string) == 2:
                # Beginning of line
                charactersII.append(string[0])
                textII.append(string[1])
                if i + 1 < len(r):
                        while i + 1 < len(r):
                                if len(r[i + 1].split(": ")) != 2 and len(list(r[i + 1])) != 0:
                                        if list(r[i + 1])[0] != "[":
                                                i = i + 1
                                                textII[len(textII) - 1] += " " + r[i]
                                        else:
                                                break
                                else:
                                        break
print(len(charactersII))
print(len(textII))

model = keras.Sequential()
model.compile(optimizer="adam", loss="mean_squared_error")
finalInputOutput = []
for i in range(len(charactersII)):
        charactersII[i] = characters[charactersII[i]]
        fullStr = [i.lower() for i in list(textII[i])]
        fullStr = fullStr[0:len(fullStr) - 1]
        finalInputOutput.append([[charactersII[i]],
        keras.preprocessing.sequence.pad_sequences(
                [code(fullStr, indexThing)],
                maxlen=400,
                padding="post",
                value=indexThing["<NEW_LINE>"]
        )[0].tolist()])
model.add(keras.layers.Dense(len(finalInputOutput[0]), tf.nn.relu))
model.add(keras.layers.Dense(len(finalInputOutput[0]), tf.nn.relu))
finalInput = []
finalOutput = []
for i in range(len(finalInputOutput) - 1):
        # model.fit([finalInputOutput[i][1]],
        # [finalInputOutput[i + 1][1]],
        # epochs=200,
        # verbose=1)
        finalInput.append(finalInputOutput[i])
        finalOutput.append(finalInputOutput[i + 1])
finalInput = np.array(finalInput)
finalOutput = np.array(finalOutput)
print(finalInput)
model.fit(finalInput, finalOutput, epochs=200, verbose=1)
# print(str(decode([charactersII[i]], characters)) + ": " + "".join(decode(code(fullStr, indexThing), indexThing)))
# print(code(r.split(" ")[0], indexThing))
# minLength = 20
# maxLength = 1000
# train_data = keras.preprocessing.sequence.pad_sequences(
#         [code(r.split(" ")[0], indexThing)],
#         maxlen=minLength,
#         padding="post",
#         value=indexThing["<NEW_LINE>"]
# )
# train_labels = keras.preprocessing.sequence.pad_sequences(
#         [code(list(r), indexThing)],
#         maxlen=maxLength,
#         padding="post",
#         value=indexThing["<NEW_LINE>"]
# )
# print(decode(train_data[0], indexThing))
# model = keras.Sequential()
# model.add(keras.layers.Dense(len(list(train_data[0])), activation=tf.nn.relu))
# model.add(keras.layers.Dense(len(list(train_data[0])), activation=tf.nn.relu))
# model.add(keras.layers.Dense(len(list(train_labels[0]))))
# model.compile(optimizer="adam",
# loss="mean_squared_error")
# model.fit(train_data,
# train_labels,
# epochs=2000,
# batch_size=10,
# verbose=1)
# print("Let's try this out!")
# inputI = input("Please enter your beginning sequence: ")
# inputI = keras.preprocessing.sequence.pad_sequences(
#         [code(list(inputI), indexThing)],
#         maxlen=minLength,
#         padding="post",
#         value=indexThing["<NEW_LINE>"]
# )
# # print(train_labels)
# checkUp = [round(i) for i in model.predict(train_data)[0]]
# # print(decode(checkUp, indexThing))