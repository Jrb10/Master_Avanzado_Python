# #                                     INSTALACIONES
pip install streamlit

pip install quandl
pip install yfinance

pip install matplotlib
pip install scikit-learn

pip freeze > requirements.txt

pip install -r requirements.txt

# #                                     EJECUTAR APP 
streamlitenv\Scripts\activate
streamlit run JonathanRioja_streamlit.py

# #                                     RESUMEN APP 
Cuenta con menu lateral te muestra las empresas sacadas del archivo wiki_prices.csv,
donde saco la informacion mediante quandl o yfinance,
y te muestra el df , la columna que quieres ver y el grafico

Tambien puedes ver el df de iris.csv
Te muestra el grafico de sepal iris
Puedes predecir insertando datos la especie

Por ultimo si quieres ver otro archivo, tambien esta la opcion del abrir y ver df
 