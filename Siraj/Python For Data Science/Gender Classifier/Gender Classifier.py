from sklearn import tree

#[height , weight, shoe size]
x = [[180,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,410],
     [190,90,47],[175,64,39],
     [177,70,40],[159,55,37],[171,75,42],[181,85,43]]

y = ['male','male','female','female','male','male','female','female','female','male','male']

print(x,y)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction  = clf.predict([[190,70,43]])
print(prediction)