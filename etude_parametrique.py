#coding:utf-8
from __future__ import division
from os import system as cmd
cmd("./compile.sh") #On compile le module fortran si ce n'est pas fait
from fortran import bemf
from modules import geometry,affichage
from modules.timeit import timeit,ProgressBar
import matplotlib.pyplot as plt
import numpy as np

#Définition des paramètres de l'étude
pas = 15

taille_l,taille_h = .4,.4

largeur = np.linspace(.001,taille_l,pas)
hauteur = np.linspace(.001,taille_h,pas)

#Définition des paramètres de la configuration
source = np.array([-20,20]) #Position de la source
f = 200 #Définition de la fréquence d'émission
omega = 2*np.pi*f #Conversion en fréquence angulaire
angle = -np.pi/3. #Angle d'incidence de l'onde plane

resultats = []
critere = []

pb = ProgressBar()
pb.set_total(pas*pas)

for i,l in enumerate(largeur):
	for j,h in enumerate(hauteur):
		pb.set_current(i*pas+j)
		points,elements = geometry.rough_1_s(h,l,200,8)
		taille = len(np.nonzero(points[:,1]))
		n,(x,y) = geometry.compute_normal(elements,points,[0,100]) #Calcul des normales 
		A,B,r = bemf.get_ab_plan(points,elements,n,source,angle,omega)
		#resolution
		ps = B
		bemf.solve_ps(A,ps)
		#Discrétisation d'un cercle
		cercle,theta = geometry.discretisation_cercle([0,.1],6,1000)

		#Calcul de la directivité de la configuration
		directivite = bemf.pression_omega(cercle,r,ps,source,elements,points,n,omega)
		directivite = abs(directivite)
		directivite = (directivite - 1)
		resultats.append(sum(abs(directivite))/1000.)

		rms = np.sqrt(sum(np.power(points[:,1],2)))/taille
		if rms < 340/f/np.cos(angle)/8: 
			critere.append(0)
		else:
			critere.append(1)
		#On désalloue la mémoire pour éviter les erreurs
		
		del points
		del elements
		del n
		del A
		del B
		del r
		del ps
		del directivite
#%%
resultats = np.array(resultats).reshape([pas,pas])
critere = np.array(critere).reshape([pas,pas])

plt.imshow(resultats,interpolation='bicubic',extent=[0,taille_l,0,taille_h],origin='lower')
plt.colorbar()
plt.contour(critere,colors='r',extent=[0,taille_l,0,taille_h])
plt.xlabel('largeur')
plt.ylabel('hauteur')
plt.title('Evolution de l\'erreur en fonction de la singularite')
plt.savefig('erreur.eps')
plt.show()