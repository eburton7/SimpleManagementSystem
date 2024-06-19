# Public Health Data Management System

## Overview
This project is a super simple web application for managing and visualizing public health data. It demonstrates skills in relational databases, SQL, Python (Flask), CSS, JavaScript, and user experience design again at a super simple small level.

## Features
- Relational database using SQLite
- CRUD operations for managing patients' data
- User-friendly forms for data entry
- Responsive frontend using HTML, CSS, and JavaScript
- Backend using Flask

## How to Run
1. **Clone the repository:**
    ```sh
    git clone
    cd managementSystem
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Initialize the database:**
    ```sh
    python init_db.py
    ```

5. **Run the Flask application:**
    ```sh
    python app.py
    ```

6. **Open your browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

## Example SQL Queries
- Retrieve all patients:
    ```sql
    SELECT * FROM Patients;
    ```

## Technologies Used
- Python (Flask)
- SQLite
- HTML
- CSS
- JavaScript

## Author
- Elysia Burton
