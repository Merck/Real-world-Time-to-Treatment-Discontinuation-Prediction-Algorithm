#!/usr/bin/env python
import copy
import random
import os
import sys
import logging
import numpy as np
import time
import scipy.io
import glob
import pickle
from keras.utils.np_utils import to_categorical
from keras import backend as K
import tensorflow as tf
import keras
import full
from scipy.interpolate import interp1d


size=len(np.loadtxt('test.dat')[0,1:])
model = full.full1d(size)
the_model='weights_0.h5'
model.load_weights(the_model)

test_feature=np.loadtxt('test.dat')[:,1:]
value=model.predict(test_feature.reshape((test_feature.shape[0],test_feature.shape[1],1)))
value=value.reshape(len(value))
value_test=copy.copy(value)
np.savetxt('prediction.dat',value)


test_feature=np.loadtxt('val.dat')[:,1:]
value=model.predict(test_feature.reshape((test_feature.shape[0],test_feature.shape[1],1)))
value=value.reshape(len(value))
np.savetxt('val_prediction.dat',value)
value_new=[]
for vvv in value:
    vvv=vvv+(random.random()-0.5)*0.0001
    value_new.append(vvv)
value_new=np.asarray(value_new)

val_gs=np.genfromtxt('gs_val.dat')
val_time=np.genfromtxt('gs_val_exptime.dat')[:,1]
val_time_new=[]
for vvv in val_time:
    vvv=vvv+(random.random()-0.5)*0.0001
    val_time_new.append(vvv)
val_time_new=np.asarray(val_time_new)



f = interp1d(value_new, val_time_new,fill_value='extrapolate')

ynew = f(value_test)

ynew=np.nan_to_num(ynew, copy=True, nan=0.0, posinf=2000, neginf=0)
np.savetxt('prediction_time.dat',ynew)

