
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel,QMainWindow, QLineEdit

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import sys 

import matplotlib.pyplot as plt 

import os
import pandas as pd
import numpy as np



MEDIA_ROOT=os.path.expanduser("~/OneDrive/Escritorio/app_pyqt5/iris.csv")

class PetalIris(QDialog):
    def __init__(self, parent=None):
        super(PetalIris, self).__init__(parent)

        df=pd.read_csv(MEDIA_ROOT)

        self.setWindowTitle("PETAL IRIS")

        # CREACION DE LA GRAFICA
        self.figure = plt.figure() 

        colors={"setosa":"blue", "versicolor":"green", "virginica":"red"}
        species_color=df.species.map(colors)
        ax = self.figure.add_subplot(111) 

        ax.scatter(df.petal_length,df.petal_width,color=species_color)
        ax.legend()
        self.canvas = FigureCanvas(self.figure) 

        self.canvas.draw() 
   
        self.toolbar = NavigationToolbar(self.canvas, self) 

        
        # BOTON PARA VOLVER AL MENU
        self.button = QPushButton(self) 
        self.button.setText("VOLVER AL MENU PRINCIPAL")
        self.button.clicked.connect(self.cerrar) 

        
        # CREACION Y AÑADIRLO AL LAYOUT
        layout = QVBoxLayout()
        layout.addWidget(self.canvas) 
        layout.addWidget(self.toolbar) 
        layout.addWidget(self.button) 
        self.setLayout(layout) 

        
    def cerrar(self):
        self.ventanaPrincipal = VentanaPrincipal()               
        self.ventanaPrincipal.show()                             
        self.hide() 
        
class SepalIris(QDialog):
    def __init__(self, parent=None):
        super(SepalIris, self).__init__(parent)

        df=pd.read_csv(MEDIA_ROOT)

        self.setWindowTitle("PETAL IRIS")

        # CREACION DE LA GRAFICA
        self.figure = plt.figure() 

        colors={"setosa":"blue", "versicolor":"green", "virginica":"red"}
        species_color=df.species.map(colors)
        ax1 = self.figure.add_subplot(111) 

        ax1.scatter(df.sepal_length,df.sepal_width,color=species_color)
        
        self.canvas = FigureCanvas(self.figure) 

        self.canvas.draw() 
   
        self.toolbar = NavigationToolbar(self.canvas, self) 

        
        # BOTON PARA VOLVER AL MENU
        self.button = QPushButton(self) 
        self.button.setText("VOLVER AL MENU PRINCIPAL")
        self.button.clicked.connect(self.cerrar) 

        
        # CREACION Y AÑADIRLO AL LAYOUT
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar) 
        layout.addWidget(self.button) 
        self.setLayout(layout) 

        
    def cerrar(self):
        self.ventanaPrincipal = VentanaPrincipal()               
        self.ventanaPrincipal.show()                             
        self.hide()   


class Predicion(QMainWindow):
    def __init__(self, parent=None):
        super(Predicion, self).__init__(parent)   
        
        # REDIMENSIONES LA VENTANA PREDICION
        self.resize(350,350)
        self.setWindowTitle("PREDICION")

        # CREO LOS LABEL 
        self.label=QLabel(self)
        self.label.setGeometry(20,20,200,50)
        self.label.setText("Sepal_length: ")
        self.label.setStyleSheet("color: black;\
                                  font-size:15px")

        self.label=QLabel(self)
        self.label.setGeometry(20,50,200,50)
        self.label.setText("Sepal_width: ")
        self.label.setStyleSheet("color: black;\
                                  font-size:15px")

        self.label=QLabel(self)
        self.label.setGeometry(20,80,200,50)
        self.label.setText("Petal_length: ")
        self.label.setStyleSheet("color: black;\
                                  font-size:15px")

        self.label=QLabel(self)
        self.label.setGeometry(20,110,200,50)
        self.label.setText("Petal_length: ")
        self.label.setStyleSheet("color: black;\
                                  font-size:15px")

        # CREO LOS QLINEEDIT DONDE SE INTRODUCE LOS DATOS
        self.line_edit_1= QLineEdit(self)
        self.line_edit_1.setGeometry(150,30,160,25)

        self.line_edit_2= QLineEdit(self)
        self.line_edit_2.setGeometry(150,60,160,25)

        self.line_edit_3= QLineEdit(self)
        self.line_edit_3.setGeometry(150,90,160,25)

        self.line_edit_4= QLineEdit(self)
        self.line_edit_4.setGeometry(150,120,160,25)
        

        # CREO EL LABEL DONDE SE VA A MOSTRAR EL RESULTADO
        self.label1=QLabel(self)
        self.label1.setGeometry(180,160,200,50)
        self.label1.setText("")
        self.label1.setStyleSheet("color: black;\
                                  font-size:15px")

        
        # BOTON PARA CALCULAR PREDICION
        self.button=QPushButton(self)
        self.button.setGeometry(20,170,120,30) 
        self.button.setText("CALCULAR")
        self.button.setStyleSheet("background-color: blue;\
                                  color: black; font-size:15px")
        self.button.clicked.connect(self.calcular)

        # BOTON PARA VOLVER AL MENU
        self.button=QPushButton(self)
        self.button.setGeometry(40,250,240,30) 
        self.button.setText("VOLVER AL MENU PRINCIPAL")
        self.button.setStyleSheet("background-color: red;\
                                  color: black; font-size:15px")
        self.button.clicked.connect(self.cerrar)

        
    def calcular(self):

        df=pd.read_csv(MEDIA_ROOT)
        df.species=df.species.map({"setosa": 0, "versicolor":1,"virginica":2})
        X=df.drop(['species'],axis=1)
        X=np.array(X)
        y=np.array(df['species'])
        
        # ENTRENO Y CALCULO EL PORCENTAJE
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        clf=DecisionTreeClassifier()
        clf.fit(X_train,y_train)
        y_pre= clf.predict(X_test)
        # print(type(y_pre))
        acc=accuracy_score(y_test,y_pre)
        # print(acc)

        # RECUPERO LA INFORMACION DE LOS line_edit
        # print(self.line_edit_1.text())
        # print(type(self.line_edit_1.text()))
        v1=float(self.line_edit_1.text())
        v2=float(self.line_edit_2.text())
        v3=float(self.line_edit_3.text())
        v4=float(self.line_edit_4.text())
        lista=[v1, v2, v3, v4]

        # CALCULO LA ESPECIE CON LOS DATOS INTRODUCIDOS
        X_test=np.array(lista).reshape(1,-1)
        y_pre=clf.predict(X_test)
        # print(y_pre)    
        predicion=y_pre.__str__()
        if "0" in predicion:
            predicion="SETOSA"
        elif "1" in predicion:
            predicion="VERSICOLOR"
        elif "2" in predicion:
            predicion="VIRGINICA"

        
        # AÑADO EL RESULTADO AL LABEL CREEADO ANTES
        self.label1.setText(predicion)
        
        
    def cerrar(self):
        self.ventanaPrincipal = VentanaPrincipal()               
        self.ventanaPrincipal.show()                             
        self.hide()                                                  

class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)

        self.resize(350,500)
        self.setWindowTitle("APP PYQT5")
        self.setStyleSheet("background-color: blue;")

        self.label=QLabel(self)
        self.label.setGeometry(40,20,300,70)
        self.label.setText("BIENVENIDO A LA APLICACION PYQT5")
        self.label.setStyleSheet("color: black;\
                                  font-size:15px")

        # BOTONES MENU PRINCIPAL
        self.button = QPushButton(self)
        self.button.setGeometry(40,100,250,70) 
        self.button.setText("MOSTRAR PETAL IRIS")
        self.button.clicked.connect(self.mostrar_petal_iris)
        self.button.setStyleSheet("background-color: grey;\
                                  color: black; font-size:15px")

        self.button = QPushButton(self)
        self.button.setGeometry(40,200,250,70)
        self.button.setText("MOSTRAR SEPAL IRIS")
        self.button.clicked.connect(self.mostrar_sepal_iris) 
        self.button.setStyleSheet("background-color: grey;\
                                  color: black; font-size:15px")

        self.button = QPushButton(self)
        self.button.setGeometry(40,300,250,70)
        self.button.setText("CALCULAR PREDICION")
        self.button.clicked.connect(self.mostrar_predicion)
        self.button.setStyleSheet("background-color: grey;\
                                  color: black; font-size:15px")

        self.button = QPushButton(self)
        self.button.setGeometry(40,400,250,70)
        self.button.setText("SALIR")
        self.button.clicked.connect(self.salir)
        self.button.setStyleSheet("background-color: grey;\
                                  color: black; font-size:15px")


    def mostrar_petal_iris(self):
        # VentanaPrincipal()
        self.ventanaPetal=PetalIris()
        self.ventanaPetal.show()
        self.hide()

    def mostrar_sepal_iris(self):
        # VentanaPrincipal()
        self.ventanaSepal=SepalIris()
        self.ventanaSepal.show()
        self.hide()
    
    def mostrar_predicion(self):
        # VentanaPrincipal()
        self.ventanaPredicion=Predicion()
        self.ventanaPredicion.show()
        self.hide()
    
    def salir(self):
        self.close()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())
