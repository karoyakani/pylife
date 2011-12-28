# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:38:54 2011

@author: karoyakani
"""

import numpy as np
from scipy.ndimage import generic_filter
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def conway(mask):
    """ The Conway function that returns the next generation life of the given mask
    args:
    mask 3-by-3 neighborhood mask
    retrurns:
    boolean true if aive or born, false if dead
    description:
    alive := if mask center is currently alive and if number of neighbors is 2 or 3
    born := if mask center is currently dead and if number of neighbots is 3
    dead := otherwise
    """
    p = mask.sum() - mask[4]
    return (2 <= p <= 3) if mask[4] == 1 else (p == 3)

def init():
    sz = 64
    hf = sz/2
    bw = np.zeros((sz, sz), dtype=np.int)
    bw[hf, hf-1:hf+2] = bw[hf-1, hf] = bw[hf+1, hf+1] = 1
    return bw

def update(n, fp):
    global bw
    print 'Generation: %d' % n
    bw = generic_filter(bw, conway, footprint=fp, mode='constant')
    ax.set_array(bw)
    return ax,

if __name__ == '__main__':
    fg = plt.figure()
    bw = init()
    ax = plt.imshow(bw, interpolation='none')
    it = 100
    fp = np.ones((3,3), dtype=np.int)
    an = animation.FuncAnimation(fg, update, it, fargs=(fp, ), blit=True, interval=10, repeat=False)
    plt.show()
