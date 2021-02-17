import numpy as np
# x_input = np.random.sample((1,2))
# print(x_input)

 import tensorflow as tf

'''1. Define the variable'''
def var():
    X_1 = tf.placeholder(tf.float32, name = "X_1")
    X_2 = tf.placeholder(tf.float32, name = "X_2")
    
''' Define the computation'''
def comput():
    multiply = tf.multiply(X_1, X_2, name = "multiply")

'''Execute the operation'''
def oper():
    with tf.Session() as session:
        result = session.run(multiply, feed_dict={X_1:[1,2,3], X_2:[4,5,6]})
        print(result)

def main():
    print('run simple TF app')

main()