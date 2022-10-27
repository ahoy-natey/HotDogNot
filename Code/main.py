import tensorflow as tf
import matplotlib as pit
import os
import numpy as np
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array


datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=.02,
    height_shift_range=0.2,
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)