from sklearn.neural_network import MLPClassifier
X=[[1],[2],[3],[4]]
Y=[0,0,1,1]
model=MLPClassifier(hidden_layer_sizes=(2,),max_iter=5000,random_state=42)
model.fit(X,Y)
hours=float(input ("enter study hours:"))
prediction=model.predict([[hours]])[0]
print("Result:","pass" if prediction else "fail")