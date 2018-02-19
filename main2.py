#coding:utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
from scipy.linalg import solve
from time import time
from mshloader import load

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
    
def p(x):
    """Calcule la pression en n'importe quel point du domaine."""
    global ps,N,source,k0,points,surfaces,beta
    x = np.asarray(x)
    y = G(x,source,k0)
    for j in range(M):
        a,b = points[surfaces[j]]
        y -= ps[j] * ((1j)*k0*beta*trap(G,a,b,x,k0) + trap(Gd,a,b,x,k0))
    return y
    
    
#DEFINITION DES PARAMETRES DU PROBLEME
w0 = 2*np.pi*900 #Fréquence angulaire
c0 = 340 #Vitesse du son
p_0 = 1 #Masse volumique du fluide
k0 = w0/c0
alpha = 1 #Amplitude et phase de la source

source = np.array([4,3])

#CREATION DE L'INTERFACE
points,surfaces = load('rough_1_s.msh')
N = len(points)
M = len(surfaces)
#COEFFICIENT D'ABSORBTION DE L'INTERFACE
beta = 1000
#RESOLUTION DE LA PRESSION A LA SURFACE
print "Construction de la matrice de résolution..."
As = np.zeros([M,M],dtype=complex)
r = []
for i in range(M):
    r0 = (points[surfaces[i][0]]+points[surfaces[i][1]])/2
    r.append(r0)
    for j in range(M):
        a,b = points[surfaces[j]]
        As[i,j] = 1j*k0*beta*trap(G,a,b,r0,k0) + trap(Gd,a,b,r0,k0)

print "Résolution..."
r = np.asarray(r)
ps = solve(.5*np.eye(M) + As,[alpha*G(ri,source,k0) for ri in r])

#RESOLUTION DE L'IMAGE EN SORTIE
res = 70

print "Calcul de la pression sur un domaine de {}x{} points...".format(res,res)

extent = [-1,6,-1,6]
x = np.linspace(extent[0],extent[1],res)
y = np.linspace(extent[2],extent[3],res)
z = np.zeros([res,res],dtype=complex)
for i in range(res):
    for j in range(res):
        z[i,j] = p([x[i],y[j]])
        
duration = time() - start
#%%
print "Fini!"
print "La simulation a pris {}s".format(int(duration))
plt.subplot(1,2,1)
plt.imshow(np.real(z),cmap='winter',extent=extent,origin='lower')
plt.plot(points[:,1],points[:,0],'r.')
plt.axis(extent)
plt.savefig('test.png')
plt.title('Partie reelle')
plt.subplot(1,2,2)
plt.imshow(np.abs(z),cmap='winter',extent=extent,origin='lower')
plt.plot(points[:,1],points[:,0],'r.')
plt.axis(extent)
plt.title('Module')
plt.show()
