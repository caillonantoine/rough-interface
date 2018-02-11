#coding:utf-8
import numpy as np

def load(name):
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