from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

iris = datasets.load_iris()
print(iris.feature_names)
print(iris.target_names)

iris_data_set=pd.DataFrame({
    'sepal length':iris.data[:,0],
    'sepal width':iris.data[:,1],
    'petal length':iris.data[:,2],
    'petal width':iris.data[:,3],
    'species':iris.target
})
#print(iris_data_set.head())

# the data
X = iris_data_set.iloc[:,0:4]
#the an / prediction
print(X) 
y = iris_data_set.iloc[:,-1]
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
#print("len of X_train:",len(X_train))
#print("len of X_test", len(X_test))
#print("len of y_train:",len(y_train))
#print("len of y_test", len(y_test))
clf = RandomForestClassifier(n_estimators = 100)
clf.fit(X_train,y_train)
y_prediction = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_prediction))


