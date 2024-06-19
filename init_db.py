import sqlite3
import os

os.makedirs('database', exist_ok=True)

conn = sqlite3.connect('database/health_data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    PatientID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Gender TEXT
)
''')

conn.commit()
conn.close()
