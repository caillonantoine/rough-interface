#coding:utf-8
from __future__ import division
from os import system as cmd
cmd("./compile.sh") #On compile le module fortran si ce n'est pas fait
from fortran import bemf
from modules import geometry,affichage
from modules.timeit import timeit
import matplotlib.pyplot as plt
import numpy as np

#Définition des paramètres de l'étude
pas = 8

taille_l,taille_h = .1,.1

largeur = np.linspace(.01,taille_l,pas)
hauteur = np.linspace(.01,taille_h,pas)

#Définition des paramètres de la configuration
source = np.array([-20,20]) #Position de la source
f = 200 #Définition de la fréquence d'émission
omega = 2*np.pi*f #Conversion en fréquence angulaire
angle = -np.pi/3. #Angle d'incidence de l'onde plane

resultats = []

for i,l in enumerate(largeur):
	for j,h in enumerate(hauteur):
		print "Calcul de ({},{})".format(h,l)
		points,elements = geometry.rough_1_s(h,l,500,8)
		n,(x,y) = geometry.compute_normal(elements,points,[0,100]) #Calcul des normales 
		A,B,r = bemf.get_ab_plan(points,elements,n,source,angle,omega)
		#resolution
		ps = B
		bemf.solve_ps(A,ps)
		#Discrétisation d'un cercle
		cercle,theta = geometry.discretisation_cercle([0,.1],2,1000)

		#Calcul de la directivité de la configuration
		directivite = bemf.pression_omega(cercle,r,ps,source,elements,points,n,omega)
		directivite = abs(directivite)
		directivite = (directivite - np.mean(directivite))/1000
		resultats.append(sum(abs(directivite)))
		
		#On désalloue la mémoire pour éviter les erreurs
		
		points = None
		elements = None
		n = None
		A = None
		B = None
		r = None
		ps = None
		directivite = None
#%%
resultats = np.array(resultats)
resultats = resultats.reshape([pas,pas])
plt.imshow(resultats,interpolation='bicubic',extent=[0,taille_l,0,taille_h],origin='lower')
plt.colorbar()
plt.xlabel('largeur')
plt.ylabel('hauteur')
plt.title('Evolution de l\'erreur en fonction de la singularite')
plt.show()