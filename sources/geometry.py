#coding:utf-8
from __future__ import division
import numpy as np
from numpy.linalg import norm

def import_gmsh(name):
    """Prend en paramètre le nom du fichier '.msh'
    Renvoie deux vecteurs: les noeuds de la géométrie et les élements.
    N'est compatible qu'avec un meshage 1D"""
    with open(name,'r') as mesh_file:
        mesh = mesh_file.read()
    mesh = mesh.split('$')
    node_liste = mesh[3].split('\n')
    n_node = int(node_liste[1])
    node = []
    for i in range(2,n_node+2):
        temp = node_liste[i].split(' ')
        x,y = float(temp[1]),float(temp[2])
        node.append([x,y])
        
    elm_liste = mesh[5].split('\n')
    n_elm = int(elm_liste[1])
    elm = []
    for i in range(2,n_elm+2):
        temp = elm_liste[i].split(' ')
        x,y = int(temp[-2]),int(temp[-1])
        if int(temp[1]) != 15:
            elm.append([x-1,y-1])
    return np.array(node),np.array(elm)

def rough_1_s(h,l,res):
    """Crée une interface avec une singularité de hauteur h et de longueur l"""
    x = np.linspace(-10,10,res)
    y = np.zeros(res)
    l = l/2
    for i,elm in enumerate(x):
        if elm > -l and elm < l:
            if elm <= 0:
                y[i] = h + elm*h/l
            else:
                y[i] = h - elm*h/l
    return np.array(zip(x,y)),\
                     np.array([[i,i+1] for i in range(len(x)-1)])
                     
def rough_p_s(h,l,res,size):
    """Crée une interface de hauteur h, largeur l, longueur size"""
    x = np.linspace(-size,size,res)
    x_ = np.linspace(-size,size,res)
    y = np.zeros(res)
    for i,elm in enumerate(x):
        elm %= l
        elm -= l/2
        if elm < 0:
            y[i] = h + elm*h/l
        else:
            y[i] = h - elm*h/l
    return np.array(zip(x_,y)),\
                     np.array([[i,i+1] for i in range(len(x_)-1)])
                     
def rough_random(h,res,size):
    x = np.linspace(-size,size,res)
    y = np.random.random(len(x))*h
    return np.array(zip(x,y)),\
                     np.array([[i,i+1] for i in range(len(x)-1)])
    

def compute_normal(elements,points,centre):
    """Calcule les normales orientées vers centre de tous les elements.
    Attention, cette fonction est assez instable pour les grosses rugosité"""
    n = []
    x = []
    y = []
    centre = np.asarray(centre)
    for i,o in enumerate(elements):
        a,b = points[o]
        u = b-a
        v = centre-a
        n.append(v - np.dot(u,v)/(np.power(norm(u),2))*u)
        n[-1] = n[-1]/norm(n[-1])
        x.append((a[0]+b[0])/2)
        y.append((a[1]+b[1])/2)
    return -np.asarray(n),np.asarray([x,y])

def discretisation_omega(extent,res):
    """Discrétise un rectangle extent en res*res points"""
    a,b,c,d = extent
    x = np.linspace(a,b,res)
    y = np.linspace(c,d,res)
    
    xx,yy = np.meshgrid(x,y)
    
    xx = xx.reshape(res*res)
    yy = yy.reshape(res*res)
    
    zz = zip(xx,yy)
    return zz,res

def discretisation_cercle(centre,rayon,resolution):
    """Discrétise un demi cercle de rayon 'rayon' en 'resolution' points"""
    theta = np.linspace(0,np.pi,resolution)
    points = rayon*np.array([[np.cos(elm),np.sin(elm)] for elm in theta])
    return points + np.asarray(centre),theta
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    