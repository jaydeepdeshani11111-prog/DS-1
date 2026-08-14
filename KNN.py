from sklearn.neighbors import KNeighborsClassifier
X=[[1],[2],[3],[4],[5],[6],[7]]
Y=["fail","fail","fail","pass","pass","pass","pass"]
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)
hours=[[4.1]]
prediction=model.predict(hours)
print("prediction:",prediction[0])