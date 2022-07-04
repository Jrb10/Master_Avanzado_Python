import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

class Model:

    def validar_formulario(data):
        # for checking Name
        if data['name'].isdigit():
            return ('name', 'Invalid name!')                    
                    # for checking UserName
        if data['username'].isdigit():
            return ('username', 'Invalid username!')
                        
        # for checking Age
        if data['age'] <= 0:
            return ('age', 'Invalid age!')
                            
        # for matching Passwords
        if data['pass'] != data['passes']:
            return ('passes', "Please make sure your passwords match")       
    
    def calcular(datos):
        df=pd.read_csv("iris.csv")
        df.species=df.species.map({"setosa": 0, "versicolor":1,"virginica":2})
        X=df.drop(['species'],axis=1)
        X=np.array(X)
        y=np.array(df['species'])
        
        # ENTRENO Y CALCULO EL PORCENTAJE
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        clf=DecisionTreeClassifier()
        clf.fit(X_train,y_train)
        y_pre= clf.predict(X_test) 
        acc=accuracy_score(y_test,y_pre)
        # print(acc)

        # CALCULO LA ESPECIE CON LOS DATOS

        X_test=np.array(datos).reshape(1,-1)
        y_pre=clf.predict(X_test)
        
        predicion=y_pre.__str__()
        if "0" in predicion:
            predicion="setosa"
            
        elif "1" in predicion:
            predicion="versicolor"
        elif "2" in predicion:
            predicion="virginica"
        # DEVUELVO EL RESULTADO
        return predicion