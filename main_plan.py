#coding:utf-8
from __future__ import division
from sources import bemf,geometry,affichage
from sources.timeit import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

#On vérifie combien de processeurs sont disponibles
print "{} processeur(s) disponible(s)".format(bemf.check_core())

#Création de la géométrie
points,elements = geometry.rough_1_s(.5,1,200)

#Définition des paramètres du problème
source = np.array([-20,20]) #Position de la source
n,(x,y) = geometry.compute_normal(elements,points,[0,100]) #Calcul des normales
f = 400 #Définition de la fréquence d'émission
omega = 2*np.pi*f #Conversion en fréquence angulaire
angle = -np.pi/8.

#On affiche la configuration
affichage.show_all(points,n,x,y,source)

#On récupère les matrices A,B et les centres des élements
A,B,r = timeit(bemf.get_ab_plan)(points,elements,n,source,angle,omega)

#On résout la pression à la surface
ps = solve(.5*np.eye(len(A)) + A, B)

#Discrétisation du domaine Omega
axis = [-5,5,-2,8]
zz,res = geometry.discretisation_omega(axis,200)

#Calcul de la pression en tout point de la discrétisation de OMEGA
pression = timeit(bemf.pression_omega_plan)(zz,r,ps,source,angle,elements,points,n,omega)
    
#Affichage de la cartographie
affichage.cartographie(pression,res,axis,points)

#Discrétisation d'un cercle
cercle,theta = geometry.discretisation_cercle([0,0],2,1000)

#Calcul de la directivité de la configuration
directivite = bemf.pression_omega(cercle,r,ps,source,elements,points,n,omega)

#Afichage de la directivité
affichage.polar_plot(directivite,theta)