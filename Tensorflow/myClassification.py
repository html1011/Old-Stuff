import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import re
import json
# 1) Create an index thingy.
strIt = "|"
try:
        indexThing = {
                strIt: 0
        }
        try:
                with open("stuff.json", "r") as f:
                        indexThing = json.load(f)
        except:
                print("Hey there!")
        def code(text):
                return [indexThing.get(i, "?") for i in text]
        def decode(text):
                reverse = dict([(value, key) for (key, value) in indexThing.items()])
                return " ".join([reverse.get(i, "?") for i in text])
        count = 1
        def add(link, linkIt):
                if(linkIt):
                        read = open(link, "r").read()
                        # Push in our values if we haven't already got them in there.
                        print(tf.__version__)
                else:
                        read = link
                splitFull = read.split("\n")
                for i in range(len(splitFull)):
                        splitFull[i] = re.findall("\w+", splitFull[i].lower())
                spl = re.findall("\w+", read)
                for i in range(len(spl)):
                        spl[i] = spl[i].lower()
                        if spl[i] not in indexThing:
                                # print(list(indexThing)[len(list(indexThing)) - 1])
                                indexThing[spl[i]] = len(list(indexThing))
                # spl = ' '.join(spl)
                coded = code(spl)
                # Okay, now we've coded and decoded our string.
                # Then what we can do is the actual machine learning part.
                # Well, we're almost on that part.
                # First we have to push in our actual inputs and our actual outputs.
                # We start by splitting our codes up properly by splitFull.
                newCoded = []
                pos = 0
                while(len(coded)):
                        newCoded.append(coded[0:len(splitFull[pos])])
                        del coded[0:len(splitFull[pos])]
                        pos = pos + 1
                        
                # Now we push them in.

                # Okay, now that we've split it up, we're going to use our things as inputs. For the very moment, we're just taking every other position as our input.
                train_data = []
                train_labels = []
                for i in range(len(newCoded)):
                        if i % 2 == 0:
                                train_data.append(newCoded[i])
                        else:
                                train_labels.append(newCoded[i])
                train_data = keras.preprocessing.sequence.pad_sequences(
                        train_data,
                        maxlen=200,
                        padding="post",
                        value=indexThing[strIt]
                )
                print(train_data)
                train_labels = keras.preprocessing.sequence.pad_sequences(
                        train_labels,
                        maxlen=200,
                        padding="post",
                        value=indexThing[strIt]
                )
                return (train_data, train_labels)
        (train_data, train_labels) = add("myText.txt", True)
        # (test_data, test_labels) = add("testdata.txt", True)
        # print(add("myText.txt"))

        # Now that we've perfectly split everything up, let's add some padding to our inputs and our outputs.

        # Perfecto!
        # print(train_data, train_labels)
        print("Status of labels: {}".format("CORRECT!" if len(train_data) == len(train_labels) else "Look quickly over your inputs and outputs; make sure someone answers for every question!"))
        if len(train_data) != len(train_labels):
                exit()
        vocab_size = len(list(indexThing))
        model = keras.Sequential()
        # model.add(keras.layers.Embedding(vocab_size, 16)) # Takes integer-coded vocabulary and looks up the vector for each word index.
        # model.add(keras.layers.GlobalAveragePooling1D()) # Allows model to handle the input of variable length in the simplest way possible.
        model.add(keras.layers.Dense(100, activation=tf.nn.relu))
        # model.add(keras.layers.Dense(100, activation=tf.nn.softmax))
        model.add(keras.layers.Dense(200, activation=tf.nn.relu))
        model.compile(optimizer="adam",
        loss="mean_squared_error")
        # Let's check its validation
        x_val = train_data[:int(len(train_data))]
        # partial_x_train = train_data[int(len(train_data)):]
        y_val = train_data[:int(len(train_labels))]
        # partial_y_train = train_labels[int(len(train_labels) / 2):]
        # print(str(len(test_data)) + " " + str(len(test_labels)))
        history = model.fit(x_val,
                        y_val,
                        epochs=200,
                        batch_size=1,
                        validation_data=(x_val, y_val),
                        verbose=1)
        # results = model.evaluate(test_data, test_labels)

        # print(results)
        print("Talk to me and I'll try to respond!")
        # 1) Convert our input into our little form.
        inputI = input()
        prevInput = ""
        while(inputI != "exit"):
                # print(inputI)
                # print([0])
                arr = model.predict(add(inputI, False)[0])
                for i in range(len(arr[0])):
                        arr[0][i] = int(arr[0][i])
                words = decode(arr[0]).split(" ")
                for i in range(len(words)):
                        words[i] = (words[i], " ")[words[i] == strIt]
                str = (" ".join(words))
                print(decode(str))
                print("Was that right? (Y / (Write correct answer)):")
                ans = input()
                if ans != "Y":
                        with open("myText.txt", "a") as a:
                                        a.write("\n" + inputI + "\n" + ans)
                                        print(add(ans, False)[0])
                                        model.fit(add(inputI, False)[0], add(ans, False)[0], epochs=100)
                                        a.close()
                inputI = input()
        import atexit

        def exit_handler():
                # Now we're going....
                # Save all the work we've done so far.
                open("stuff.json", "w").write(json.dumps(indexThing, indent=4))

        atexit.register(exit_handler)
except KeyboardInterrupt or SystemExit:
        open("stuff.json", "w").write(json.dumps(indexThing, indent=4))
