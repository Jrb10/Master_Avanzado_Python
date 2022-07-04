
from fastapi import FastAPI 
from fastapi import HTTPException

from models import ClaseTitanic
from models import ClaseTitanic1

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

import os
import pandas as pd
import json
import csv 
import numpy as np


# app
app=FastAPI()

# get
@app.get("/")
async def root():
    return "Bienvenido a mi app"

        
# ruta archivo: C:\Users\Usuario\OneDrive\Escritorio\app_fastAPI
# ruta csv : ~/OneDrive/Escritorio/app_fastAPI/Titanic.csv
#RUTA MEDIA_ROOT
MEDIA_ROOT=os.path.expanduser("~/OneDrive/Escritorio/app_fastAPI/Titanic.csv")


@app.get("/getTitanic/")
async def root():
    df=pd.read_csv(MEDIA_ROOT)
    data=df.to_json(orient="index")
    data=json.loads(data)
    return data


@app.get("/describeTitanic/")
async def describeTitanic():
    df=pd.read_csv(MEDIA_ROOT)
    data=df.describe().to_json(orient="index")
    data=json.loads(data)
    return data


@app.post("/insertData/")
async def insertData(item: ClaseTitanic):
    with open(MEDIA_ROOT, 'a', newline='') as csvfile:
        fieldnames = ['Name','Pclass','Age','Sex','Survived']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({'Name': item.Name,
                         'Pclass': item.Pclass,
                         'Age': item.Age,
                         'Sex': item.Sex,
                         'Survived': item.Survived})
    return item


@app.put("/updateData/{item_id}")
async def updateData(item_id: int, item: ClaseTitanic):
    df=pd.read_csv(MEDIA_ROOT)
    
    new_row=[item.Name, item.Pclass,item.Age,item.Sex,item.Survived]

    if item_id in df.index.tolist():
        df.iloc[item_id]=new_row
        df.to_csv(MEDIA_ROOT,index=False)
        data=df.iloc[item_id].to_json(orient="index")
        data=json.loads(data)
        # añado al dict el id 
        id={"id":item_id}
        data.update(id)
        return data
    
    else:
        raise HTTPException(status_code=400, detail='ID NO ENCONTRADO')


@app.delete("/deleteData/{item_id}")
async def deleteData(item_id: int):
    df=pd.read_csv(MEDIA_ROOT)
    
    if  item_id in df.index.tolist():
        df.drop(df.index[item_id],inplace=True)
        df.to_csv(MEDIA_ROOT,index=False)
        return "ELIMINADO"
    else: 
        raise HTTPException(status_code=400, detail='ID NO ENCONTRADO')


@app.put("/predicion/")
async def predicion(item: ClaseTitanic1):

    df=pd.read_csv(MEDIA_ROOT)
        # CAMBIO STR A INT
    df['Sex'].replace(['female','male'],[0,1],inplace=True)
    df['PClass'].replace(['1st','2nd','3rd'],[1,2,3],inplace=True)
        # PARA VER LOS NaN
    # df.isnull().any()     
        # CALCULA LA MEDIA DE LOS AÑOS PARA VALORES NaN
    # print(df['Age'].mean())
        # DA 30.40 ASI QUE CAMBIO LA EDAD NaN a 30
    meanAge=30
    df['Age']=df['Age'].replace(np.nan,meanAge)
        # VER LAS FILAS DONDE LA COLUM=PCLASS HAY VALORES NaN
    # lineas=df[df['PClass'].isnull()]
    # print(lineas)
        # AL SER UNA FILA, LA ELIMINO 
    df.drop(df.index[456],inplace=True)
        # EN X ME QUITO LA COL=NAME YA QUE NO ME INTERESA Y SURVIDED
    X=np.array(df.drop(['Name','Survived'],axis=1))
    y=np.array(df['Survived'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # CALCULO LA PREDICION CON KNEIGHBORS
    knn=KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,y_train)
    y_pre=knn.predict(X_test)
    # print("y_pred")
    # print(y_pre)
    # print("predicion 1")
    # print(knn.score(X_train,y_train))
    # Calculo y_test con los datos
    new_data=[item.Pclass,item.Age,item.Sex]
    X_test3=np.array(new_data).reshape(1,-1)
    y_pre=knn.predict(X_test3)
    print("y_pred_test3")
    print(y_pre)
    if y_pre[0]==0:
        print("NO SOBREVIVE ")
        return {"SOBREVIVE":"NO"}
    else:
        print("SI SOBREVIVE ")
        return {"SOBREVIVE":"SI"}
     
        # PRUEBA CON SUPPORT VECTOR MACHINE
    # svc=SVC()
    # svc.fit(X_train,y_train)
    # # y_pred=svc.predict(X_test)
    # # print("y_pred")
    # # print(y_pre)
    # print("predicion 2")
    # print(svc.score(X_train,y_train))
        # Calculo y_test con los datos
    # new_data=[item.Pclass,item.Age,item.Sex]
    # X_test2=np.array(new_data).reshape(1,-1)
    # y_pre=svc.predict(X_test2)
    # print("y_pred_test2")
    # print(y_pre)
    

        # PRUEBA CON REGRESION LOGISTICA
    # logreg=LogisticRegression()
    # logreg.fit(X_train,y_train)
    # y_pre=logreg.predict(X_test)
    # print("y_pred")
    # print(y_pre)
    # print("predicion 1")
    # print(logreg.score(X_train,y_train))
        # Calculo y_test con los datos
    # new_data=[item.Pclass,item.Age,item.Sex]
    # X_test1=np.array(new_data).reshape(1,-1)
    # y_pre=logreg.predict(X_test1)
    # print("y_pred_test1")
    # print(y_pre)
    
    

    




    








    
    
    

        







