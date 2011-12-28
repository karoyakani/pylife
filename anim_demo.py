# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 00:28:04 2011

@author: karoyakani
"""
import numpy as np
from scipy.ndimage import generic_filter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import urllib

def init():
    url = urllib.URLopener()
    url.retrieve("http://blogs.mathworks.com/images/steve/2008/gosper_glider_gun.png", "gosper.png")
    return (plt.imread('gosper.png')*255).astype(np.int)

def conway(mask):
    p = mask.sum() - mask[4]
    return (2 <= p <= 3) if mask[4] == 1 else (p == 3)

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

""" Animation.save doesn't work and more likely mencoder doesn't exit; however, 
this creates _tmpNNNN.png files so that e.g. ImagemMagic's convert may work. 
an = animation.FuncAnimation(fg, update, it, fargs=(fp, ), blit=True, interval=10, repeat=False)
an.save('life.mp4')
import os
os.system("mencoder 'mf:_tmp*.png' -mf type=png:fps=15 -ovc lavc -lavcopts vcodec=wmv2 -oac copy -o anim.mpg")
"""
""" url loader example - nasa.jpg image
import urllib
url = urllib.URLopener()
url.retrieve("http://www.python.org/images/success/nasa.jpg", "NASA.jpg")
img = plt.imread('NASA.jpg')
plt.figure()
plt.imshow(np.flipud(img))
plt.show()
"""
