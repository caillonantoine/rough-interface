#coding:utf-8
from __future__ import division
import numpy as np
from numpy.linalg import norm,solve
from scipy.special import hankel1
import matplotlib.pyplot as plt
from mshloader import load

def Green(r,r0,k):
    r,r0 = np.asarray(r),np.asarray(r0)
    R = norm(r-r0)
    return -1j/4 * hankel1(0,k*R)

def deltaGreen(r,r0,k):
    r,r0 = np.asarray(r),np.asarray(r0)
    R = norm(r-r0)
    return 1j/4 * k * hankel1(1,k*R) * (r-r0)/R

def compute_normal(elements,points,centre):
    """Calcule les normales orientées vers centre de tous les elements"""
    n = []
    x = []
    y = []
    centre = np.asarray(centre)
    for i,o in enumerate(elements):
        a,b = points[o]
        u = b-a
        v = centre-a
        n.append(v - np.dot(u,v)/(np.power(norm(u),2))*u)
        n[-1] = n[-1]/norm(n[-1])
        x.append((a[0]+b[0])/2)
        y.append((a[1]+b[1])/2)
    return -1*np.asarray(n),np.asarray([x,y])

def show(points,source):
    """Affiche dans un plot tous les points contenus dans points"""
    plt.scatter(*source)
    plt.plot(points[:,0],points[:,1],'.')
    plt.axis('equal')
    
def show_all(points,n,x,y,source=None):
    """Affiche toute la configuration, y compris les normales aux élements"""
    show(points,source)
    plt.quiver(x,y,n[:,0],n[:,1],width=0.005)
    
def get_AB(points,elements,normal,source,amplitude,omega,beta,c=340):
    """Renvoie les matrices A et B en fonction de:
        -points
        -elements
        -normales aux elements
        -position de la source
        -amplitude (et phase si complex) de la source
        -pulsation
        -coefficient d'absorption de la frontière
        -vitesse des ondes sonores dans le milieu"""
    k = omega / c
    N = len(elements)
    A = np.zeros([N,N],dtype=complex)
    B = np.zeros([N,1],dtype=complex)
    r = []
    for i,o in enumerate(elements):
        a,b = points[o]
        r.append((a+b)/2)
        for j,elm_j in enumerate(elements):
            if i==j:
                A[i,j] = 0 + 0j
            else:
                a,b = points[elm_j]
                rj = (a+b)/2
                aire = norm(a-b)
                A[i,j] = aire*(np.dot(deltaGreen(r[i],rj,k),normal[j]))
        B[i] = amplitude*Green(r[i],source,k)
    return A,B,r
        
def p(x,r,ps,source,amplitude,elements,points,normal,omega,beta,c=340):
    """implémentation de l'équation (14)"""
    k = omega/c
    x = np.asarray(x)
    y = amplitude*Green(x,source,k)
    y = 0
    for i,o in enumerate(elements):
        a,b = points[o]
        aire = norm(b-a)
        n = normal[i]
        y -= ps[i] *aire*(np.dot(deltaGreen(x,r[i],k),n)) #vectoriser
    return y
    
#On définit les paramètres du problème
points,elements = load('/home/antoine/untitled.msh')
source = np.array([2,3])
f = 500
omega = 2*np.pi*f
beta=0

#On calcul les normales de chaque élement
n,(x,y) = compute_normal(elements,points,source)

#...Puis on affiche la configuration
print 'Affichage de la configuration'
show_all(points,n,x,y,source)
plt.show()

a = raw_input('Appuyez sur une touche pour lancer le calcul...')
print 'Création des matrices'
#Création des matrices et du vecteur pression
A,B,r = get_AB(points,elements,n,source,1,omega,0)
#Calcul de la pression en tout point de la surface
print 'Résolution'
ps = solve(.5*np.eye(len(elements))+A,B)

print 'Calcul'
res = 60

extent = [-2,6,-2,6]

x = np.linspace(extent[0],extent[1],res)
y = np.linspace(extent[2],extent[3],res)
z = np.zeros([res,res],dtype=complex)

for i in range(res):
    for j in range(res):
        z[i,j] = p([x[i],y[j]],r,ps,source,1,elements,points,n,omega,beta)
print 'Affichage'
#%%
plt.scatter(source[1],source[0],c='w')
plt.imshow(np.real(z),extent=extent,origin='lower',vmin=-.2,vmax=.2,cmap='Blues')
plt.plot(points[:,1],points[:,0],'w.')
plt.axis(extent)
plt.colorbar()
plt.show()

plt.scatter(source[1],source[0],c='w')
plt.imshow(abs(z),extent=extent,origin='lower',cmap='autumn')
plt.plot(points[:,1],points[:,0],'w.')
plt.axis(extent)
plt.colorbar()
plt.show()
