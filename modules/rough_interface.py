#coding:utf-8
import geometry, affichage, bemf
from timeit import timeit, ProgressBar
import numpy as np

class RoughInterfaceScattering(object):
	"""Encapsulation de toutes les fonctions nécessaires à la
	modélisation de la réflexion d'une onde à une interface rugueuse.

	Pour une source ponctuelle, l'usage typique est:
		test = RoughInterfaceScattering()
		test.create_interface('s_unique', .5, .5, 1600, 16)
		test.set_source('ponctuelle', [-1,3])
		test.set_frequency(200)
		test.set_omega([-2,8,-2,8], 150, .1)
		test.set_circle(2,[0,.5])
		test.start()

	Pour une source plance, l'usage typique est:
		test = RoughInterfaceScattering()
		test.create_interface('s_unique', .5, .5, 1600, 16)
		test.set_source('plane', [-1,3])
		test.set_angle(-np.pi/3)
		test.set_frequency(200)
		test.set_omega([-2,8,-2,8], 150, .1)
		test.set_circle(2,[0,.5])
		test.start()"""
	def __init__(self):
		pass

	def create_interface(self,type_interface,h,l,res,size):
		"""Initialise une interface rugueuse. Le type d'interface peut être:
			-s_unique
			-s_periodique
			-s_sinusoidale
			-s_aleatoire
		Et prent en paramètre:
			-h la hauteur de rugosité
			-l la largeur de rugosité
			-res la resolution de l'interface
			-size la taille de l'interface"""
		if type_interface == 's_unique':
			self.points,self.elements = geometry.rough_1_s(h, l, res, size)
		elif type_interface == 's_periodique':
			self.points,self.elements = geometry.rough_p_s(h, l, res, size)
		elif type_interface == 's_sinusoidale':
			self.points,self.elements = geometry.rough_s_s(h, l, res, size)
		elif type_interface == 's_aleatoire':
			self.points,self.elements = geometry.rough_random(h, l, res, size)

		self.rms = np.sqrt(sum(np.power(self.points[:,1],2)))/16
		self.n,(self.x,self.y) = geometry.compute_normal(self.elements,self.points,[0,1000])

	def set_source(self,type_onde,position):
		"""Définit une source pour le problème. On peut choisir entre un type d'onde:
			-plane
			-ponctuelle
		La position est un vecteur de deux points donnant la position dans l'espace de la source"""
		self.type_onde = type_onde
		self.source = np.array(position)

	def set_angle(self,angle):
		"""Définit l'angle d'incidence d'une onde plane"""
		self.angle = angle

	def set_frequency(self,f):
		"""Définit la fréquence de pulsation de la source"""
		self.f = f
		self.omega = 2*np.pi*f

	def set_omega(self,extent,res,amplitude):
		"""Définit les paramètres du domaine d'observation. Les paramètres sont:
			-extent un vecteur de 4 points, [xmin,xmax,ymin,ymax]
			-res la resolution du domaine
			-amplitude l'amplitude représentée"""
		self.extent = extent
		self.res = res
		self.amplitude = amplitude

	def set_circle(self,radius,position):
		"""Discrétise un cercle. radius = rayon, position = vecteur de deux coordonnées du centre du cercle"""
		self.cercle,self.theta = geometry.discretisation_cercle(position,radius,1000)

	def start(self):
		"""Une fois les paramètres entrés, lance la simulation et affiche les différents résultats"""
		affichage.introduction(self.type_onde, bemf.check_core())
		if self.type_onde == 'plane':
			affichage.lisse_ou_pas_lisse(self.rms,self.f,self.angle)
		affichage.show_all(self.points,self.n,self.x,self.y,self.source)
		if self.type_onde == 'plane':
			A,B,r = timeit(bemf.get_ab_plan)(self.points\
											,self.elements\
											,self.n\
											,self.source\
											,self.angle\
											,self.omega)
		elif self.type_onde == 'ponctuelle':
			A,B,r = timeit(bemf.get_ab)(self.points\
										,self.elements\
										,self.n\
										,self.source\
										,self.omega)
		else:
			print('Type d\'onde non compris')
		ps = B
		bemf.solve_ps(A,ps)
		zz,res = geometry.discretisation_omega(self.extent,self.res)
		if self.type_onde == 'plane':
			pression = timeit(bemf.pression_omega_plan)(zz\
														,r\
														,ps\
														,self.source\
														,self.angle\
														,self.elements\
														,self.points\
														,self.n\
														,self.omega)
			directivite = bemf.pression_omega(self.cercle\
												,r\
												,ps\
												,self.source\
												,self.elements\
												,self.points\
												,self.n\
												,self.omega\
												)
		elif self.type_onde =='ponctuelle':
			pression = timeit(bemf.pression_omega)(zz\
													,r\
													,ps\
													,self.source\
													,self.elements\
													,self.points\
													,self.n\
													,self.omega\
													)
			directivite = bemf.pression_omega(self.cercle\
											,r\
											,ps\
											,self.source\
											,self.elements\
											,self.points\
											,self.n\
											,self.omega\
											)
		affichage.cartographie(pression,res,self.extent,self.points,amplitude=self.amplitude)
		affichage.polar_plot(directivite,self.theta)

if __name__ == '__main__':

	test = RoughInterfaceScattering()
	test.create_interface('s_unique', .5, .5, 1600, 16)
	test.set_source('plane', [-1,3])
	test.set_angle(np.pi/3)
	test.set_frequency(200)
	test.set_omega([-2,8,-2,8], 150, 2)
	test.set_circle(2,[0,.5])
	test.start()
