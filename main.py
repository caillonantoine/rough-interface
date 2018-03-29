#coding:utf-8
#!/usr/bin/env python
import numpy as np
import rough_interface as ri
from scipy.optimize import minimize as mini
import matplotlib.pyplot as plt


problem = ri.RoughInterfaceScattering() #On crée le problème
lam = 1.7
problem.create_interface('s_aleatoire', .5*lam, .5*lam, 300, 5)
problem.set_source('plane', [-1,3])
problem.set_angle(np.pi/3)
problem.set_frequency(200)
problem.set_omega([-5,5,0,10], 150, 2)
problem.set_circle(2,[0,.5])

p_plane, directivite = problem.start(quiet=True)