import tensorflow as tf
from tensorflow import keras
import numpy as np
import notify2
notify2.init("Finished?")
with open("./NAMES.txt", "r") as i:
    nameList = i.read().split("\n")
'''
Input: First letter
Output: Padded name
'''
dictionary = {
    " ": 0
}
def code(name):
    return [dictionary[i.lower()] for i in name]

def decode(name):
    reverse = dict((value, key) for (key, value) in dictionary.items())
    print(name)
    return "".join([reverse.get(round(i * 100)/100, "?") for i in name])
maxlen = len(list(nameList[0]))
model = keras.Sequential()
for i in range(len(nameList)):
    nameList[i] = list(nameList[i])
    for ii in nameList[i]:
        if ii.lower() not in dictionary:
            dictionary[ii.lower()] = len(dictionary.items())
    nameList[i] = code(nameList[i])
    if len(nameList[i]) > maxlen:
        maxlen = len(nameList[i])
maxDict = len(dictionary.items()) - 1
for i in dictionary:
    dictionary[i] /= maxDict
    # dictionary[i] = round(dictionary[i] * 100) / 100
# Okay. Since I can't figure out an input, we'll just use the first letter.
nameList = keras.preprocessing.sequence.pad_sequences(
    nameList,
    maxlen=maxlen,
    padding="post"
)
inputSize = 1
model.add(tf.keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(inputSize, activation=tf.nn.sigmoid))
model.add(tf.keras.layers.Dropout(0.5))
model.add(keras.layers.Dense((inputSize + maxlen) / 2, activation=tf.nn.relu))
model.add(keras.layers.Dense(maxlen * 8, activation=tf.nn.tanh))
model.add(keras.layers.Dense(maxlen * 16, activation=tf.nn.relu))
model.add(keras.layers.Dense(maxlen * 8, activation=tf.nn.tanh))
model.add(keras.layers.Dense(maxlen * 4, activation=tf.nn.selu))
model.add(keras.layers.Dense(maxlen))
model.compile(optimizer="adam", loss="mean_squared_error")
# nameList = np.array(nameList)
times = 1
for i in range(0, len(nameList)): # CHANGE STEP TO CONTROL SPEED
    if (round(i / len(nameList) * 1000)/10) % 1 == 0:
        coolStr = ""
        for ii in range(int(round(i / len(nameList) * 1000)/20)):
            coolStr += "="
        print("%s%%" % (coolStr + "> " + str(round(i / len(nameList) * 1000)/10)))
    '''
    Vreeta
    Dretta
    Vrettñ
    Vrettña
    Etñaa
    Reetna
    Vreta
    Veta
    Srettña
    Aeetñaa
    '''
    model.fit(np.array([[nameList[i][0]]]),
    np.array([nameList[i]]),
    verbose=False,
    epochs=3) # CHANGE NUMBER OF EPOCHS TO CONTROL SPEED
nameList = np.array(nameList)
# xList = []
# for i in range(0, len(nameList)):
#     xList.append(nameList[i][0])
# xList = np.array(xList)
# model.fit(xList,
# nameList,
# epochs=300,
# verbose=True)
n = notify2.Notification("Hello", message="Heeeey! We're reeeady!")
n.set_urgency(notify2.URGENCY_NORMAL)
n.show()
inputI = input("Now enter a letter: ")
while inputI != "exit":
    choice = model.predict(np.array([code(inputI.lower())])) # code(inputI.lower()
    # Okay, we actually have to find who is closer to who.
    result = ""
    choice = [i / 100 for i in choice[0]]
    for i in choice:
        reverse = dict((value, key) for (key, value) in dictionary.items())
        closest = float("inf")
        for ii in reverse:
            if abs(ii - i) < closest:
                closest = abs(ii - i)
            else:
                result += reverse[ii]
                break
    print(result)
    inputI = input("Pick another letter or exit: ")