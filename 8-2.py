import tensorflow as tf

x = tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
n = tf.size(x)
n = tf.cast(n,dtype = "float32")
XY = tf.reduce_sum(x*y)
X_Y = tf.reduce_sum(x)*tf.reduce_sum(y)
XX = tf.reduce_sum(x*x)
X_X = tf.reduce_sum(x)*tf.reduce_sum(x)
w = (n*XY-X_Y)/(n*XX-X_X)

b1 = tf.reduce_sum(y)
b2 = tf.reduce_sum(x)
b = (b1-w*b2)/n

print("w = ",tf.Session().run(w))
print("b = ",tf.Session().run(b))

