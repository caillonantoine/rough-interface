#coding: utf-8
import numpy as np
import rough_interface as ri
from rough_interface import geometry
import matplotlib.pyplot as plt

lam = 1

problem = ri.RoughInterfaceScattering()

points,elements = geometry.import_gmsh('/home/antoine/untitled.msh')

points = np.asarray(points)
elements = np.asarray(elements)


problem.set_interface(points,elements)
problem.set_source('ponctuelle',[-5,5])
problem.set_angle(0)
problem.set_omega([-10*lam,10*lam,-10*lam,10*lam],150,.1)
problem.set_frequency(lam*340)
problem.set_circle(2,[0,1])

problem.n[167:189] *= -1
problem.n[240:262] *= -1
problem.n[275:297] *= -1
problem.n[346:368] *= -1

pression, directivite = problem.start()

#%%
import matplotlib.pyplot as plt

amplitude = .5
plt.imshow(np.real(pression.reshape([problem.res,problem.res])),extent=problem.extent,origin='lower',interpolation='bicubic',\
		   vmin=-amplitude,vmax=amplitude,cmap='hot')
plt.savefig('validation_ris.eps')

#%%

ligne = zip(np.linspace(-10,10,1000),7.5*np.ones(1000))

problem.cercle = ligne
p,l = problem.start(quiet=True)
