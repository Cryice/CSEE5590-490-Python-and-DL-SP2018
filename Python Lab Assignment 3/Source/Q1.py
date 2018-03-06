# Importing required modules and datasets from sklearn

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits

# initializing digit function
digitdata = load_digits()
# retrieving data
data = digitdata.data
# retrieving labels
labels = digitdata.target
# splitting data into train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
#Initializing lda
clf = LinearDiscriminantAnalysis()
#fitting the training data
clf.fit(X_train,y_train)
# predicting for test data
ypred = clf.predict(X_test)
# calculating the accuracy
print(accuracy_score(ypred, y_test))


