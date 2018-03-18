#coding:utf-8
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

def introduction(onde,n):
    print "Simulation de la réflexion d'une onde {} à une interface rugueuse."\
    .format(onde)
    print "{} processeur(s) utilisé(s)".format(n)
    print "Représentation de la configuration"

def show(points,source):
    """Affiche dans un plot tous les points contenus dans points"""
    plt.scatter(*source)
    plt.plot(points[:,0],points[:,1],'.')
    plt.axis('equal')
    
def show_all(points,n,x,y,source=None):
    """Affiche toute la configuration, y compris les normales aux élements"""
    show(points,source)
    plt.quiver(x,y,-n[:,0],-n[:,1],width=0.005)
    plt.grid()
    plt.show()
    
def lisse_ou_pas_lisse(rms,f,angle):
    print "RMS:{}, LAMBDA:{}, LAMBDA/COS(THETA)/8:{}".format(rms,340/f,340/f/np.cos(angle)/8)
    if rms < 340/f/np.cos(angle)/8: 
        print "Surface lisse au sens de Rayleigh"
    else:
        print "Surface rugueuse au sens de Rayleigh, de rugosité {}".format(rms)

def cartographie(pression, res, extent, points,\
                 title='Pression',amplitude=1):
    plt.subplot(1,2,1)
    plt.imshow(np.real(pression.reshape([res,res])), extent=extent,\
               origin='lower',vmin=-amplitude, vmax=amplitude,\
               interpolation='bicubic')
    plt.plot(points[:,0],points[:,1],'r.')
    plt.axis(extent)
    plt.colorbar()
    plt.title('Partie reelle de la pression')
    plt.subplot(1,2,2)
    plt.imshow(abs(pression.reshape([res,res])), extent=extent,\
               origin='lower',vmin=-amplitude, vmax=amplitude,\
               interpolation='bicubic')
    plt.plot(points[:,0],points[:,1],'b.')
    plt.axis(extent)
    plt.colorbar()
    plt.title('Module de la pression')
    plt.show()
    
def polar_plot(directivite,theta,title='Directivite de la configuration'):
    plt.polar(theta[1:-1],abs(directivite[1:-1]))
    plt.title(title)
    plt.show()