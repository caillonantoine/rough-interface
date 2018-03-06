#coding:utf-8
from __future__ import division
from sources import geometry, bemf
from scipy.linalg import solve
import matplotlib.pyplot as plt
import numpy as np

points, elements = geometry.rough_p_s(.25,.5,200,10)

source = np.array([0,3])
n,(x,y) = geometry.compute_normal(elements,points,[0,10])

fe = 1000
freq = np.linspace(0,fe/2,int(fea))
freq[0] = 1

echo = []

micro = np.array([2,3])

for i,elm in enumerate(freq):
    print i*100/len(freq)
    A,B,r = bemf.get_ab(points,elements,n,source,2*np.pi*elm)
    ps = solve(.5*np.eye(len(A)) + A , B)
    echo.append(bemf.pression_omega([micro],r,ps,source,elements,points,n,elm))
    