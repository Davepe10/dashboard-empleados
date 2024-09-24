# Dashboard de Empleados

Este proyecto es un dashboard interactivo que muestra la relación entre la edad y el salario de empleados, así como una distribución de empleados por ciudad. Utiliza Flask para el backend y se conecta a una base de datos MySQL para obtener los datos.

## Tabla de Contenidos
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características
- Visualización de gráficos de barras que representan la relación entre edad y salario.
- Gráfico circular que muestra la distribución de empleados por ciudad.
- Tabla que lista todos los empleados con sus respectivos datos.

## Requisitos
- Python 3.x
- MySQL
- Las siguientes bibliotecas de Python:
  - `Flask`
  - `mysql-connector-python`
  - `pandas`
  - `matplotlib`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Davepe10/tu-repo.git
   cd tu-repo


## Crea un entorno virtual y actívalo:Crea un entorno virtual y actívalo:

python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate


## Instale las dependencias necesarias:
pip install Flask mysql-connector-python pandas matplotlib

## Configurar la base de datos:

Asegúrese de tener MySQL instalado y en ejecución.
Crea una base de datos de llamada planilla_db.
Crea una tabla empleadoscon las columnas necesarias ( edad, `salarisalario, ciudad, etc.).
Inserta algunos datos de prueba en la tabla.
Crea la carpeta graficosen la raíz del proyecto para almacenar las imágenes generadas.


## Ejecuta la aplicación Flask:

python app.py

Abra un navegador web y visite http://localhost:5001para ver el tablero.


