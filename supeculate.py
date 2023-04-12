import os
import tensorflow as tf

from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.preprocessing import image
import numpy as np


im_class = ["cutting","heating"]
model = load_model('./trainkitchen_model.h5')

