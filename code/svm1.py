import numpy as np
import pandas as pd
from sklearn import *
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
training_data = np.genfromtxt('waterset.csv', delimiter=',')
inputs = training_data[:,:-1]
outputs = training_data[:, -1]
training_inputs = inputs[:1200]
training_outputs = outputs[:1200]
testing_inputs = inputs[1200:]
testing_outputs = outputs[1200:]
classifier = SVC()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of SVM Classifier on testing data is: " + str(accuracy))
testSet = [[2476.21,0,2.94,0,0.0236,0,1622.24,15,0,68.7117,6,15.32,4.49,6.6,15.8,1.3,1,0]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('SVM Prediction on the first test set is:',predictions)
testSet = [[1989.51,1,1.37,1,0.1012,1,747.1,27,1,164.5017,15,38.23,7.43,7.9,13.6,3.2,2,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('SVM Prediction on the second test set is:',predictions)
testSet = [[25.38,2,0.55,2,0.4265,2,164.81,39,2,223.8352,21,220.59,13.51,5.5,11.3,4.9,3,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('SVM Prediction on the third test set is:',predictions)
#In the result, 0 stands for good quality, 1 stands for poor quality and 2 stands for very poor quality water