import numpy as np 


#解きたい方程式
def func_f(x):
    return x**3 - 3*x**2 + 2*x -0.2
#接線の傾き
def func_f_dash(x):
    return 3*x**2 - 6*x + 2

#bisection（方程式の関数項、探索区間の左端、探索区間の右端、誤差範囲）
def bisection(func_f, xneg, xpos, error=1e-7):
    #初期値を表示
    num_calc = 0  #計算回数
    print("iteration {}     x = {:.7}".format(num_calc, (xpos+xneg)/2.0))

    while(True):

        x_mid = (xpos +xneg)/2.0

        #探索区間を更新
        if (0.0 < func_f(x_mid)):  #中間と右端の値が同じの時
            xpos = x_mid  #右端を更新
        else: 
            xneg = x_mid  #左端を更新

        #結果を表示
        num_calc += 1  #計算回数を数える
        print("Iteration {}     x = {:.7f}".format(num_calc, x_mid))

        #「誤差範囲が一定値以下」
        if xpos-xneg <= error:
            break
   
    return x_mid






def newtonsMethod(x0,err):
    x_pre = x0
    num_calc = 0
    while True:
        num_calc += 1
        x0 = - func_f(x_pre)/func_f_dash(x_pre) + x_pre
        print("iteration {}     x = {:.8}".format(num_calc, x0))
        
        if abs(x0 - x_pre)<=err:
            break

        x_pre = x0

x0 =  3
err = 1.0e-7


if (__name__ == '__main__'):
    print('Bisection')
    solution = bisection(func_f, 1.5, 3.0)
    print("")
    print('Newton\'s Method')
    solution2 = newtonsMethod(x0,err)