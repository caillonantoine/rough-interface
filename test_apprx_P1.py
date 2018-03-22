#coding:utf-8
from os import system as cmd
cmd('cd modules && make')
import numpy as np
from modules import get_ab,geometry,affichage,bemf
import matplotlib.pyplot as plt
from scipy.linalg import solve

points, elements = geometry.rough_1_s(.5, .5, 200, 3)
n,(x,y) = geometry.compute_normal(elements, points, [0,100])
source = [-1,5]

affichage.show_all(points, n, x, y,source=source)

omega = 2*np.pi*600

A,B = bemf.get_ab(points, elements, n, source, omega)

#%%
zz,res = geometry.discretisation_omega([-5,5,-5,5],150)
angles = get_ab.compute_angles(points,elements)/(2*np.pi)
ps = solve(np.diag(angles) + A,B)
#ps = solve(.5*np.eye(len(points)) + A,B)


#%%

pression = bemf.pression_omega(zz,ps,points,elements,n,source,omega)

pression = pression.reshape([res,res])

#%%

amplitude = .08
plt.imshow(np.real(pression),interpolation='bicubic',origin='lower',vmin=-amplitude,vmax=amplitude)
plt.colorbar()

