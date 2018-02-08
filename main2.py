#coding:utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
from scipy.linalg import solve
from time import time

start = time()

"""Definition des fonctions de GREEN"""
print "Définition des fonctions de Green..."
H1 = lambda z:ss.hankel1(0,z)
H1d = lambda z:ss.h1vp(0,z)
G = lambda r,r0,k0: (1/4j)*H1(k0*np.linalg.norm(r-r0))
Gd = lambda r,r0,k0:(1/4j)*k0*H1d(k0*np.linalg.norm(r-r0))

def trap(f,a,b,r0,k0):
    """Integration en utilisant la méthode des trapèzes"""
    a = np.asarray(a)
    b = np.asarray(b)
    return np.linalg.norm(b-a)/2*(f(a,r0,k0) + f(b,r0,k0))

def rug(x):
    if (x>=0 and x<=1):
        return [x,0]
    elif (x>1 and x<=2):
        return [x,x-1]
    elif (x>2 and x <=3):
        return [x,-x+3]
    else:
        return [x,0]
        

def rug(x):
    return (x,.0*np.sin(10*x))
    
def p(x):
    """Calcule la pression en n'importe quel point du domaine."""
    #Pour l'instant, le paramètre beta ne fait rien. Je vais donc l'enlever et voir si quelque chose se passe...
    global ps,N,source,k0,points,surfaces,beta
    x = np.asarray(x)
    y = G(x,source,k0)
    for j in range(N-1):
        a,b = points[surfaces[j]]
        y -= ps[j] * ((1j)*k0*beta*trap(G,a,b,x,k0) + trap(Gd,a,b,x,k0))
        #y -= ps[j] * (1j)*k0*beta*trap(G,a,b,x,k0) + trap(Gd,a,b,x,k0)
    return y
    
    
#DEFINITION DES PARAMETRES DU PROBLEME
N = 200 #Nombre de points de discrétisation
w0 = 2*np.pi*200 #Fréquence angulaire
c0 = 340 #Vitesse du son
k0 = w0/c0
alpha = 20 #Amplitude et phase de la source

source = np.array([1,3])

#CREATION DE L'INTERFACE
space = np.linspace(0,4,N)
points = np.asarray([rug(elm) for elm in space])
surfaces = np.asarray([[i,i+1] for i in range(N-1)])

#COEFFICIENT D'ABSORBTION DE L'INTERFACE
beta = 1

#RESOLUTION DE LA PRESSION A LA SURFACE
print "Construction de la matrice de résolution..."
As = np.zeros([N-1,N-1],dtype=complex)
r = []
for i in range(N-1):
    r0 = (points[surfaces[i][0]]+points[surfaces[i][1]])/2
    r.append(r0)
    for j in range(N-1):
        a,b = points[surfaces[j]]
        As[i,j] = 1j*k0*beta*trap(G,a,b,r0,k0) + trap(Gd,a,b,r0,k0)

print "Résolution..."
r = np.asarray(r)
ps = solve(.5*np.eye(N-1) + As,[alpha*G(ri,source,k0) for ri in r])

#RESOLUTION DE L'IMAGE EN SORTIE
res = 100

print "Calcul de la pression sur un domaine de {}x{} points...".format(res,res)
x = np.linspace(-1,5,res)
y = np.linspace(-1,5,res)
z = np.zeros([res,res],dtype=complex)
for i in range(res):
    for j in range(res):
        z[i,j] = p([x[i],y[j]])
        
duration = time() - start

print "Fini!"
print "La simulation a pris {}s".format(duration)
plt.imshow(np.real(z),cmap='winter')
pxlt.colorbar()
plt.show()
