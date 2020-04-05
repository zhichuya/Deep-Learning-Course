import  numpy as np
import tensorflow as tf

x1 = np.array([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2 = np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
y = np.array([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])
x0 = np.ones(len(x1))
x = np.stack((x0,x1,x2),axis = 1)
y = np.array(y).reshape(-1,1)
X = tf.constant(x)
Y = tf.constant(y)
Xt = tf.transpose(X)
XtX_1 = tf.linalg.inv(tf.matmul(Xt,X))
XtX_1_Xt = tf.matmul(XtX_1,Xt)
W = tf.matmul(XtX_1_Xt,Y)
W = tf.reshape(W,[1,3])
X1 = float(tf.Session().run(W[0][1]))
X2 = float(tf.Session().run(W[0][2]))
b = float(tf.Session().run(W[0][0]))
while(1):
    A = float(input("请输入房屋面积，范围：20-500之间的实数"))
    R = int(input("请输入房间数，范围：1-10之间的整数"))
    if(A<20 or A>500 or R<1 or R>10):
        if(A<20 or A>500):
            print("输入的面积不在范围内，请重新输入")
            continue
        if(R<1 or R>10):
            print("输入的房间数量不在范围内，请重新输入")
            continue
    else:
        break

G = A*X1+R*X2+b
print("模型估计房价为：",G)



