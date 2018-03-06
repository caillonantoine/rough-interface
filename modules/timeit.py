#coding:utf-8
from time import time

def timeit(func):
    """Chronomètre l'éxecution d'une fonction"""
    def wrapper(*args,**kwargs):
        starttime = time()
        output = func(*args,**kwargs)
        stoptime = time()
        print '{}s'.format(stoptime-starttime)
        return output
    return wrapper