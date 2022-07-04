
from flask import Flask, jsonify, request
from flask import render_template
from flask import Response
#app=Flask(__name__,template_folder="./templates")


import pandas as pd
import json
import csv

# MACHINE LEARNING
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# CREACION APP
app=Flask(__name__)

# RUTA DE INICIO
@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")
    #return "Bienvenido"


# CSV
@app.route("/irisData/", methods=['GET'])
def irisData():
    df=pd.read_csv("iris.csv")
    data=df.to_json(orient="index")
    data=json.loads(data)

    return data


# RESUMEN DEL CSV
@app.route("/iris/", methods=['GET'])
def iris():
    df=pd.read_csv("iris.csv")
    describe=df.describe().to_json(orient="index")
    describe=json.loads(describe)

    return describe


# INSERTAR
@app.route("/insertData/", methods =['POST'])
def insertData():
    data=request.data
    data=json.loads(data)
    with open("iris.csv" , "a" ,newline="") as csvfile:
        fieldnames=["sepal_length", "sepal_width", "petal_length","petal_width", "species"]
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"sepal_length": data["sepal_length"],
                         "sepal_width": data["sepal_width"],
                         "petal_length": data["petal_length"],
                         "petal_width": data["petal_width"],
                         "species": data["species"]})
    print("writing")
    return data


# ACTUALIZAR DEPENDIENDO DEL ID
@app.route('/updateData/', methods=['PUT'])
def updatedata():
    # se reciben a través del Postman:
    data = request.data
    data = json.loads(data)
    df = pd.read_csv('iris.csv')
    # id recogido de Postman:
    posicion=data['id']
    if  posicion in df.index.tolist():
        print("EXISTE")
        df.loc[df.index[posicion], 'sepal_length'] = data['sepal_length']
        df.loc[df.index[posicion], 'sepal_width'] = data['sepal_width']
        df.loc[df.index[posicion], 'petal_length'] = data['petal_length']
        df.loc[df.index[posicion], 'petal_width'] = data['petal_width']
        df.loc[df.index[posicion], 'species'] = data['species']
        # convertir a csv
        df.to_csv('iris.csv', index=False)
        # mostrar el  dato en formato Json:
        result = df.iloc[posicion].to_json(orient="index")
        return result
    else:
        # print("no existe")
        mensaje="ESTE ID NO EXISTE"
        return Response(mensaje, status=400)


# BORRAR DEPENDIENDO ID
@app.route('/deleteData/', methods=['DELETE'])
def deleteData():
    data = request.data
    data = json.loads(data)
    
    df = pd.read_csv('iris.csv')

    posicion=data['id']
    
    if  posicion in df.index.tolist():
        result = df.iloc[posicion].to_json(orient="index")
        df.drop(df.index[posicion], inplace=True)
        # convertir a csv
        df.to_csv('iris.csv', index=False)
        # mostrar el dato en formato Json:
        
        return result
    else:
        # print("no existe")
        mensaje="ESTE ID NO EXISTE"
        return Response(mensaje, status=400)


# CALCULAR LA ESPECIE
@app.route('/predicion/', methods=['PUT'])
def predicion():
    data = request.data
    data = json.loads(data)
    iris=pd.read_csv('iris.csv')    
    # cambio species a 0,1,2
    iris.species=iris.species.map({"setosa": 0, "versicolor":1,"virginica":2})
    # separo los datos a X i y 
    X=iris.drop(['species'],axis=1)
    X=np.array(X)
    y=np.array(iris['species'])
    # separo a entranimiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf=DecisionTreeClassifier()
    clf.fit(X_train,y_train)
    y_pre= clf.predict(X_test)
    
    acc=accuracy_score(y_test,y_pre)
    print(acc)

    # 
    lista=[data['sepal_length'],data['sepal_width'],data['petal_length'],data['petal_width']]
    X_test=np.array(lista).reshape(1,-1)
    y_pre=clf.predict(X_test)
    print(y_pre)
    
    predicion=y_pre.__str__()
    
    if "0" in predicion:
        predicion={0:"setosa"}
    elif "1" in predicion:
        predicion={1:"versicolor"}
    elif "2" in predicion:
        predicion={2:"virginica"}
    
    
    return jsonify(predicion)


    
if __name__ == '__main__':
    app.run(debug=True) 


