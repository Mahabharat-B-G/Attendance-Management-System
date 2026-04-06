from attendance_logic import add_student, mark_attendance

def menu():
    while True:
        print("\n--- Student Attendance System ---")
        print("1. Add New Student")
        print("2. Mark Attendance")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            sid = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            print(add_student(sid, name, course))
            
        elif choice == '2':
            sid = int(input("Enter Student ID: "))
            status = input("Status (Present/Absent): ").capitalize()
            print(mark_attendance(sid, status))
            
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
