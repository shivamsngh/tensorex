import tensorflow as tf
import numpy as np
data = np.random.randint(5, size=5)
x=tf.constant(0, name='x')
y=tf.Variable(0,'y')
model = tf.global_variables_initializer()

with tf.Session() as session:
    for i in range(5):
        session.run(model)
        y=y+1
        print(session.run(y))