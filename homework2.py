import math

# 求二元一次方程函数
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('a,b,c只能为数字')
    if a==0:
        return '请输入不等于0的a值'
    else:
        d=b*b-4*a*c
        if d<0:
            return '无实根'
        elif d==0:
            x=-b/(2*a)
            return x
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            return x1,x2

print(quadratic(1,2,1))
