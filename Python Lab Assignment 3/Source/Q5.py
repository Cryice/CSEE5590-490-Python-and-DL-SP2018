# importing necessary packages and modules
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# loading iris dataset
iris = datasets.load_iris()

# loading features
data = iris.data
# loading target labels
labels = iris.target

#splitting data into train and test
train_X,test_X,train_y,test_y = train_test_split(data,labels,test_size=0.2,random_state=42)

# loading KNN estimator
clf = neighbors.KNeighborsClassifier(n_neighbors=50)
# fitting training data
clf.fit(train_X, train_y)
# predicting on test data
ypred = clf.predict(test_X)
# calculating accuracy
print(accuracy_score(ypred,test_y))
