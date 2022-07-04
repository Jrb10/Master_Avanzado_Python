# INSTALACIONES

pip install fastapi

pip install uvicorn[standard]

pip install pandas

pip install scikit-learn


pip freeze > requirements.txt

pip install -r requirements.txt

# EJECUTAR APP

uvicorn JonathanRioja_fastAPI:app --reload

http://127.0.0.1:8000/docs

ELEGIMOS EL METODO 
HACEMOS CLIC EN TRY II OUT
LUEGO DAMOS A EXECUTE

# INSERTAR 

{
  "Name": "jj",
  "Pclass": "jj",
  "Age": 0,
  "Sex": "jj",
  "Survived": 0
}

# ACTUALIZAR 

PONER ID 

{
  "Name": "jj",
  "Pclass": "jj",
  "Age": 0,
  "Sex": "jj",
  "Survived": 0
}

# ELIMINAR 

PONER ID 


# PREDECIR

HAY QUE INSERTAR:
Pclass: OPCIONES: 1,2,3
Age: 
Sex: OPCIONES: 0 QUE ES FEMALE
               1 QUE ES MALE

