from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect('database/health_data.db')
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients', methods=['GET'])
def get_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    conn.close()
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient():
    new_patient = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Patients (Name, Age, Gender) VALUES (?, ?, ?)",
                   (new_patient['name'], new_patient['age'], new_patient['gender']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Patient added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=False)  