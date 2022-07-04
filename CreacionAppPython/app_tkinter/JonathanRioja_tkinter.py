# PARA PODER CONVERTIR A EXE
import sklearn.utils._typedefs
import sklearn.utils._heap
import sklearn.utils._cython_blas
import sklearn.tree
import sklearn.tree._utils
import sklearn.utils._sorting
import sklearn.utils._vector_sentinel

import sklearn.neighbors._partition_nodes
import sklearn.neighbors._quad_tree


from tkinter import Tk,Button,Toplevel,Label,Entry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


import pandas as pd
import os
import numpy as np


MEDIA_ROOT=os.path.expanduser("~/OneDrive/Escritorio/app_tkinter/iris.csv")

df=pd.read_csv(MEDIA_ROOT)


ventana = Tk()
ventana.geometry("500x500")
ventana.wm_title('APP IRIS')


def irisPetal():
    # CREO UNA NUEVA VENTANA
    nueva_ventana=Toplevel(ventana)
    nueva_ventana.title("IRIS PETAL")
    versicolor=df[df.species=="versicolor"]
    setosa=df[df.species=="setosa"]
    virginica=df[df.species=="virginica"]

    # CREO LA FIGURA
    fig, ax = plt.subplots()
    ax.scatter(versicolor["petal_length"], versicolor["petal_width"], label="versicolor", facecolor="green")
    ax.scatter(setosa["petal_length"], setosa["petal_width"], label="setosa",facecolor="blue")
    ax.scatter(virginica["petal_length"], virginica["petal_width"], label="virginica",facecolor="red")
    ax.set_xlabel("Petal_length")
    ax.set_ylabel("Petal_width")
    ax.set_title("Iris Petal Sizes")
    ax.legend(loc='upper left')

    canvas = FigureCanvasTkAgg(fig, nueva_ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar=NavigationToolbar2Tk(canvas,nueva_ventana)
    toolbar.update()
    canvas.get_tk_widget().pack()




def irisSepal():
    nueva_ventana=Toplevel(ventana)
    nueva_ventana.title("SEPAL PETAL")

    versicolor=df[df.species=="versicolor"]
    setosa=df[df.species=="setosa"]
    virginica=df[df.species=="virginica"]
    
    fig1, ax1 = plt.subplots()
    ax1.scatter(versicolor["sepal_length"], versicolor["sepal_width"], label="versicolor", facecolor="green")
    ax1.scatter(setosa["sepal_length"], setosa["sepal_width"], label="setosa",facecolor="blue")
    ax1.scatter(virginica["sepal_length"], virginica["sepal_width"], label="virginica",facecolor="red")
    ax1.set_xlabel("Sepal_length")
    ax1.set_ylabel("Sepal_width")
    ax1.set_title("Iris Sepal Sizes")
    ax1.legend(loc='upper left')

    canvas1 = FigureCanvasTkAgg(fig1, nueva_ventana)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

    toolbar1=NavigationToolbar2Tk(canvas1,nueva_ventana)
    toolbar1.update()
    canvas1.get_tk_widget().pack()


    
def predecir():
    
    nueva_ventana=Toplevel(ventana)
    nueva_ventana.title("PREDECIR")
    nueva_ventana.geometry("300x300")
    # CREO LOS LABEL
    Label(nueva_ventana, text="Sepal_length: ").grid(padx=5,pady = 5,row=1,column=0)
    Label(nueva_ventana, text="Sepal_width: ").grid(padx=5,pady = 5,row=2,column=0)
    Label(nueva_ventana, text="Petal_length: ").grid(padx=5,pady = 5,row=3,column=0)
    Label(nueva_ventana, text="Petal_width: ").grid(padx=5,pady = 5,row=4,column=0)
    Label(nueva_ventana, text=" ").grid(padx=5,pady = 5,row=5,column=1)
    
    # CREO LOS ENTRY
    el=Entry(nueva_ventana)
    el.insert(0,"")
    el.grid(padx=5,pady = 5,row=1,column=1)

    el2=Entry(nueva_ventana)
    el2.insert(0,"")
    el2.grid(padx=5,pady = 5,row=2,column=1)

    el3=Entry(nueva_ventana)
    el3.insert(0,"")
    el3.grid(padx=5,pady = 5,row=3,column=1)

    el4=Entry(nueva_ventana)
    el4.insert(0,"")
    el4.grid(padx=5,pady = 5,row=4,column=1)

    # CALCULO EL PORCENTAJE DE PREDICION
    df.species=df.species.map({"setosa": 0, "versicolor":1,"virginica":2})
    X=df.drop(['species'],axis=1)
    X=np.array(X)
    y=np.array(df['species'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf=DecisionTreeClassifier()
    clf.fit(X_train,y_train)
    y_pre= clf.predict(X_test)
    
    acc=accuracy_score(y_test,y_pre)
    # print(acc)

    def calcular():
        # RECUPERO LA INFORMACION DE LOS ENTRY
        v1=float(el.get())
        v2=float(el2.get())
        v3=float(el3.get())
        v4=float(el4.get())
        lista=[v1, v2, v3, v4]

        # CALCULO LA ESPECIE CON LOS DATOS INTRODUCIDOS
        X_test=np.array(lista).reshape(1,-1)
        y_pre=clf.predict(X_test)
        # print(y_pre)
            
        predicion=y_pre.__str__()
        if "0" in predicion:
            predicion="setosa"
        elif "1" in predicion:
            predicion="versicolor"
        elif "2" in predicion:
            predicion="virginica"

        # AÑADO EL RESULTADO EN EL LABEL 
        Label(nueva_ventana, text=predicion , fg="white",bg="red").grid(padx=5,pady = 5,row=5,column=1)

    
    Button(nueva_ventana,text="Calcular Especie", command=calcular,
                fg="white",bg="blue").grid(padx=5,pady = 5,row=5,column=0)
    

def quit():
    ventana.quit()
    ventana.destroy()

# VENTANA PRINCIPAL CON EL LABEL Y LOS 4 BOTONES
Label(ventana, text="BIENVENIDO A LA APLICACION").grid(padx=20,pady = 20,row=0,column=0)

Button(ventana,text="Mostrar Petal Iris",command=irisPetal ,fg="white",bg="blue",width=30,
                           height=5).grid(padx=30,pady = 5,row=1,column=0)


Button(ventana,text="Mostrar Sepal Iris",command=irisSepal ,fg="white",bg="blue",width=30,
                           height=5).grid(padx=30,pady = 5,row=2,column=0)


Button(ventana,text="Calcular Predición",command=predecir ,fg="white",bg="blue",width=30,
                            height=5).grid(padx=30,pady = 5,row=3,column=0)


Button(ventana,text="Cerrar",command=quit ,fg="white",bg="blue",width=30,
                           height=5).grid(padx=30,pady = 5,row=4,column=0)


ventana.mainloop()

# tkinterenv\Scripts\activate
# python JonathanRioja_tkinter.py