#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

clf1 = AdaBoostClassifier()
clf1.fit(features_train, labels_train)
pred1 = clf1.predict(features_test)

clf2 = RandomForestClassifier()
clf2.fit(features_train, labels_train)
pred2 = clf2.predict(features_test)

clf3 = KNeighborsClassifier()
clf3.fit(features_train, labels_train)
pred3 = clf3.predict(features_test)

print accuracy_score(pred1, labels_test)
print accuracy_score(pred2, labels_test)
print accuracy_score(pred3, labels_test)
ensemble_pred = [pred1[i] + pred2[i] + pred3[i] for i in range(len(pred1))]
ensemble_pred = [int ( x > 1.5) for x in ensemble_pred]
print accuracy_score(ensemble_pred, labels_test)



#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary








try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
