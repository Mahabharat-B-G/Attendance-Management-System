import tkinter as tk
from tkinter import messagebox, ttk
from attendance_logic import add_student, mark_attendance

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Attendance System")
        self.root.geometry("400x450")
        self.root.configure(padx=20, pady=20)

        # --- UI Elements: Add Student Section ---
        tk.Label(root, text="Add New Student", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(root, text="Student ID:").pack()
        self.ent_sid = tk.Entry(root)
        self.ent_sid.pack()

        tk.Label(root, text="Name:").pack()
        self.ent_name = tk.Entry(root)
        self.ent_name.pack()

        tk.Label(root, text="Course:").pack()
        self.ent_course = tk.Entry(root)
        self.ent_course.pack()

        tk.Button(root, text="Register Student", command=self.handle_add, bg="#4CAF50", fg="white").pack(pady=10)

        ttk.Separator(root, orient='horizontal').pack(fill='x', pady=10)

        # --- UI Elements: Attendance Section ---
        tk.Label(root, text="Mark Attendance", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(root, text="Status:").pack()
        self.status_var = tk.StringVar(value="Present")
        tk.OptionMenu(root, self.status_var, "Present", "Absent").pack()

        tk.Button(root, text="Submit Attendance", command=self.handle_attendance, bg="#2196F3", fg="white").pack(pady=10)

    def handle_add(self):
        try:
            sid = int(self.ent_sid.get())
            name = self.ent_name.get()
            course = self.ent_course.get()
            
            if not name or not course:
                raise ValueError("Fields cannot be empty")
                
            msg = add_student(sid, name, course)
            messagebox.showinfo("Success", msg)
            self.clear_entries()
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    def handle_attendance(self):
        try:
            sid = int(self.ent_sid.get())
            status = self.status_var.get()
            msg = mark_attendance(sid, status)
            messagebox.showinfo("Attendance", msg)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid Student ID first.")

    def clear_entries(self):
        self.ent_sid.delete(0, tk.END)
        self.ent_name.delete(0, tk.END)
        self.ent_course.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
