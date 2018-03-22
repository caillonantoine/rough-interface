#coding:utf-8
from os import system as cmd
cmd('cd modules && make')
import numpy as np
from modules import get_ab,geometry,affichage,bemf
import matplotlib.pyplot as plt
from scipy.linalg import solve

points, elements = geometry.rough_1_s(.5, .5, 100, 3)
n,(x,y) = geometry.compute_normal(elements, points, [0,100])
source = [0,5]

affichage.show_all(points, n, x, y,source=source)

omega = 2*np.pi*400

A,B = get_ab.get_ab(points, elements, n, source, omega)

#%%
zz,res = geometry.discretisation_omega([-5,5,-5,5],50)

ps = solve(.5*np.eye(len(points)) + A,B)

#%%

pression = get_ab.pression(zz,ps,points,elements,n,source,omega)

pression = pression.reshape([res,res])

plt.imshow(np.real(pression),interpolation='bicubic',origin='lower')
plt.colorbar()

