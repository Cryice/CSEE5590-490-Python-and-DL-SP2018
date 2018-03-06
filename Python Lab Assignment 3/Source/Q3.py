# importing required packages and modules
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# loading iris dataset
iris = load_iris()
# loading the features
data = iris.data
# loading the target labels
labels = iris.target
# splitting the data into train_test
X_train,X_test,y_train,y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
#Support vector classifier with 'linear' kernel
clf = SVC(kernel='rbf')
# fitting the classifier on train data
clf.fit(X_train,y_train)
# predicting using test data
ypred = clf.predict(X_test)
# calculating accuracy
print(accuracy_score(ypred, y_test))