#coding:utf-8
import numpy as np
from scipy.special import hankel1
import matplotlib.pyplot as plt

def d(x,y):
    z = np.zeros(len(x))
    for i in range(len(x)):
        z[i] = np.sqrt(np.power(x[i][0] - y[0],2) + np.power(a,b)(x[i][1] - y[1],2))
    return z

def show():
    global points,s0,s1
    plt.plot(points[:,0],points[:,1])
    plt.axis('equal')
    plt.scatter(*s0)
    for elm in s1:
        plt.scatter(*elm)
        
def sym(s,a,b):
    s,a,b = np.asarray(s),np.asarray(a),np.asarray(b)
    h = (np.dot(s-a,b-a)/np.linalg.norm(b-a)**2)*(b-a) + a
    return 2*h -s
    
    
H1 = lambda z:hankel1(0,z) #Définition de la fonction de Hankel de première espèce et d'ordre 0

G = lambda r,r0,k0: (1/4j)*H1(k0*d(r,r0)) #Définition de la fonction de Green en dimension 2


points = np.asarray([[0,0],[1,0],[.5,1],[0,1]])
plans = np.asarray([[i%4,(i+1)%4] for i in range(4)])

s0 = np.asarray([.5,.5])
si = [[s0]]
#%%
for i in range(2):
    si.append([])
    for j,elm in enumerate(plans):
        for source in si[i]:
            a,b = points[elm[0]], points[elm[1]]
            u = b-a
            sa = source-a
            proj = np.dot(sa,u)/np.linalg.norm(u)
            if proj >= 0 and proj <= 1:
                si[i+1].append(sym(s0,a,b))