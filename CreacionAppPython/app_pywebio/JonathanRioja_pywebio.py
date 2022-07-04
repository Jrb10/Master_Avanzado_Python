from pywebio.input import *
from pywebio.output import*

from pywebio import  config,start_server

import plotly.express as px
import pandas as pd

from model import Model


@config(theme='dark')
def main():
    put_text("BIENVENIDO A LA APP DE PYWEBIO")
    df = px.data.iris()

    def main_2(valor_boton):
        #------------------------------------
            # BOTON GRAFICA SEPAL IRIS
        #------------------------------------
        if valor_boton=='Grafica iris sepal':
            # CREO UN FIGURA CON PLOTY 
            fig = px.scatter(df, x=df["sepal_width"], y=df["sepal_length"], color="species",title="IRIS SEPAL")
            # fig.show() 
            # PARA QUE SE VEA EN PYWEBIO
            fig=fig.to_html(include_plotlyjs="require", full_html=False)
            put_html(fig)

        #------------------------------------
            # BOTON GRAFICA PETAL IRIS
        #------------------------------------              
        elif valor_boton=='Grafica iris petal':
            fig = px.scatter(df, x=df["petal_width"], y=df["petal_length"], color="species",title="IRIS PETAL")
            fig=fig.to_html(include_plotlyjs="require", full_html=False)
            put_html(fig)
        
        #------------------------------------
            # BOTON CALCULAR PREDICION
        #------------------------------------
        elif valor_boton=='Calcular predicion':
            # INPUT_GROUP PARA PEDIR LOS VALORES 
            data = input_group("Calcular Predicion Iris :", [
                input('sepal_length', name='sepal_length', type=FLOAT, required=True),                
                input('sepal_width', name='sepal_width', type=FLOAT, required=True), 
                input('petal_length', name='petal_length', type=FLOAT,required=True),
                input('petal_width', name='petal_width', type=FLOAT, required=True),
            ])
            # LLAMO AL METODO CALCULAR DE LA CLASE MODEL, DONDE LE ENVIO UNA CON LOS DATOS
            datos=[data['sepal_length'],data['sepal_width'],data['petal_length'],data['petal_width']]
            s=Model.calcular(datos)
            # MUESTRO CON LA VENTANA EMERGENTE POPUP EL STR QUE RETORNA EL METODO CALCULAR
            popup("EL RESULTADO ES :",s)

        #------------------------------------
            # BOTON FORMULARIO
        #------------------------------------
        else:
            # INPUT_GROUP PARA PEDIR LOS VALORES
            data = input_group("Formulario de Registro :", [
                input('Nombre', name='name', type=TEXT, required=True, 
                    PlaceHolder="name"),                
                input('Apellido', name='username', type=TEXT,
                    required=True, PlaceHolder="@username"),
                input('Edad', name='age', type=NUMBER, required=True,
                    PlaceHolder="age"),                
                input('Contraseña', name='pass', type=PASSWORD,
                    required=True, PlaceHolder="Password"),                
                input('Confirmar Contraseña', name='passes', type=PASSWORD,
                    required=True, PlaceHolder="Confirm Password"),                
                select('Lenguaje', name='languaje', options=['Java','C++','Python'],
                        required=True) ,
                radio("Sexo", name='sexo', options=['Hombre', 'Mujer'], required=True),
                checkbox("¿ Estás trabajando ahora ?", name='trabajo', options=["SI","NO"], required=True)                
            ], validate=Model.validar_formulario, cancelable=True)

            popup("FORMULARIO :",f'''\n
                    NAME : {data['name']}\n
                    USERNAME : {data['username']}\n
                    AGE: {data['age']}\n
                    PASWORD: {data['pass']}\n
                    LANGUAJE: {data['languaje']}\n
                    Sexo: {data['sexo']}\n
                    Trabajo: {data['trabajo']}
                ''')

    # BOTONES PARA ELEGIR QUE HACER Y UNA IMAGEN
    put_buttons(['Grafica iris sepal','Grafica iris petal','Calcular predicion','Formulario'], onclick=main_2)    
    put_image('https://www.python.org/static/img/python-logo.png')
    

if __name__ == '__main__':
    start_server(main, port=8081, debug=True)