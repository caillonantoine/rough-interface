#coding:utf-8
from __future__ import division
from os import system as cmd
cmd("./compile.sh") #On compile le module fortran si ce n'est pas fait
from fortran import bemf
from modules import geometry,affichage
from modules.timeit import timeit
import matplotlib.pyplot as plt
import numpy as np

affichage.introduction('plane',bemf.check_core())

#Création de la géométrie
points,elements = geometry.rough_1_s(0.5,.5,1600,16)
n,(x,y) = geometry.compute_normal(elements,points,[0,100]) #Calcul des normales

#Définition des paramètres du problème
source = np.array([-20,20]) #Position de la source
f = 200 #Définition de la fréquence d'émission
omega = 2*np.pi*f #Conversion en fréquence angulaire
angle = -np.pi/3. #Angle d'incidence de l'onde plane

#On affiche la configuration
affichage.show_all(points,n,x,y,source)

#On récupère les matrices A,B et les centres des élements
A,B,r = timeit(bemf.get_ab_plan)(points,elements,n,source,angle,omega)

#On résout la pression à la surface
ps = B
bemf.solve_ps(A,ps)

#Discrétisation du domaine Omega
axis = [-5,5,-2,8]
zz,res = geometry.discretisation_omega(axis,150)

#Calcul de la pression en tout point de la discrétisation de OMEGA
pression = timeit(bemf.pression_omega_plan)(zz,r,ps,source,angle,elements,points,n,omega)
    
#Affichage de la cartographie
affichage.cartographie(pression,res,axis,points,amplitude=1)

#Discrétisation d'un cercle
cercle,theta = geometry.discretisation_cercle([0,.1],1,1000)

#Calcul de la directivité de la configuration
directivite = bemf.pression_omega(cercle,r,ps,source,elements,points,n,omega)

#Afichage de la directivité
affichage.polar_plot(directivite,theta)
