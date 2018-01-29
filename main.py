#coding:utf-8
import numpy as np
from scipy.special import hankel1
import matplotlib.pyplot as plt

def show():
    """Affiche la configuration"""
    global points,s0
    plt.plot(points[:,0],points[:,1])
    plt.axis('equal')
    plt.scatter(*s0)
    for passe in si:
        for elm in passe:
            plt.scatter(*elm)
    plt.grid()
        
def sym(s,a,b):
    """Donne les coordonnées du symétrique d'un point s par rapport au segment [a,b]"""
    s,a,b = np.asarray(s),np.asarray(a),np.asarray(b)
    h = (np.dot(s-a,b-a)/np.linalg.norm(b-a)**2)*(b-a) + a
    return (2*h -s)

def Green(r,k0):
    global si
    y = 0
    for i in range(1,len(si)):
        for elm in si[i]:
            y += G(r,np.array(elm),k0)
    return y

H1 = lambda z:hankel1(0,z)

G = lambda r,r0,k0: (1/4j)*H1(k0*np.linalg.norm(r-r0))


points = np.asarray([[i,.5*np.sin(3*i)] for i in np.linspace(0,5,10)]) #Définition des points de la frontière
plans = np.asarray([[i,(i+1)] for i in range(9)]) #Définition des segments entre chaque points

s0 = np.asarray([2.5,2]) #Positionnement de la source

n = 2 #Nombre de passes de réflexion
si = [0 for i in range(n)] #Liste de liste de points
si[0] = [s0]

for i in range(1,n): #Calcul des sources n-ième
    si[i] = []
    for source in si[i-1]:
        for plan in plans:
            si[i].append(sym(source, points[plan[0]],points[plan[1]]))
















