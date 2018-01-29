import os
import numpy as np
from shutil import copyfile

for imagename in os.listdir(os.getcwd() + '/HR'):
    chance = np.random.rand()
    if chance > .85:
        copyfile(os.getcwd() + '/HR/' + imagename, os.getcwd() + '/HRV/' + imagename)
        copyfile(os.getcwd() + '/LR/LR_' + imagename, os.getcwd() + '/LRV/' + imagename)
