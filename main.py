#coding:utf-8
from __future__ import division
from sources import affichage, bem, bemf, geometry
import numpy as np
import matplotlib.pyplot as plt
from time import time

points,elements = geometry.import_gmsh('rough_1_s.msh')
    
source = np.array([2,3])
n,(x,y) = geometry.compute_normal(elements,points,source)
f = 600
omega = 2*np.pi*f

ps,r = bemf.resolution_pression_surface(points,elements,n,source,omega)
#%%
res = 100
#Discrétisation du domaine Omega
x = np.linspace(0,4,res)
y = np.linspace(-2,2,res)

xx,yy = np.meshgrid(x,y)

xx = xx.reshape(res*res)
yy = yy.reshape(res*res)
zz = zip(xx,yy)

#%%
def test():
    global a
    a = []
    for elm in zz:
        a.append(bem.calcul_pression_source_ponctuelle(elm,r,ps,source,1,elements,points,n,omega))
    a = np.array(a)
    #%%
def test2():
    global a
    a = bemf.calcul_pression_omega(zz,r,ps,source,elements,points,n,omega)
def show():
    plt.imshow(np.real(a.reshape([res,res])),vmin=-.3,vmax=.3)
    plt.colorbar()
    plt.show()
