import numpy as np
np.seterr(divide='ignore')  
#fwd関数
#xのリスト
#正確な解のリスト
#エラーのリスト
n = 6
h = 0.025*np.pi

def fwdDiffFormula(x):
   return (np.sin(x+h)-np.sin(x))/h

def ctrlDiffFormula(x):
    return (np.sin(x+h)-np.sin(x-h))/(2*h)

# xのpiにかかる係数のリストとxのリスト
a = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
x_list = [ i*np.pi for i in a]

#正確な値
exactValues = [np.cos(i) for i in x_list]

# Forward difference formulaで得られた値と誤差のリスト
numericalFwdValues = [ fwdDiffFormula(i) for i in x_list]
fwdErrs = [i - j for i,j in zip(numericalFwdValues, exactValues)]

# Central difference formulaで得られた値と誤差のリスト
numericalCtrlValues = [ ctrlDiffFormula(i) for i in x_list]
ctrlErrs = [i - j for i,j in zip(numericalCtrlValues, exactValues)]

print('Numerical differentiation')
print('')
print('Forward difference')
for i in range(n):
    print('x = {} PI  Deriv =   {:.6f}   Error =  {:.6f}'.format(a[i],numericalFwdValues[i],fwdErrs[i]))
print('')
print('Central difference')
for i in range(n):
    print('x = {} PI  Deriv =   {:.6f}   Error =  {:.6f}'.format(a[i],numericalCtrlValues[i],ctrlErrs[i]))



exactIntgrValue = np.arctan(1)
N = 24

#Trapezoidal
def f1(x):
    return 1/(x**2.0+1)# x^5

a = 0
b = 1
h = (b-a)/N

S1 = (h/2) * (f1(a) + 2*sum(f1(h*i) for i in range(1,N)) + f1(b)) # ①の計算

#Simpson 1/3 rule
def f2(x):
    return 1/(x**2+1)

N = 24

a = 0
b = 1
h = (b-a)/N

S2 = (h/3) * sum((f2(h*i) + 4*f2(h*(i+1)) + f2(h*(i+2))) for i in range(0,N, 2))
print('')
print('Numerical integration')
print('I = Integral(1/(x^2+1)), limits: [0,1]')
print('')
print('Trapezoidal rule, nsub = 24')
print('I =   {:.12f}   Error =  {}   R =  {:e} %'.format(S1, S1-exactIntgrValue,((S1-exactIntgrValue)/S1)*100))
print('')
print('Simpson 1/3 rule, nsub = 24')
print('I =  {:.12f}   Error =  {}   R =  {} %'.format(S2,S2-exactIntgrValue,((S2-exactIntgrValue)/S2)*100))