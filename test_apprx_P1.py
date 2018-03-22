#coding:utf-8
from os import system as cmd
cmd('cd modules && make')
import numpy as np
from modules import get_ab,geometry,affichage,bemf
import matplotlib.pyplot as plt
from scipy.linalg import solve

points, elements = geometry.rough_1_s(.5, .1, 100, 10)
n,(x,y) = geometry.compute_normal(elements, points, [0,100])
source = [0,5]

affichage.show_all(points, n, x, y,source=source)

omega = 2*np.pi*600

A,B = get_ab.get_ab(points, elements, n, source, omega)

#%%
zz,res = geometry.discretisation_omega([-5,5,-5,5],50)
angles = get_ab.compute_angles(points,elements)/(2*np.pi)
ps = solve(np.diag(angles) + A,B)

#%%

pression = get_ab.pression(zz,ps,points,elements,n,source,omega)

pression = pression.reshape([res,res])

#%%

amplitude = .02
plt.imshow(np.real(pression),interpolation='bicubic',origin='lower',vmin=-amplitude,vmax=amplitude)
plt.colorbar()

