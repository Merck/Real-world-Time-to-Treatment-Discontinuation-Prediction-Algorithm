import numpy as np
import random
import copy
import sklearn
import sklearn.ensemble
import os
import pickle
import lightgbm as lgb
import sys
from scipy.interpolate import interp1d



train_gs=np.loadtxt('train.dat')[:,0]
train_feature=np.loadtxt('train.dat')[:,1:]

num_tree=1000
max_depth=3
the_model=sklearn.ensemble.ExtraTreesRegressor(n_estimators=num_tree, \
        max_depth=max_depth, random_state=0).fit(np.asarray(train_feature),np.asarray(train_gs))



test_feature=np.loadtxt('test.dat')[:,1:]
value=the_model.predict(test_feature)
value_test=copy.copy(value)


np.savetxt('prediction.dat',value)



test_feature=np.loadtxt('val.dat')[:,1:]
value=the_model.predict(test_feature)
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

