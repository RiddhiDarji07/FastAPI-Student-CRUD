# Student CRUD API

## Project Description

This project is a Student CRUD API developed using FastAPI.

It allows users to create, read, update, and delete student records.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
student-crud/
     main.py
     requirements.txt
     models/
     routes/
     controllers/
```

## CRUD Operations

* Create a student
* Get all students
* Get a student by ID
* Update a student
* Delete a student

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/RiddhiDarji07/FastAPI-Student-CRUD
```

### 2. Open the project folder

```bash
cd student-crud
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Storage

Student data is stored in memory as implemented in Assignment 1.
