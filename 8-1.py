import tensorflow as tf

x = tf.constant([64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y = tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])
meanX = tf.reduce_mean(x)
meanY = tf.reduce_mean(y)

sumXY = tf.reduce_sum((x-meanX)*(y-meanY))
sumX = tf.reduce_sum((x-meanX)*(x-meanX))

w = sumXY/sumX
b = meanY - w*meanX

print("w = ",tf.Session().run(w))
print("b = ",tf.Session().run(b))

