import numpy
import imageio as ii
import os
from scipy import misc

for imagename in os.listdir(os.getcwd() + '/HR'):
    hrimage = ii.imread(os.getcwd() + '/HR/' + imagename)
    lrimage = misc.imresize(hrimage, size=(135, 135), interp='bicubic')
    misc.imsave(os.getcwd() + '/LR/LR_' + imagename, lrimage)
