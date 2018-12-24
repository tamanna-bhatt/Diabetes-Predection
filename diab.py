# Create first network with Keras
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers.core import Dense, Dropout, Activation, Flatten
from sklearn.utils import shuffle
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split
#from keras.optimizer import Adam
import numpy 
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
dataset = numpy.loadtxt("diabetes.csv", delimiter=",")
num_classes=2
labels=numpy.ones((768,),dtype='int64')
labels[0:269]=1
labels[269:]=0
names=['positive','negative']
Y=np_utils.to_categorical(labels,num_classes)
x,y=shuffle(dataset,Y,random_state=2)
XTrain, XTest,Ytrain,YTest=train_test_split(x,y,test_size=0.05,random_state=2)

data_dim = 9
timesteps = 729
batch_size=1
XTrain=XTrain[:,:,None]
XTest=XTest[:,:,None]
Ytrain=Ytrain[:,:,None]
YTest=YTest[:,:,None]
#original
# load pima indians dataset
#dataset = numpy.loadtxt("diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
#X = dataset[:,0:8]
#print(X)
#Y = dataset[:,8]
# create model
#%%

model = Sequential()
#change init='kernel_initializer'

model.add(LSTM(32, return_sequences=True, batch_input_shape=(729, 9, 1)))  # returns a sequence of vectors of dimension 32
model.add(LSTM(32, return_sequences=True))  # returns a sequence of vectors of dimension 32
#model.add(LSTM(32))  # return a single vector of dimension 32
model.add(Flatten())
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dropout(0.3))
model.add(Dense(2))
model.add(Activation('sigmoid'))

#original
#model.add(Dense(12, input_dim=8, kernel_initializer='normal', activation='relu')) 
#model.add(Dense(8, kernel_initializer='normal', activation='relu'))
#model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
# Compile model
#adam=Adam(lr=0.01)
model.compile(loss='binary_crossentropy', optimizer='Adamax', metrics=['accuracy'])
model.summary()


#%%
# Fit the model
#XTrain=XTrain[None,:]

model.fit(XTrain, Ytrain, epochs=150, batch_size=batch_size, validation_data=(XTest, YTest), verbose=2)
#evaluate the model
#scores=model.evaluate(X,Y)
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# calculate predictions'''
datapred=numpy.loadtxt('predia.csv',delimiter=',')
predictions = model.predict(datapred[None,0:8])
# round predictions
rounded = [round(x[0]) for x in predictions]
print("\nPREDICTIONS:",predictions[:,0])
print(rounded)