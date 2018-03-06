#coding:utf-8
try:
	import bemf, affichage, geometry
	from timeit import timeit
	from scipy.linalg import solve
	import numpy as np 
	import matplotlib.pyplot as plt 
except:
	raise ImportError