import psycopg2
from flask import Flask, render_template

# Update the connection details
conn = psycopg2.connect(
        host="ulugbek1.crqq8yy40wh8.us-east-1.rds.amazonaws.com",  # RDS endpoint
        dbname="test",  # Default database name for RDS
        user="postgres",  # RDS username
        password="your_password",  # RDS password
        port="5432"  # Port for PostgreSQL
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Drop the table if it exists
cur.execute("DROP TABLE IF EXISTS courses;")

# Create the courses table
cur.execute('''
    CREATE TABLE courses (
        id SERIAL PRIMARY KEY,
        course_code VARCHAR(10) NOT NULL,
        course_name VARCHAR(255) NOT NULL,
        student_level VARCHAR(50) NOT NULL,
        day_of_week VARCHAR(50) NOT NULL,
        time VARCHAR(50) NOT NULL
    );
''')

# Insert data into the courses table
cur.execute('''
    INSERT INTO courses (course_code, course_name, student_level, day_of_week, time)
    VALUES 
    ('CS101', 'Data Structures', 'Undergraduate', 'Monday', '10:00 AM'),
    ('CS102', 'Operating Systems', 'Undergraduate', 'Tuesday', '1:00 PM'),
    ('CS103', 'Algorithms', 'Graduate', 'Wednesday', '3:00 PM'),
    ('CS104', 'Advanced Databases', 'Graduate', 'Thursday', '2:00 PM'),
    ('CS105', 'AI Fundamentals', 'Undergraduate', 'Friday', '11:00 AM');
''')

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()

# Flask application setup
app = Flask(__name__)

# Function to get a database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="ulugbek1.crqq8yy40wh8.us-east-1.rds.amazonaws.com",  # RDS endpoint
        dbname="postgres",  # Default database name
        user="postgres",  # RDS username
        password="your_password",  # RDS password
        port="5432"  # Port
    )
    return conn

# Define the index route
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM courses;')  # Query to fetch all courses
    courses = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', courses=courses)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
