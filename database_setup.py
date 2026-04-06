import mysql.connector

def initialize_db():
    db = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )
    cursor = db.cursor()
    
    # Create Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
    cursor.execute("USE school_db")
    
    # Create Students Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            course VARCHAR(50)
        )
    """)
    
    # Create Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            record_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            date DATE DEFAULT (CURRENT_DATE),
            status ENUM('Present', 'Absent'),
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    """)
    
    print("Database and Tables initialized successfully.")
    db.close()

if __name__ == "__main__":
    initialize_db()
