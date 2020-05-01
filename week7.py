import tensorflow.compat.v1 as tf
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
tf.disable_eager_execution()   
class Train:
    def __init__(self,route):
        self.df = pd.read_csv(route,header = 0)  
        print(self.df.describe())        
        self.df = self.df.values        
        self.df = np.array(self.df)         
    def Standard(self):
        for i in range(12):
            self.df[:,i] = (self.df[:,i] - self.df[:,i].min())/(self.df[:,i].max() - self.df[:,i].min())
        self.x_data = self.df[:,:12]     
        self.y_data = self.df[:,12]           
    def model(x,w,b):     
        return tf.matmul(x,w) + b    
    def Matrix(self):
        self.x = tf.placeholder(tf.float32,[None,12],name="X") 
        self.y = tf.placeholder(tf.float32,[None,1],name="Y") 
        with tf.name_scope("Model"):              
            self.w = tf.Variable(tf.random_normal([12,1],stddev = 0.01),name = "W")
            self.b = tf.Variable(1.0,name = "b")      
            self.pred = Train.model(self.x,self.w,self.b)              
    def LossFunction(self,train_epochs,learning_rate):
        self.train_epochs,self.learning_rate = train_epochs,learning_rate        
        with tf.name_scope("LossFunction"):    
            self.loss_function = tf.reduce_mean(tf.pow(self.y - self.pred,2))   
        self.optimizer = tf.train.GradientDescentOptimizer(self.learning_rate).minimize(self.loss_function)
        self.sess =tf.Session()  
        self.init = tf.global_variables_initializer()    
        self.sess.run(self.init)      
    def iteration(self):     
        self.loss_list = [] 
        for epoch in range(self.train_epochs):
            self.loss_sum = 0.0 
            for xs,ys in zip(self.x_data,self.y_data):
                xs = xs.reshape(1,12)  
                ys = ys.reshape(1,1)               
                _,self.loss = self.sess.run([self.optimizer,self.loss_function],feed_dict={self.x:xs,self.y:ys})
                self.loss_sum = self.loss_sum + self.loss
            self.x_data,self.y_data = shuffle(self.x_data,self.y_data)
            self.b0temp = self.b.eval(session = self.sess)
            self.w0temp = self.w.eval(session = self.sess)
            self.loss_average = self.loss_sum/len(self.y_data)  
            self.loss_list.append(self.loss_average)   
            print("epoch={0:<5}loss={1:<15.7f}b={2:<15.7f}".format(epoch+1,self.loss_average,self.b0temp))
            print("w=")
            print(self.w0temp)       
        print("\n")
        print("每次训练的平均损失值为：")   
        print(self.loss_list)       
    def test(self):
        for i in range(3):
            self.n = np.random.randint(506)
            print("\n")
            print("当前随机抽取的是第{}条数据".format(self.n))
            self.x_test = self.x_data[self.n]

            self.x_test = self.x_test.reshape(1,12)
            self.predict = self.sess.run(self.pred,feed_dict={self.x:self.x_test})
            print("预测值：%f"% self.predict)
            self.target = self.y_data[self.n]
            print("标签值：%f"% self.target)
route = r"boston.csv"  
train_epochs = eval(input("请输入进行迭代的次数："))
learning_rate = float(input("请输入调整的学习率："))    
T = Train(route)       
T.Standard()          
T.Matrix()           
T.LossFunction(train_epochs,learning_rate)
T.iteration()       
T.test()