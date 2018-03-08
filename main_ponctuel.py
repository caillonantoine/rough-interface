#coding:utf-8
from __future__ import division
from os import system as cmd
cmd("./compile.sh") #On compile le module fortran si ce n'est pas fait
from fortran import bemf
from modules import geometry,affichage
from modules.timeit import timeit
import matplotlib.pyplot as plt
import numpy as np

cmd("./compile.sh") #On compile le module fortran si ce n'est pas fait

affichage.introduction('sphérique',bemf.check_core())

#Création de la géométrie
points,elements = geometry.rough_1_s(1,2,300,10)
n,(x,y) = geometry.compute_normal(elements,points,[0,100]) #Calcul des normales

#Définition des paramètres du problème
source = np.array([-2,3]) #Position de la source
f = 500 #Définition de la fréquence d'émission
omega = 2*np.pi*f #Conversion en fréquence angulaire

#On affiche la configuration
affichage.show_all(points,n,x,y,source)

#On récupère les matrices A,B et les centres des élements
A,B,r = timeit(bemf.get_ab)(points,elements,n,source,omega)

#On résout la pression à la surface
#ps = solve(.5*np.eye(len(A)) + A, B)
ps = B
bemf.solve_ps(A,ps)

#Discrétisation du domaine Omega
axis = [-5,5,-2,8]
zz,res = geometry.discretisation_omega(axis,200)

#Calcul de la pression en tout point de la discrétisation de OMEGA
pression = timeit(bemf.pression_omega)(zz,r,ps,source,elements,points,n,omega)
    
#Affichage de la cartographie
affichage.cartographie(pression,res,axis,points,amplitude=.2)

#Discrétisation d'un cercle
cercle,theta = geometry.discretisation_cercle([0,0],5,1000)

#Calcul de la directivité de la configuration
directivite = bemf.pression_omega(cercle,r,ps,source,elements,points,n,omega)

#Afichage de la directivité
affichage.polar_plot(directivite,theta)