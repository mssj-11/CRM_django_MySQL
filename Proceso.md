



Crear el entorno virtual con el nombre **venv**
```sh
virtualenv venv
```
Ingresando a la carpeta, Activando el entorno virtual
```sh
.\venv\Scripts\activate
```
Desactivar el entorno virtual:
```sh
deactivate
```

#   Instalación de Django y MySQL
```sh
pip install django
```
```sh
pip install mysql
```
```sh
pip install mysql-connector-python
```
```sh
pip install mysql-connector
```

#  Crear el proyecto
Ejemplo: `django-admin startproject NOMBRE_DEL_PROYECTO`
```sh
django-admin startproject crm
```

##  Ingresar al proyecto
```sh
cd crm/
```

##  Iniciar el proyecto
```sh
python manage.py runserver
```


