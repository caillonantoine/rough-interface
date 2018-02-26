#coding:utf-8
from __future__ import division
from sources import affichage, bemf, geometry
from scipy.linalg import solve
import numpy as np
import matplotlib.pyplot as plt

#Importation de la géométrie


#points,elements = geometry.import_gmsh('rough_1_s.msh')
points,elements = geometry.rough_1_s(.5,1,100)
#Définition des paramètres du problème

source = np.array([2,3]) #Position de la source
n,(x,y) = geometry.compute_normal(elements,points,source) #Calcul des normales
f = 400 #Définition de la fréquence d'émission
omega = 2*np.pi*f #Conversion en fréquence angulaire

#On affiche la configuration
affichage.show_all(points,n,x,y,source)

#On récupère les matrices A,B et les centres des élements
A,B,r = bemf.get_ab(points,elements,n,source,omega)

#On résout la pression à la surface
ps = solve(.5*np.eye(len(A)) + A, B)

#Discrétisation du domaine Omega
zz,res = geometry.discretisation_omega([-1,7,-2,6],200)

#Calcul de la pression en tout point de la discrétisation de OMEGA
pression = bemf.pression_omega(zz,r,ps,source,elements,points,n,omega)

#Affichage de la cartographie
affichage.cartographie(pression,res,[-1,7,-2,6],points)

#Discrétisation d'un cercle
cercle,theta = geometry.discretisation_cercle([2,0],6,1000)

#Calcul de la directivité de la configuration
directivite = abs(bemf.pression_omega(cercle,r,ps,source,elements,points,n,omega))

#Afichage de la directivité
affichage.polar_plot(directivite,theta)