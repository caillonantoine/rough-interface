#coding: utf-8
import numpy as np
from modules import rough_interface as ri

lam = 1

problem = ri.RoughInterfaceScattering()
trou= .3*lam

e =  .25*lam
f = e + 1.5*lam
g = .5*lam + f
h = 50

d,c,b,a = -e,-f,-g,-h

points = zip(np.concatenate([np.linspace(a,b,500),\
						 np.linspace(c,d,100),\
						 np.linspace(e,f,100),\
						 np.linspace(g,h,500)]),np.zeros(1200))
elements = np.concatenate([[(i,i+1) for i in range(499)],\
							[(i,i+1) for i in range(500,599)],\
							[(i,i+1) for i in range(600,699)],\
							[(i,i+1) for i in range(700,1199)]])

points = np.asarray(points)
elements = np.asarray(elements)


problem.set_interface(points,elements)
problem.set_source('plane',[0,5*lam])
problem.set_angle(0)
problem.set_omega([-10*lam,10*lam,-10*lam,10*lam],150,.5)
problem.set_frequency(lam*340)
problem.set_circle(2,[0,1])

pression, directivite = problem.start(quiet = True)

#%%
import matplotlib.pyplot as plt

amplitude = .5
plt.imshow(np.real(pression.reshape([problem.res,problem.res])),extent=problem.extent,origin='lower',interpolation='bicubic',\
		   vmin=-amplitude,vmax=amplitude,cmap='hot')
plt.savefig('validation_ris.eps')

#%%

ligne = zip(np.linspace(-10,10,1000),-5*np.ones(1000))

problem.cercle = ligne
p,l = problem.start(quiet=True)
