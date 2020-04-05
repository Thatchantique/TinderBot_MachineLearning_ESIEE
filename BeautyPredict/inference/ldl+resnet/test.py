from keras.layers import Conv2D, Input, MaxPool2D,Flatten, Dense, Permute, GlobalAveragePooling2D
from keras.models import Model
from keras.optimizers import adam
import numpy as np
import pickle
import keras
import cv2
import sys
import dlib
import os.path
from keras.models import Sequential
from keras.applications.resnet50 import ResNet50
from keras.layers.core import Dense
from keras.optimizers import Adam
import pickle
import numpy as np
import cv2
import os
from keras.layers import Dropout

from beauty_predict import beauty_predict


beauty_predict("../../samples/image",'rayou.png')