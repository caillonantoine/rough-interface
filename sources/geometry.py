#coding:utf-8

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
    return np.asarray(n),np.asarray([x,y])