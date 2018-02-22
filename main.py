#coding:utf-8
from sources import affichage, bem, geometry
import numpy as np

points,elements = geometry.import_gmsh('rough_1_s.msh')
source = np.array([2,3])

f = 500
omega = 2*np.pi*f

n,(x,y) = geometry.compute_normal(elements,points,source)

affichage.show_all(points,n,x,y,source)

A,B,r = bem.get_AB(points,elements,n,source,1,omega)

ps = bem.calcul_pression_surface(A,B)

res = 25

extent = [-2,6,-2,6]

x = np.linspace(extent[0],extent[1],res)
y = np.linspace(extent[2],extent[3],res)
z = np.zeros([res,res],dtype=complex)

for i in range(res):
    for j in range(res):
        z[i,j] = bem.calcul_pression_source_ponctuelle([x[i],y[j]],r,ps,source,1,elements,points,n,omega)