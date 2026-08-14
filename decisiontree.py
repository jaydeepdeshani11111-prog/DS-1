from sklearn.tree import DecisionTreeClassifier
X=[[1],[2],[4],[5]]
Y=["fail","fail","pass","pass"]
model=DecisionTreeClassifier()
model.fit(X,Y)
hours=[[3.1]]
prediction=model.predict(hours)
print(prediction)