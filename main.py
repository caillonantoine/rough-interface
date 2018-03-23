#coding:utf-8
import numpy as np
from modules import rough_interface as ri


#Une simplification du code a été effectuée afin de rester concentré sur les resultats
#plutôt que sur les aspects programmation.


problem = ri.RoughInterfaceScattering() #On crée le problème

problem.create_interface('s_sinusoidale', .25, 340/200., 1000, 13)
problem.set_source('plane', [-1,3])
problem.set_angle(np.pi/3)
problem.set_frequency(200)
problem.set_omega([-5,5,-1,9], 150, 2)
problem.set_circle(7,[0,.5])

pression, directivite = problem.start()