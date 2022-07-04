import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# INSTALACIONES NECESARIAS
# pip install pandas
# pip install matplotlib

def mes_gastado(data):
    '''
        Guardo en s , el resultado de la suma de gastos(-) y ganancias (+)
        Con la funcion idxmin() me devuelve la columna donde esta el valor minimo
        Con la funcion min() me devuelve el valor minimo
    '''
    s=data.sum(axis=0)
    # print(data.sum(axis=0)) #<class 'pandas.core.series.Series'>
    month=s.idxmin()
    money=s.min()
    money=abs(money)
    print(f"El mes de {month} has gastado {money}")
    
    
    '''
       Segunda opcion , aunque nose si esta bien usar for con pandas
       Mes gastado mas  ---> valores positivos== ingresos | valores negativos== gastos
       resumen_dinero -- Guardo los datos de la suma de gastos y ganancias en un diccionario
       gasto_maximo -- el valor mas negativo (tras la suma de gastos y ganancias)
       por lo ultimo recorro el diccionario para saber que mes tiene ha tenido mayor gasto
    '''
    
    # resumen_dinero=dict(data.sum(axis=0))
    # gasto_maximo=min(data.sum(axis=0))
    # for mes,dinero in resumen_dinero.items():
    #     if dinero==gasto_maximo:
    #         print(f"El mes de {mes} has gastado {gasto_maximo}")
            
def mes_ahorrado(data):
    '''
        Guardo en s , el resultado de la suma de gastos(-) y ganancias (+)
        Con la funcion idxmax() me devuelve la columna donde esta el valor maximo
        Con la funcion max() me devuelve el valor maximo
    '''
    s=data.sum(axis=0)
    # print(data.sum(axis=0)) #<class 'pandas.core.series.Series'>
    month=s.idxmax()
    money=s.max()
    money=abs(money)
    print(f"El mes de {month} has ahorrado {money}")


def media_gastos(data):
    '''
       ---> valores positivos== ingresos | valores negativos== gastos

       dinero_mes -- Guardo los datos de la suma de gastos y ganancias
       y con el metodo mean() calculo la media del dinero
    '''
    dinero_mes=(data.sum(axis=0))
    dinero_media=dinero_mes.mean()
    if dinero_media<0:
        print(f'La media sale en perdidas: {dinero_media}')
    else:
        print(f'La media sale en ganancias: {dinero_media}')


def gasto_total(data):

    '''
        Guardo en un datafram los valores negativos
        Reemplazo los valores nan por 0
        Guardo en un lista la suma de valores positivos de cada mes
        Y con la funcion sum() sumo los valores 
    '''
    df=data[data[data.columns.values]<0]
    df=df.fillna(0)
    # print(df)
    gastos_mes=list(df.sum(axis=0))
    # print(gastos_mes) 
    gastos=sum(gastos_mes)
    gastos=abs(gastos)
    print(f'Durante todo el año has gastado {gastos}')

    '''
        Segunda opcion:
        Recorrer cada columna y por cada columna añadir a la lista los valores negativos
        y con la funcion sum() sumar los gastos
    '''
    # gastos1=[]
    # for col in data.columns:
    #     for value in data[col]:
    #         if value<0:
    #             gastos1.append(value)
    # gastos_final=sum(gastos1)
    # print("gastos")
    # print(gastos_final)
         

def ingresos_total(data):
    '''
        Guardo en un datafram los valores positivos
        Reemplazo los valores nan por 0
        Guardo en un lista la suma de valores positivos de cada mes
        Y con la funcion sum() sumo los valores 
    '''
    
    df=data[data[data.columns.values]>0]
    df=df.fillna(0)
    # print(df)
    ganancias_mes=list(df.sum(axis=0))
    # print(ganancias_mes) 
    ingresos=sum(ganancias_mes)
    print(f'Durante todo el año has ganado {ingresos}')

def grafico(data):
    '''
        Creo el grafico con matplotlib
        x= los meses, reduzco los meses a 3 letras
        y= el rango de ganancias o perdidas 
        color -- azul si ha habido ganancias y rojo perdidas
    '''
    fig= plt.figure() 
    ax=fig.add_subplot(111)
    x=[]
    meses=data.columns.values
    for m in meses:
        x.append(m[0:3])
    y=data.sum(axis=0)
    colors = ["red" if i < 0 else "blue" for i in y]
    ax.bar(x,y, color=colors)
    plt.title('GANANCIAS O PERDIDAS POR MES')
    plt.show()
 

def change_data(data):
    '''
        Con data.info--- compruebo si hay valores nulos
        Compruebo el tipo de datos de cada columna ---data.dtypes
        Modico por index y columna con loc los valores erroneos
        Y con pd.to_numeric() convierto a int para poder calcular los datos del apartado 1
        Devuelvo el df cambiado 
    '''
    # print(data.info())
    # print(data.dtypes)
    
    try:
        # list, tuple, 1-d array, or Series
        # if type(data.values) != 'list':
        #     raise ValueError("DATOS INCORRECTOS")

        

        data.loc[63,'Enero']='-541'
        data.loc[59,'Julio']='-602'
        data.loc[43,'Septiembre']='0'
        data.loc[50,'Octubre']='0'
        data.loc[90,'Noviembre']='0'
        
        # para pd.to_numeric
        df1=data
        df1=df1.apply(pd.to_numeric)
        print(df1.info())
        
        # for col in df1.columns:
        #     # print(df1[col])
        #     df1[col] = pd.to_numeric(df1[col])
        
        # print(df1.info())
        
        data['Enero']=pd.to_numeric(data['Enero'])
        data['Julio']=pd.to_numeric(data['Julio'])
        data['Septiembre']=pd.to_numeric(data['Septiembre'])
        data['Octubre']=pd.to_numeric(data['Octubre'])
        data['Noviembre']=pd.to_numeric(data['Noviembre'])    




        # data=data[data==-760]
        # data=data.fillna(0)
        # print(data)






        # PARA SABER EN QUE MES TENGO UN GASTO DE -760 
        print(" RESUMEN DEL DATAFRAME ")
        print(data.head())
        mes=data[data.values==15]
        print(mes)
        mes=mes.T
        print(mes)
        print(mes.columns.values)
        # me=mes.index[(mes[0] == -760)].tolist()
        meses=[]
        
        
            
        
        # print(mes.index.tolist())
        print(" MES DONDE TUVE UN GASTO DE -760")
        # print(me) # ENERO -- SERIA LA SOLUCION
        
        # print(type(mes.columns.values))
        # if mes.columns.values[mes.values==-760]:
        #     print(mes.columns.values)
        
        # mes=data.columns[data.values==-760]
        # print(mes)

        return data
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)

def main():
    '''
        Uso del try expcept para cargar el el fichero y comprobar que existe
        comprobacion de que hay 12 columnas con raise
        Con .info() - compruebo que los valores de cada columna no son nulos
        y tambien el tipo de datos en cada columna
        Change_data cambio los valores que estan mal en el df
    '''
    try:
        filename="finanzas2020[1].csv"
        df= pd.read_csv(filename, sep='\t')
        # print("existe el fichero")
        if len(df.columns)!=12:
            raise AssertionError
        # print(df.info())
        data=change_data(df)
        # print(data.info())
        print("Menu: ")
        seguir=True
        while seguir:
            try:
                print('''
                        1- ¿Qué mes se ha gastado más?
                        2- ¿Qué mes se ha ahorrado más?
                        3- ¿Cuál es la media de gastos al año?
                        4- ¿Cuál ha sido el gasto total a lo largo del año?
                        5- ¿Cuáles han sido los ingresos totales a lo largo del año?
                        6- Grafico
                        7- Salir ''')
                opcion=int(input("---->"))
                if opcion==1:
                    mes_gastado(data)
                elif opcion==2:
                    mes_ahorrado(data)
                elif opcion==3:
                    media_gastos(data)
                elif opcion==4:
                    gasto_total(data)  
                elif opcion==5:
                    ingresos_total(data)  
                elif opcion==6:
                    grafico(data)    
                elif opcion==7:
                    print("Hasta luego")
                    seguir=False
                else:
                    print("Tienes que elegir un numero del 1 al 7")
            except ValueError:
                print("Eige un un numero")
                     
    except IOError:
        print("FICHERO NO EXISTE")
    except FileNotFoundError:
        return False


if __name__ == '__main__':
    main()