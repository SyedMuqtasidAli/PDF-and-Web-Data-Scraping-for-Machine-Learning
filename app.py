from flask import Flask, render_template, jsonify, send_file
import pandas as pd
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='ezline'
)

# Function to fetch data from a specific table and save it to an Excel file
def fetch_and_save_to_excel(table_name, excel_file_name):
    query = f'SELECT * FROM {table_name};'
    df = pd.read_sql(query, connection)
    df.to_excel(excel_file_name, index=False)

# API Endpoint for Downloading PDF Data
@app.route('/api/download_pdf_data', methods=['GET'])
def download_pdf_data():
    try:
        # Fetch data from pdf_data_table and save it to Excel
        fetch_and_save_to_excel('pdf_data_table', 'downloaded_pdf_data.xlsx')
        return send_file('downloaded_pdf_data.xlsx', as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint for Downloading Web Data
@app.route('/api/download_web_data', methods=['GET'])
def download_web_data():
    try:
        # Fetch data from web_data_table and save it to Excel
        fetch_and_save_to_excel('web_data_table', 'downloaded_web_data.xlsx')
        return send_file('downloaded_web_data.xlsx', as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Home Page with Buttons
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
