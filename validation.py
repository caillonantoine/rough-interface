#coding: utf-8
import numpy as np
from modules import rough_interface as ri

problem = ri.RoughInterfaceScattering()

trou= .1

points = zip(np.concatenate([np.linspace(-50, -trou,500), np.linspace(trou,50,500)]),np.zeros(1000))
elements = np.concatenate(([[i,i+1] for i in range(499)],[[i,i+1] for i in range(500,999)]))


points = np.asarray(points)
elements = np.asarray(elements)


problem.set_interface(points,elements)
problem.set_source('ponctuelle',[0,10])
problem.set_angle(np.pi/2)
problem.set_omega([-10,10,-10,10],150,.01)
problem.set_frequency(200)
problem.set_circle(2,[0,1])
problem.start()