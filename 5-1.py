import numpy as np
np.random.seed(612)
RandomArray = np.random.rand(1000)  #生成1000个[0,1)区间的随机数组
print("请输入一个1-100之间的整数：",end="")
a = int(input())
i = 0
j = 1
print("序号  索引值  随机数")
for R in RandomArray:
    if(i%50==0):
        print(" ",j," ",i," ",R)
        j+=1
    i+=1
