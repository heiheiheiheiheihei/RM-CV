import numpy as np 

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

np.random.seed(1333)

#X shape (60,000 28*28) Y shape (10,000)
(X_train, Y_train),(X_test, Y_test)=mnist.load_data()


# data pre-processing
X_train = X_train.reshape(X_train.shape[0], -1)/255
