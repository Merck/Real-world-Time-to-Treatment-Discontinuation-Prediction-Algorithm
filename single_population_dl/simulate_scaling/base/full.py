import keras
import tensorflow as tf
import numpy as np
from keras.models import Model
from keras.layers import Input, Conv1D, MaxPooling1D, BatchNormalization, Dense, Flatten
from tensorflow.keras.optimizers import Adam
from keras.initializers import glorot_uniform
from keras.losses import binary_crossentropy
from keras import backend as K
from keras import losses
from keras.optimizers import adam


def self_crossentropy(y_true, y_pred):
    y_true = K.flatten(y_true)
    y_pred = tf.clip_by_value(K.flatten(y_pred), 1e-7, (1.0 - 1e-7))
    out = -(y_true * K.log(y_pred) + (1.0 - y_true) * K.log(1.0 - y_pred))
    return K.mean(out)

def mean_squared_error(y_true, y_pred):
    return K.mean(K.square(y_pred - y_true), axis=-1)

def clipped_mse(y_true, y_pred):
    return K.mean(K.square(K.clip(y_pred, 0., 1.0) - K.clip(y_true, 0., 1.0)), axis=-1)

opt = adam(lr=0.001, decay=1e-6)

def full1d(size):
    inputs = Input((size,1))  # 1024
    layer=Dense(256,activation='relu')(inputs)
    layer=Dense(128,activation='relu')(layer)
    layer=Dense(64,activation='relu')(layer)
    layer=Flatten()(layer)
    outputs = Dense(1, activation=None)(layer)
    model = Model(inputs=[inputs], outputs=[outputs])
    model.compile(optimizer=opt, loss=mean_squared_error, metrics=["accuracy"])
    return model


