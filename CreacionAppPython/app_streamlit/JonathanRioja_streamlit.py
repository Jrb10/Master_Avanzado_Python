import streamlit as st
import pandas as pd
import quandl 
import yfinance as yf

import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from io import StringIO

st.set_page_config(
     page_title="APP STREAMLIT",
     page_icon="🦈",
     layout="wide",
     initial_sidebar_state="expanded"
)
st.title("APP STREAMLIT")



     
#----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Sidebar --- BARRA LATERAL
#-----------------------------------------------------------------------
#----------------------------------------------------------------------
sidebar = st.sidebar
sidebar.header("OPCIONES QUE PUEDES HACER:")


#----------------------------------------------------------------------
#----------------------------------------------------------------------
# SIDEBAR PARA EMPRESAS
# LEO EL ARCHIVO CSV PARA SACAR LAS EMPRESAS
# UTIZO UN SELECTBOX PARA LAS EMPRESAS Y SLIDER PARA EL AÑO
sidebar.subheader("1-VER INFORMACION DE EMPRESAS")
df_empresas=pd.read_csv('WIKI_PRICES.csv')
empresas=df_empresas['ticker']
empresa =sidebar.selectbox("ELIGE LA EMPRESA ",  empresas )
año=sidebar.slider("ELIGE EL PERIODO DE AÑO", 2014 , 2018 , 2014)

#----------------------------------------------------------------------
# CHECKBOX PARA PODER NO MOSTRAR LA INFORMACION EMPRESA QUE ESTA POR DEFECTO EN TRUE
if sidebar.checkbox('VER INFORMACION DE LA EMPRESA',True):
    
    st.header("DATOS FINANCIEROS")
    st.write(f" HAS ELEGIDO LA EMPRESA : {empresa} DESDE 2014-{año}")
    
    # OPCIONES PARA SACAR INFO -- QUANDL O YFINANCE
    data= quandl.get(f'WIKI/{empresa}', start_date='2014-1-1', end_date=f'{año}-12-31')
    # data= yf.download(empresa, '2014-1-1', f'{año}-12-31')
    
    # EMPRESAS COMO AAMC - NO HAY DATOS EN ESAS FECHAS
    # data= yf.download('AAMC')
    # st.write(data)
    if data.empty:
        st.warning("NO EXISTE BUSQUEDA PAPRA ESE FILTRADO, PRUEBA OTRA INFORMACION")
    else:
        st.write(data)
        x=st.selectbox("QUE COLUNMA QUIERES VER", data.columns.values)
        st.write(data[x])
        st.bar_chart(data[x])
        



#----------------------------------------------------------------------
#----------------------------------------------------------------------
# SIDEBAR PARA IRIS
sidebar.subheader("2-VER IRIS DATASET")

# METODO PARA CALCULAR LA PREDICION CON LOS DATOS 
def calcular(datos):
    # LEO EL CSV Y SEPARO X E Y 
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
    #print(acc)

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
    # markdown para resaltar la respuesta
    st.markdown(f'La especie seria : **{predicion}**')

# UTIZO UN RADIO PARA MOSTRAR O NO EL IRIS, POR DEFECTO LO DEJO EN NO
radio=sidebar.radio('¿ QUIERES VERLO ? ',  ('NO','SI')  )
if radio=="SI":
    st.write()
    st.header("IRIS DATASET")
    df=pd.read_csv("iris.csv")
    st.write(df)

    # GRAFICO SEPAL IRIS
    # UTILIZO CHECKBOX PARA MOSTRAR GRAFICO SEPAL -- DEFECTO EN TRUE
    ver_figura = st.checkbox("VER GRAFICO SEPAL", value=True)
    if ver_figura:
        versicolor=df[df.species=="versicolor"]
        setosa=df[df.species=="setosa"]
        virginica=df[df.species=="virginica"]
        fig, ax = plt.subplots()
        ax.scatter(versicolor["sepal_length"], versicolor["sepal_width"], label="versicolor", facecolor="green")
        ax.scatter(setosa["sepal_length"], setosa["sepal_width"], label="setosa",facecolor="blue")
        ax.scatter(virginica["sepal_length"], virginica["sepal_width"], label="virginica",facecolor="red")
        ax.set_xlabel("Sepal_length")
        ax.set_ylabel("Sepal_width")
        ax.set_title("Iris Sepal Sizes")
        ax.legend(loc='upper left')

        st.pyplot(fig)

    # UTILIZO CHECKBOX PARA CALCULAR LA PREDICION -- DEFECTO EN FALSE
    calcular_predicion = st.checkbox("CALCULAR PREDICION", value=False)
    if calcular_predicion:
        sepal_length=st.number_input('Sepal_length : ')
        sepal_width=st.number_input('Sepal_width : ')
        petal_length=st.number_input('Petal_length : ')
        petal_width=st.number_input('Petal_width : ')
        datos=[sepal_length, sepal_width, petal_length, petal_width]

        if st.button("Calcular"):
            calcular(datos)


#----------------------------------------------------------------------
#----------------------------------------------------------------------
# SIDEBAR PARA ABRIR ARCHIVO
sidebar.subheader("3-ABRIR UN ARCHIVO")
radio1=sidebar.radio('¿ QUIERES ABRIRLO ? ',  ('NO','SI')  )
if radio1=="SI":
    uploaded_file = sidebar.file_uploader("Elige un archivo")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write("DATAFRAME DEL ARCHIVO ELEGIDO: ")
        st.write(dataframe)