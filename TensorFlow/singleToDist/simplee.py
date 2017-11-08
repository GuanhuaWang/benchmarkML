from __future__ import print_function

import tensorflow as tf
import time

def single():
        with tf.device('/cpu:0'):
                a = tf.Variable(tf.truncated_normal(shape=[2]),dtype=tf.float32)
                b = tf.Variable(tf.truncated_normal(shape=[2]),dtype=tf.float32)
                c = a+b

                target = tf.constant(100.,shape=[2],dtype = tf.float32)
                loss = tf.reduce_mean(tf.square(c-target))

                opt = tf.train.GradientDescentOptimizer(0.0001).minimize(loss)

        with tf.Session() as sess:
                sess.run([target])

        sv = tf.train.Supervisor()
        sess = sv.prepare_or_wait_for_session()
        for i in range(1000):
                sess.run(opt)
                if i%10 ==0:
                        r = sess.run(c)
                        print(r)
#               time.sleep(0.1)
if __name__ == '__main__':
        single()