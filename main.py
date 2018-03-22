#coding:utf-8
import numpy as np
from modules import rough_interface as ri


#Une simplification du code a été effectuée afin de rester concentré sur les resultats
#plutôt que sur les aspects programmation.


problem = ri.RoughInterfaceScattering() #On crée le problème
problem.create_interface('s_unique', .5, .5, 500, 16) #On crée l'interface
problem.set_source('plane', [-1,3])
problem.set_angle(-np.pi/3)
problem.set_frequency(200)
problem.set_omega([-20,20,-20,20], 150, 2)
problem.set_circle(2,[0,.5])
problem.start()