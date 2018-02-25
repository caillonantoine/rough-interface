#coding:utf-8
import bemf

from numpy.linalg import norm,solve
import numpy as np
from scipy.special import hankel1,yn,jn

def Green(r,r0,k):
    """Fonction de Green 2D en fonction de r,r0 et du nombre d'onde k"""
    r,r0 = np.asarray(r),np.asarray(r0)
    R = norm(r-r0)
    return 1/4. * complex(yn(0,k*R),-1*jn(0,k*R))
def deltaGreen(r,r0,k):
    """gradient de la fonction de Green 2D en fonction de r,r0 et
    du nombre d'onde k"""
    r,r0 = np.asarray(r),np.asarray(r0)
    R = norm(r-r0)
    return k*(r-r0)/(4*R)*complex(-1*yn(1,k*R),jn(1,k*R))

def get_AB(points,elements,normal,source,amplitude,omega,c=340):
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

def calcul_pression_surface(A,B):
    """Résout le système A*ps = B"""
    return solve(.5*np.eye(A.shape[0])+A,B)

def calcul_pression_source_ponctuelle(x,r,ps,source,amplitude,elements,points,normal,omega,c=340):
    """implémentation de l'équation (14).
    Prend en paramètre:
        -x:         Point en lequel la pression est calculée
        -r:         liste des centre de tous les elements de la frontière
        -ps:        pression sur chaque element de la frontiere
        -source:    position de la source ponctuelle
        -amplitude: amplitude de la source (complexe ou réelle)
        -elements:  liste des elements
        -points:    liste des points
        -normal:    liste des normales
        -omega:     pulsation
        -c:         vitesse du son dans le milieu"""
    k = omega/c
    x = np.asarray(x)
    y = amplitude*bemf.green(x,source,k)
    #y = 0
    for i,o in enumerate(elements):
        a,b = points[o]
        aire = norm(b-a)
        n = normal[i]
        y -= ps[i] *aire*(np.dot(bemf.gradgreen(x,r[i],k),n)) #vectoriser
    return y

def pression_omega(zz,ps,source,elements,points,n,omega,r):
    y = []
    for elm in zz:
        y.append(calcul_pression_source_ponctuelle(elm,r,ps,source,1,elements,points,n,omega))
    return np.asarray(y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        