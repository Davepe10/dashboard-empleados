import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_from_directory

# Conectar a la base de datos MySQL
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # servidor local
            user="root",  # usuario por defecto de MySQL
            password="Javieralexander0210",  # contraseña
            database="planilla_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Obtener datos de la base de datos
def get_data_from_db():
    connection = connect_to_db()
    if connection is None:
        return pd.DataFrame()  # Retornar un DataFrame vacío en caso de error
    query = "SELECT * FROM empleados"
    resultado = pd.read_sql(query, connection)
    connection.close()
    return resultado

# Gráfico de barras Edad vs Salario
def plot_bar_chart(data):
    plt.figure(figsize=(10, 5))
    plt.bar(data['edad'], data['salario'], color='blue')
    plt.xlabel('Edad')
    plt.ylabel('Salario')
    plt.title('Relación Edad-Salario')
    plt.savefig('graficos/edad_vs_salario.png')
    plt.close()

# Gráfico circular por Ciudad
def plot_pie_chart(data):
    city_counts = data['ciudad'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución por Ciudad')
    plt.savefig('graficos/ciudad_distribution.png')
    plt.close()

# Aplicación Flask
app = Flask(__name__)

@app.route('/graficos/<path:filename>')
def graficos(filename):
    return send_from_directory('graficos', filename)

@app.route('/')
def dashboard():
    data = get_data_from_db()
    if data.empty:
        return "No se pudieron obtener datos de la base de datos.", 500

    plot_bar_chart(data)  # Genera gráfico de barras
    plot_pie_chart(data)  # Genera gráfico circular
    return render_template('index.html', tables=[data.to_html(classes='table table-striped')], titles=['Empleados'])

if __name__ == '__main__':
    app.run(debug=True, port=5001)
