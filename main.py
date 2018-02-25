#coding:utf-8
from __future__ import division
from sources import affichage, bem, bemf, geometry
from scipy.linalg import solve
import numpy as np
import matplotlib.pyplot as plt
from time import time

points,elements = geometry.import_gmsh('/home/antoine/untitled.msh')

#points = np.asarray(zip(np.linspace(0,5,100),np.zeros(100)))
#elements = np.array([[i,i+1] for i in range(99)])
   
source = np.array([2,3])
n,(x,y) = geometry.compute_normal(elements,points,source)
f = 600
omega = 2*np.pi*f

affichage.show_all(points,n,x,y,source)

A,B,r = bemf.get_ab(points,elements,n,source,omega)

#B = solve(.5*np.eye(len(A)) + A, B)
bemf.solve_pression(A,B)
res = 100
#Discrétisation du domaine Omega
x = np.linspace(-2,6,res)
y = np.linspace(-4,4,res)

xx,yy = np.meshgrid(x,y)

xx = xx.reshape(res*res)
yy = yy.reshape(res*res)

zz = zip(xx,yy)
z = zip(x,np.zeros(len(x)))

pression = bem.pression_omega(zz,B,source,elements,points,n,omega,r)

plt.imshow(np.real(pression.reshape([res,res])),origin='lower')
plt.colorbar()
plt.show()
