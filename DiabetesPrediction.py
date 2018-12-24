
from keras.models import Sequential
from keras.layers import Dense
import numpy

seed=7
numpy.random.seed(seed)

indata=numpy.loadtxt("dia.csv",delimiter=",")
X=indata[:,0:8]
#print(X)
Y=indata[:,8]


model=Sequential()
model.add(Dense(12, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, kernel_initializer='normal', activation='relu'))
model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adamax', metrics=['accuracy'])
model.fit(X, Y, epochs=150, batch_size=5, verbose=2)

model.save("Model1.hdf5")

scores=model.evaluate(X,Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#%%

from keras.models import load_model

loaded_model=load_model('Model1.hdf5')

predicdata=numpy.loadtxt('predia.csv',delimiter=',')
prediction=loaded_model.predict(predicdata[None,0:8])

#ans=prediction[:,0][0]
#rounded = [round(x[0]) for x in prediction]
print("\nPrediction: ",prediction[:,0])
#print("\nPrediction Percentage: ",round(ans))
#print(rounded)