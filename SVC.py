from sklearn.svm import SVC
X=[[1],[2],[4],[5]]
Y=["fail","fail","pass","pass"]
model=SVC(kernel="linear")
model.fit(X,Y)
hours=[[3]]
prediction=model.predict(hours)
print(prediction)