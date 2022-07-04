# #                     INSTALACIONES

pip install dash

pip install pandas

pip install quandl

pip install notebook

# para utilizarlo: jupyter notebook

pip install jupyter-dash


pip install nasdaq-data-link
# PARA QUE NO TENGA LIMITE DE INTENTOS

# import nasdaqdatalink

# quandl.ApiConfig.api_key = '<YOUR_API_KEY>'

pip freeze > requirements.txt

pip install -r requirements.txt


# #              FUNCION DE LOS 2 ARCHIVOS

Adjunto el csv descargado de : https://data.nasdaq.com/databases/WIKIP/documentation
He escogido algunas empresas al azar

HACEN LO MISMO LO UNICO QUE CAMBIA :

    app.run_server(mode="inline")
    app.run_server(mode="external")

dcc.DatePickerRange - lo utilzo para la fecha

dcc.Dropdown - lo utilzo para elegir la empresa 

app.callback - recoger la fecha y la empresa
             - para devolver el grafico 

