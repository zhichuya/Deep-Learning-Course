import numpy as np
x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x_sum = np.sum(x)
y_sum = np.sum(y)
x_ = x_sum/x.size
y_ = y_sum/y.size
i = 0
wup = 0
wdown = 0
while i<x.size:
    wup += ((x[i]-x_)*(y[i]-y_))
    wdown += ((x[i]-x_)*(x[i]-x_))
    i+=1
w = wup/wdown
b = y_-(w*x_)
print("w = ",w," b = ",b)