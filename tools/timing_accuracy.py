import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score

def timing_and_accuracy(Model, features_train, features_test, labels_train, labels_test, model_params):

	clf = Model(**model_params)

	t0 = time()
	clf.fit(features_train, labels_train)
	print 'Training time is {} seconds'.format(round(time() - t0), 3)

	t1 = time()
	preds = clf.predict(features_test)
	print 'Prediction time is {} seconds'.format(round(time() - t1), 3)


	accuracy = accuracy_score(labels_test, preds)

	print 'accuracy is {}'.format(accuracy)