#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from timing_accuracy import timing_and_accuracy
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
preds = clf.predict(features_test)
print len([x for x in preds if x == 1])
# C = 10000
# timing_and_accuracy(SVC, features_train, features_test,
#                     labels_train, labels_test,
#                     model_params={'kernel': 'rbf', 'C':C})