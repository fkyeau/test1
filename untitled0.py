# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:06:42 2022

@author: fkyeau
"""

import tensorflow as tf
import keras as k
tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello,world!')
sess = tf.compat.v1.Session()
print(sess.run(hello))
