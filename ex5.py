"""
ヤコビ法による固有値問題
Sept. 2017
ok
"""
import numpy as np

A=np.array( [[3,pow(3,1/2)],[pow(3,1/2),1]]) ## テスト計算用行列



B=np.array([len(A),len(A)])
C=np.array([len(A),len(A)])

R=np.identity(len(A))


qri =1e-8  # 収束条件: 非対角成分の最大値

def max_non_diag_abs_val(A): #非対角成分の絶対値をとり，対角項を0にする
    C = np.abs(A)
    for i in range(len(A)):
        C[i,i] = 0
    return np.max(C)

def search_max_index(A): # 非対角成分の絶対値の最大値を求める。
    C = np.abs(A)
    for i in range(len(A)) :
        C[i,i] = 0

    index=np.argmax(C) 
    index_list=[]

    p = index // len(C)
    q = index % len(C)

    index_list.append(p)
    index_list.append(q)

    return index_list 

def elim_diag(AA,p,q):  # Bの相似変換: B_{j-1} -> B_jへ
    D = np.zeros([len(AA),len(AA)])
    D[:,:] = AA[:,:]


    if AA[p,p]-AA[q,q] ==0 :
        print("hit")
        phi = np.pi/4
    else:
        phi = 0.5*np.arctan(-2*AA[p,q]/(AA[p,p]-AA[q,q]))

    #
    for k in range(len(AA)):
            D[p,k] = AA[p,k]*np.cos(phi) - AA[q,k]*np.sin(phi)
            D[k,p] = D[p,k]    

            D[q,k] = AA[p,k]*np.sin(phi) + AA[q,k]*np.cos(phi)
            D[k,q] = D[q,k]

    D[p,p] = (AA[p,p]+AA[q,q])/2+ ((AA[p,p]-AA[q,q])/2)*np.cos(2*phi)-AA[p,q]*np.sin(2*phi)
    D[q,q] = (AA[p,p]+AA[q,q])/2- ((AA[p,p]-AA[q,q])/2)*np.cos(2*phi)+AA[p,q]*np.sin(2*phi)



    D[p,q] = 0.0
    D[q,p] = 0.0

    return D, phi  # 新しいBとギブンス回転角phiを返す

def make_ortho_mat(R,p,q,phi): #ギブンス回転行列の構築
    RR = np.identity(len(A))

    RR[p,p] = np.cos(phi)
    RR[p,q] = np.sin(phi)
    RR[q,p] = -np.sin(phi)
    RR[q,q] = np.cos(phi)

    return np.dot(R,RR)

n_step = 0
B=A
non_diag_max= max_non_diag_abs_val(B)
print(A)
print ("n_step=",n_step,", non_diag_max=",non_diag_max )

#メインループ
while (non_diag_max) >= qri: #非対角成分がqri以下になるまで計算を繰り返す
    n_step += 1
    max_index=search_max_index(B)
    p = max_index[0]
    q = max_index[1]
    B,phi = elim_diag(B,p,q)
    R = make_ortho_mat(R,p,q,phi)

    non_diag_max= max_non_diag_abs_val(B)
    print ("n_step=",n_step,", non_diag_max=",non_diag_max )

# 結果の表示
print()
print("eigen_vectors",R.T)
print("eigen values = ", np.diag(B))