import numpy as np
from scipy.special import hankel1

def gradgreen(x1,x2,k,n):
	R = np.linalg.norm(x1-x2)
	if R != 0:
		return np.dot(1j/(4*R)*hankel1(1, k*R)*(x1-x2),n)
	else:
		return 0+0j
	
def green(x1,x2,k):
	R = np.linalg.norm(x1-x2)
	return -1j/4. * hankel1(0,k*R)
	
def pression(zz,points,elements,normales,source,omega):
	pass


def get_ab(points,elements,normales,source,omega):
	"""Implémentation de BEM GALLERKIN"""
	k = omega/340.

	m = len(elements)
	n = len(points)

	A = np.zeros([n,n],dtype=complex)
	B = np.zeros([n,1],dtype=complex)

	for j in range(m):
		a,b = elements[j]
		milieu = (points[a]+points[b])/2
		aire = np.linalg.norm(points[a] - points[b])

		for i in range(n):
			A[i,a] += aire*(gradgreen(points[i],points[a],k,normales[j])\
				+ 2*gradgreen(points[i],milieu,k,normales[j]))
			A[i,b] += aire*(gradgreen(points[i],points[b],k,normales[j])\
				+ 2*gradgreen(points[i],milieu,k,normales[j]))
	A /= 6
	
	for i in range(n):
		B[i] = green(points[i],source,k)
		
	return A,B