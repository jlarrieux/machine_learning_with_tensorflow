import tensorflow as tf
firstnumber = tf.constant([10, 20, 30, 35, 40, 50])
secondnumber = tf.Variable(firstnumber + 50)
with tf.Session() as session:
 session.run(tf.global_variables_initializer())
 print(session.run(secondnumber))
session.close()