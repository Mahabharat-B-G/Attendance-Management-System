import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="school_db"
    )

def add_student(sid, name, course):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO students (student_id, name, course) VALUES (%s, %s, %s)", (sid, name, course))
        db.commit()
        return "Student added successfully!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        db.close()

def mark_attendance(sid, status):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO attendance (student_id, status) VALUES (%s, %s)", (sid, status))
        db.commit()
        return "Attendance recorded!"
    except Exception as e:
        return f"Error: {e}"
    finally:
        db.close()
