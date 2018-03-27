#coding:utf-8
import numpy as np
from modules import rough_interface as ri


problem = ri.RoughInterfaceScattering() #On crée le problème

problem.create_interface('s_sinusoidale', .31, 340/200., 1000, 13)
problem.set_source('plane', [-1,3])
problem.set_angle(30*np.pi/180.)
problem.set_frequency(200)
problem.set_omega([-5,5,-1,9], 150, 2)
problem.set_circle(7,[0,.5])

angles = np.array([25,27,30,33,35]) #Définition des angles
pression = []

#%%

for angle in angles:
	print("Calcul de la pression pour un angle de {}".format(angle))
	problem.set_angle(angle*np.pi/180.)
	pression.append(problem.start(quiet=True)[0])
	
#%%

hauteur = np.linspace(.25,.35,6)

for h in hauteur:
	print("Calcul de la pression pour une hauteur de {}".format(h))
	problem.create_interface('s_sinusoidale',h,1.7,600,13)
	pression.append(problem.start(quiet=True)[0])
#%%
import matplotlib.pyplot as plt
for i,o in enumerate(pression):
	plt.subplot(2,3,i+1)
	plt.imshow(abs(o.reshape([problem.res,problem.res])),origin='lower',\
			extent=problem.extent,interpolation='bicubic',vmin=0,vmax=2)
	plt.title('Angle d\'incidence = {}'.format(angles[i]))
	plt.colorbar()
plt.suptitle('Comparaison de la reflexion pour plusieurs angles d\'incidence')
plt.tight_layout()
plt.show()
#%%
import matplotlib.pyplot as plt
for i,o in enumerate(pression):
	plt.subplot(2,3,i+1)
	plt.imshow(abs(o.reshape([problem.res,problem.res])),origin='lower',\
			extent=problem.extent,interpolation='bicubic',vmin=0,vmax=2)
	plt.title('Hauteur = {}'.format(hauteur[i]))
	plt.colorbar()
plt.suptitle('Comparaison de la reflexion pour plusieurs hauteur d\'interface')
plt.tight_layout()
plt.show()
