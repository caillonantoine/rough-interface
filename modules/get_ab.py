#coding:utf-8
from __future__ import division
import numpy as np
from scipy.special import hankel1

def gradgreen(x1,x2,k,n):
	x1 = np.asarray(x1)
	x2 = np.asarray(x2)
	R = np.linalg.norm(x1-x2)
	if R != 0:
		return np.dot(1j/(4*R)*k*hankel1(1, k*R)*(x1-x2),n)
	else:
		return 0+0j
	
def green(x1,x2,k):
	x1 = np.asarray(x1)
	x2 = np.asarray(x2)
	R = np.linalg.norm(x1-x2)
	return -1j/4. * hankel1(0,k*R)
	
def pression(zz,ps,points,elements,normales,source,omega):
	zz = np.asarray(zz)
	points = np.asarray(points)
	elements = np.asarray(elements)
	normales = np.asarray(normales)
	ps = np.asarray(ps)
	
	yy = np.zeros(len(zz),dtype=complex)
	k = omega/340.
	
	for i,o in enumerate(zz):
		yy[i]  = green(o,source,k)
		for j,elm in enumerate(elements):
			a,b = elm
			taille = np.linalg.norm(points[a] - points[b])
			milieu = (points[a] + points[b])/2
			yy[i] -= taille*(ps[a]*(1/6. *gradgreen(o,points[a],k,normales[j]) + \
									 1/3. *gradgreen(o,milieu,k,normales[j])))
			yy[i] -= taille*(ps[b]*(1/6. *gradgreen(o,points[b],k,normales[j]) + \
									 1/3. *gradgreen(o,milieu,k,normales[j])))
	return yy


def get_ab(points,elements,normales,source,omega):
	"""Implémentation de BEM GALLERKIN"""
	k = omega/340.

	m = len(elements)
	n = len(points)

	ksi = np.zeros([n,n],dtype=complex)
	beta = np.zeros([n,1],dtype=complex)
	
	for i in range(n):
		for j in range(m):
			a,b = elements[j]
			taille = np.linalg.norm(points[b] - points[a])
			ksi[i,a] += taille*(1/6. * gradgreen(points[i],points[a],k,normales[j]) +\
							1/3. * gradgreen(points[i],(points[a]+points[b])/2,k,normales[j]))
			ksi[i,b] += taille*(1/6. * gradgreen(points[i],points[b],k,normales[j]) +\
							1/3. * gradgreen(points[i],(points[a]+points[b])/2,k,normales[j]))
		beta[i] = green(points[i],source,k)
	return ksi,beta
		
		
		
		
		
		
		
		
		
		