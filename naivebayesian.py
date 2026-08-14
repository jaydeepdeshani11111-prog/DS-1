from sklearn.naive_bayes import GaussianNB
X=[[1],[2],[4],[5]]
Y=["fail","fail","pass","pass"]
model=GaussianNB()
model.fit(X,Y)
hours=[[3.5]]
prediction=model.predict(hours)
print(prediction)