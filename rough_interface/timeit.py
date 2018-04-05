#coding:utf-8
from __future__ import print_function
from time import time,sleep
import sys

class ProgressBar(object):
    """Affichage de l'avancée en %"""
    def __init__(self):
        super(ProgressBar, self).__init__()
        self.current = 0
        self.percent = 0
        self.total = 0

    def reset(self):
        self.current = 0
        self.total = 0

    def set_total(self,number):
        self.total = number

    def set_current(self,number):
        self.current = number
        self.show()

    def show(self):
        current_percent = int(self.current*100/float(self.total))
        if self.percent != current_percent:
            self.percent = current_percent
            print('{0:02d}%'.format(current_percent))
            #sys.stdout.flush()
        


def timeit(func,quiet=False):
    """Chronomètre l'éxecution d'une fonction"""
    def wrapper(*args,**kwargs):
        starttime = time()
        output = func(*args,**kwargs)
        stoptime = time()
        if not quiet:
            print('{}s'.format(stoptime-starttime))
        return output
    return wrapper

if __name__ == '__main__':
    a = ProgressBar()
    a.set_total(200)
    for i in range(200):
        a.set_current(i)
        sleep(.1)
