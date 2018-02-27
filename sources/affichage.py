#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import bemf

def introduction(onde):
    print "Simulation de la réflexion d'une onde {} à une interface rugueuse."\
    .format(onde)
    print "{} processeur(s) utilisé(s)".format(bemf.check_core())
    print "\n"
    print "Représentation de la configuration"

def show(points,source):
    """Affiche dans un plot tous les points contenus dans points"""
    plt.scatter(*source)
    plt.plot(points[:,0],points[:,1],'.')
    plt.axis('equal')
    
def show_all(points,n,x,y,source=None):
    """Affiche toute la configuration, y compris les normales aux élements"""
    show(points,source)
    plt.quiver(x,y,n[:,0],n[:,1],width=0.005)
    plt.show()
    
def cartographie(pression, res, extent, points,\
                 title='Pression',amplitude=1):
    plt.imshow(np.real(pression.reshape([res,res])), extent=extent,\
               origin='lower',vmin=-amplitude, vmax=amplitude)
    plt.plot(points[:,0],points[:,1],'r.')
    plt.axis(extent)
    plt.colorbar()
    plt.title(title + ' reelle')
    plt.show()
    plt.imshow(abs(pression.reshape([res,res])), extent=extent,\
               origin='lower',vmin=-amplitude, vmax=amplitude)
    plt.plot(points[:,0],points[:,1],'b.')
    plt.axis(extent)
    plt.colorbar()
    plt.title(title + ' absolue')
    plt.show()
    
def polar_plot(directivite,theta,title='Directivite de la configuration'):
    plt.polar(theta,abs(directivite))
    plt.title(title)
    plt.show()