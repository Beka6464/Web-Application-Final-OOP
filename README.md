Final Project
Operating Systems Course
University Schedule Management System

This project is a web application for managing and displaying course information from a PostgreSQL database. It includes a backend built with Python (using Flask) and a frontend designed with HTML and CSS.

Project Overview
The application allows users to:

View course details such as course name, code, description, level (Undergraduate/Graduate), and credits.
Filter courses by their level.
Interact with a user-friendly, responsive interface to browse the schedule efficiently.
Technologies Used:

Backend: Flask (Python) with psycopg2 for database interaction.
Frontend: HTML, CSS, and JavaScript.
Database: PostgreSQL for storing course details.
Database Setup
Create the Database:
Run the following SQL command:

sql
CREATE DATABASE university_schedule;
Create the Table:
Define the structure for storing course data:

sql
CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    location TEXT,
    level VARCHAR(20),
    credits INTEGER
);
Insert Data:
Populate the table with initial course data:

sql
INSERT INTO courses (code, name, location, level, credits) VALUES
('CS101', 'Data Structures', 'Webster Univ Tashkent, Uzbekistan', 'Undergraduate', 3),
('CS102', 'Operating Systems', 'Webster Univ Tashkent, Uzbekistan', 'Undergraduate', 3),
('CS103', 'Algorithms', 'Webster Univ Tashkent, Uzbekistan', 'Graduate', 3),
('CS104', 'Advanced Databases', 'Webster Univ Tashkent, Uzbekistan', 'Graduate', 4),
('CS105', 'AI Fundamentals', 'Webster Univ Tashkent, Uzbekistan', 'Undergraduate', 4);
Application Setup
Install Dependencies:
Install required libraries using:

bash
pip install flask psycopg2
Run the Application:
Start the Flask server and access the application via your browser.

Author
Beka Sharipov
Computer Science & Business Administration
11.12.2024

