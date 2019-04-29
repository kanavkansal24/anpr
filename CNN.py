from keras.models import Sequential,load_model
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialising
model=Sequential()


#First ConvoLayer
model.add(Conv2D(64, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

#another Convolayer
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(64, activation='tanh'))
model.add(Dense(units = 1, activation = 'sigmoid'))

#Final Compiling the model
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])



from keras.preprocessing.image import ImageDataGenerator


trainDataGen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = False)


testDataGen = ImageDataGenerator(rescale = 1./255)

trainingSet = trainDataGen.flow_from_directory('DataSet/TrainingSet',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')


testSet = testDataGen.flow_from_directory('DataSet/TestSet',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')


model.fit_generator(trainingSet,
                         steps_per_epoch = 10,
                         epochs = 3,
                         validation_data = testSet,
                         validation_steps = 200)

import os
import h5py


model.save("model.h5")
model=load_model("model.h5")


