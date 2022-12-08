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



train_gs=np.genfromtxt('gs_train_exptime.dat')[:,1]
train_feature=np.loadtxt('train.dat')[:,1:]

num_tree=1000
max_depth=3
the_model=sklearn.ensemble.ExtraTreesRegressor(n_estimators=num_tree, \
        max_depth=max_depth, random_state=0).fit(np.asarray(train_feature),np.asarray(train_gs))



test_feature=np.loadtxt('test.dat')[:,1:]
value=the_model.predict(test_feature)
value_test=copy.copy(value)


np.savetxt('prediction_time.dat',value)



