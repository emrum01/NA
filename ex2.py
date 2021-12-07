import numpy as np
def ans(a,b,c):
    #解の公式
    x1 = (-b + np.sqrt(b*b - 4.0*a*c))/(2.0*a)
    x2 = (-b - np.sqrt(b*b - 4.0*a*c))/(2.0*a)
    return [x1,x2]

a=1.0
b=-8000.0
c=1.0
#単精度パート. pythonの浮動小数点型はデフォルトで64bit
xDouble1 = ans(a,b,c)[0]
xDouble2 = ans(a,b,c)[1]

#倍精度パート. 32bitにキャスト
numbers = np.array([a,b,c],dtype = np.float32)
#変数、要素を全て32bitにキャストし、ダメ押しで配列全体を32bitにキャスト
xSingle = np.array([(-numbers[1].astype('float32') + np.sqrt(numbers[1].astype('float32')**2.0 - 4.0*numbers[0].astype('float32')*numbers[2].astype('float32')))/(2.0*numbers[0].astype('float32')),
(-numbers[1].astype('float32') - np.sqrt(numbers[1].astype('float32')**2.0 - 4.0 * numbers[0].astype('float32') * numbers[2].astype('float32')))/(2.0*numbers[0].astype('float32'))],dtype=np.float32)

#xSingle1 = ans(a2,b2,c2,1)[0]
#xSingle2 = ans(a2,b2,c2,1)[1]

print("Task 1. Quadratic equation ax^2+bx+c=0")
print("-------------------------------")
print("a = 1.0  b = -8000.0  c = 1.0")
print("Single precision  x1 = {}  x2= {:.16e}".format(xSingle[0],xSingle[1]))
print("Double precision  x1 = {}  x2= {}".format(xDouble1,xDouble2))
print("")
print("There are errors between single (4 bytes) and double precision (8 bytes),and error values are ")
print("x1:{}".format(xSingle[0]-xDouble1))
print("x2:{}".format(xSingle[1]-xDouble2))
print("")
#task2  
x = 1.0E12
#rearranged
fx1 = np.log((x+1)/x)
print("Task 2. Cancellation")
print("------------")
print("ln(x+1)-ln(x),     x = 1.0E12 : 1.0018652574217413E-12")
print("ln((x+1)/x), x = {} : {}".format(x,fx1))


x = 1.0E9
#rearranged
fx2 = 1/(np.sqrt(x**2+1)+x)
print("")
print("sqrt(x^2+1)-x,     x = 1.0E9 : 0.0")
print("1/(sqrt(x**2 + 1) + x),  x = {} : {}".format(x,fx2))

x = np.radians(44.999999999999)
#rearranged
fx3 = np.cos(2.0*x)
print("")
print("cos^2(x)-sin^2(x), x = 44.999999999999 : 3.5083047578154947E-14")
print("cos(2*x), x = 44.999999999999 : {}".format(fx3))
