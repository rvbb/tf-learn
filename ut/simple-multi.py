import tensorflow as tf
import numpy as np

tf.get_logger().setLevel('INFO')

####Define the variable
X_1 = tf.placeholder(tf.float32, name = "X_1")
X_2 = tf.placeholder(tf.float32, name = "X_2")

####Define the computation
multiply = tf.multiply(X_1, X_2, name = "multiply")

####Execute the operation
with tf.Session() as session:
    result = session.run(multiply, feed_dict={X_1:[1,2,3], X_2:[4,5,6]})
    print(result)
'''One common practice in Tensorflow is to create a pipeline to load the data. If you follow these five steps, you'll be able to load data to TensorFLow'''

# 1. Create the data

x_input = np.random.sample((1,2))
print(x_input)

# 2. Create the placeholder
x = tf.placeholder(tf.float32, shape=[1,2], name = 'X')
	
# 3. Define the dataset method
dataset = tf.data.Dataset.from_tensor_slices(x)
	
# 4. Create the pipeline
iterator = dataset.make_initializable_iterator()
get_next = iterator.get_next()
	
# 5. Execute the program
with tf.Session() as sess:  
    print(sess.run(iterator.initializer, feed_dict={ x: x_input }))
	