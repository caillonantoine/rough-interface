#coding:utf-8
import numpy as np
from scipy.special import hankel1
import matplotlib.pyplot as plt

def show():
    """Affiche la configuration"""
    global points,s0
    plt.plot(points[:,0],points[:,1])
    plt.axis('equal')
    #plt.axis([-2,7,-4.5,4.5])
    plt.scatter(*s0)
    for passe in si:
        for elm in passe:
            plt.scatter(*elm)
    plt.grid()
    plt.show()
        
def sym(s,a,b):
    """Donne les coordonnées du symétrique d'un point s par rapport au segment [a,b]"""
    s,a,b = np.asarray(s),np.asarray(a),np.asarray(b)
    h = (np.dot(s-a,b-a)/np.linalg.norm(b-a)**2)*(b-a) + a
    return (2*h -s)

def Green(r,k0):
    """Fonction de green correspondant à toutes les sources images"""
    global si
    y = 0
    for i in range(1,len(si)):
        for elm in si[i]:
            y += G(r,np.array(elm),k0)
    return y

H1 = lambda z:hankel1(0,z)

G = lambda r,r0,k0: (1/4j)*H1(k0*np.linalg.norm(r-r0))

N = 4
points = np.asarray([[0,0],[1,0],[1,1],[0,1]]) #Définition des points de la frontière
plans = np.asarray([[i%N,(i+1)%N] for i in range(N)]) #Définition des segments entre chaque points

s0 = np.asarray([.25,.5]) #Positionnement de la source

n = 3 #Nombre de passes de réflexion
si = [0 for i in range(n)] #Liste de liste de points
si[0] = [s0]

for i in range(1,n): #Calcul des sources n-ième
    si[i] = []
    for source in si[i-1]:
        for plan in plans:
            symetrique = sym(source, points[plan[0]],points[plan[1]])
            if not (True in [(symetrique == elm).all() for elm in si[i-1]]):
                si[i].append(symetrique)

#%% BEM







