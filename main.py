#coding:utf-8
import numpy as np
import rough_interface as ri
from scipy.optimize import minimize as mini
import matplotlib.pyplot as plt

#%%

#Une simplification du code a été effectuée afin de rester concentré sur les resultats
#plutôt que sur les aspects programmation.


problem = ri.RoughInterfaceScattering() #On crée le problème
lam = 1.7
problem.create_interface('s_unique', 0*lam, .5*lam, 1500, 30)
problem.set_source('plane', [-1,3])
problem.set_angle(np.pi/3)
problem.set_frequency(200)
problem.set_omega([-5,5,0,10], 150, 2)
problem.set_circle(2,[0,.5])

p_plane, directivite = problem.start(quiet=True)

#%%
evolution = []

for a in np.linspace(0.005,.5,40):
	problem.create_interface('s_aleatoire',a*lam,a*lam,1500,30)
	p_pert , d = problem.start(quiet = True)
	
	p_plane = p_plane.reshape([150,150])
	p_pert = p_pert.reshape([150,150])
	
	p1 = p_plane[5:,:]
	p2 = p_pert[5:,:]
	
	coef = mini(lambda x: np.sqrt(np.mean(np.power(abs(x*p2 - p1),2))),1).x
	norm = np.sqrt(np.mean(np.power(abs(p1),2)))
	
	erreur = np.sqrt(np.mean(np.power(abs(coef*p2 - p1),2)))
	
	
	print "erreur = {}%".format(100*erreur/norm)
	print "coef   = {}".format(coef[0])
	evolution.append((erreur,coef))
#%%

evolution = np.array(evolution)
plt.plot(np.linspace(.005,.5,40)[0:33],evolution)
ref = np.linspace(.005,.5,40)[0:33]
plt.legend(['erreur','coef'])
plt.grid()
