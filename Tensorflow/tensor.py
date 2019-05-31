# Sets up environment
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0) # also tf.float32 implicitly
total = tf.add(a, b, name="add1")
print(a)
print(b)
print(total)
sess = tf.Session()
sess.run(total)
output = sess.run(total)

writer = tf.summary.FileWriter(".", graph=sess.graph)
print(sess.run(total))