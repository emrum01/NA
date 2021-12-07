import numpy as np

# オイラー法で1階微分方程式の数値解を得る関数
# t0:tの初期値
# y0:y初期値
# tmax:tの最大値
def euler_method_1ord(t0, y0, tmax,func,n):
    
    # t0～tmaxを2**n+1個に分割
    t = np.linspace(t0, tmax,n)

    # tの刻み幅⊿t
    dt = t[1] - t[0]

    # tと同じ形状の未初期化配列
    y = np.empty_like(t)

    # y[0]に初期値y0を代入
    y[0] = y0

    # オイラー法でt毎の数値解を計算
    for k in range(len(t)-1):
        y[k+1] = y[k] + func(t[k], y[k]) * dt
    return t[-1], y[-1],dt

def func(x,y):
    return x*y

print(euler_method_1ord(0,1,1,func,101))

def rungeKutta(t_0,y_0, t_max, f,n):
    tpoints = np.arange(t_0, t_max+0.01,1/n)
    ypoints = []
    y = 1.00
    h = euler_method_1ord(0,1,1,func,101)[2]
    for t in tpoints:
        print(t)
        ypoints.append(y)
        k1 = h*f(y,t)
        k2 = h*f(y+0.5*k1  , t+0.5*h)
        k3 = h*f (y+0.5*k2, t+0.5*h)
        k4 = h*f(y+k3, t)
        y += (k1+2*k2+2*k3+k4)/6
        print(y)
    return ypoints[-1]
print(rungeKutta(0,1,1,func,100))
