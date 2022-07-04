# INSTALACIONES
pip install Flask

pip install pandas

pip install scikit-learn



# EJECUTAR LA APP
set FLASK_APP=JonathanRioja_flask
set FLASK_ENV=development
flask run

# PARA INSERTAR 

{
    "petal_length": 5.0,
    "petal_width": 1.9,
    "sepal_length": 6.3,
    "sepal_width": 2.5,
    "species": "virginica"
}

# PARA ACTUALIZAR 
{
    "id": 150 ,
    "sepal_length": 102,
    "sepal_width": 100,
    "petal_length": 100,
    "petal_width": 100,
    "species":"virginica"
}

# PARA BORRAR
{
    "id": 154
} 

# PARA PREDECIR LA ESPECIE
{
    "sepal_length": 6.9,
    "sepal_width": 3.2,
    "petal_length": 4.4,
    "petal_width": 1.5
}
