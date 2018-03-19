import numpy as np

def get_ab(points,elements,normales,source,omega):
	m = len(elements)
	n = len(points)

	A = np.zeros([n,n])
	B = np.zeros([n,1])

	for j in range(m):
		a,b = elements[j]
		milieu = (points[a]+points[b])/2
		aire = np.linalg.norm(points[a] - points[b])

		for i in range(n):
			A[i,a] += aire*(gradgreen(points[i],points[a]) + 2*gradgreen(points[i],points[milieu]))
			A[i,b] += aire*(gradgreen(points[i],points[b]) + 2*gradgreen(points[i],points[milieu]))