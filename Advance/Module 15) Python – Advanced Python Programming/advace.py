import tkinter as tk
from tkinter import messagebox
import sqlite3, re, datetime, os

def init_db():
    conn = sqlite3.connect("meditrack.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            disease TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS appointments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor TEXT,
            date TEXT,
            notes TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS billing(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            amount REAL,
            medicines TEXT,
            tax REAL,
            total REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
    
    def save(self):
        conn = sqlite3.connect("meditrack.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO patients(name, age, disease) VALUES (?, ?, ?)",
                    (self.name, self.age, self.disease))
        conn.commit()
        conn.close()

class Appointment:
    def __init__(self, patient_id, doctor, date, notes):
        self.patient_id = patient_id
        self.doctor = doctor
        self.date = date
        self.notes = notes

    def save(self):
        conn = sqlite3.connect("meditrack.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO appointments(patient_id, doctor, date, notes) VALUES (?, ?, ?, ?)",
                    (self.patient_id, self.doctor, self.date, self.notes))
        conn.commit()
        conn.close()

class Billing:
    def __init__(self, patient_id, amount, medicines, tax=0.05):
        self.patient_id = patient_id
        self.amount = amount
        self.medicines = medicines
        self.tax = tax
        self.total = amount + (amount * tax)

    def save(self):
        conn = sqlite3.connect("meditrack.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO billing(patient_id, amount, medicines, tax, total, date) VALUES (?, ?, ?, ?, ?, ?)",
                    (self.patient_id, self.amount, self.medicines, self.tax, self.total, str(datetime.date.today())))
        conn.commit()
        conn.close()

        filename = f"invoice_patient_{self.patient_id}.txt"
        with open(filename, "w") as f:
            f.write(f"--- MediTrack Invoice ---\n")
            f.write(f"Patient ID: {self.patient_id}\n")
            f.write(f"Medicines: {self.medicines}\n")
            f.write(f"Amount: {self.amount}\n")
            f.write(f"Tax: {self.tax*100}%\n")
            f.write(f"Total: {self.total}\n")
            f.write(f"Date: {datetime.date.today()}\n")

def add_patient():
    try:
        name = entry_name.get()
        age = int(entry_age.get())
        disease = entry_disease.get()

        if not name or not disease:
            raise ValueError("Fields cannot be empty!")

        p = Patient(name, age, disease)
        p.save()
        messagebox.showinfo("Success", f"Patient {name} added.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_appointment():
    try:
        pid = int(entry_pid.get())
        doctor = entry_doctor.get()
        date = entry_date.get()
        notes = entry_notes.get()

        a = Appointment(pid, doctor, date, notes)
        a.save()
        messagebox.showinfo("Success", f"Appointment added for Patient ID {pid}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_bill():
    try:
        pid = int(entry_bpid.get())
        amount = float(entry_amount.get())
        meds = entry_meds.get()

        b = Billing(pid, amount, meds)
        b.save()
        messagebox.showinfo("Success", f"Bill generated for Patient {pid}\nSaved as text file.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_patient():
    pattern = entry_search.get()
    conn = sqlite3.connect("meditrack.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    results = cur.fetchall()
    conn.close()

    matches = [str(r) for r in results if re.search(pattern, str(r), re.IGNORECASE)]
    if matches:
        messagebox.showinfo("Search Results", "\n".join(matches))
    else:
        messagebox.showinfo("Search Results", "No match found.")


def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    roles = {"admin":"admin123", "doctor":"doc123", "reception":"rec123"}

    if user in roles and roles[user] == pwd:
        login_win.destroy()
        launch_main_gui(user)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")


def launch_main_gui(role):
    root = tk.Tk()
    root.title(f"MediTrack - Logged in as {role}")


    tk.Label(root, text="Add Patient").grid(row=0, column=0, columnspan=2)
    tk.Label(root, text="Name").grid(row=1, column=0)
    tk.Label(root, text="Age").grid(row=2, column=0)
    tk.Label(root, text="Disease").grid(row=3, column=0)

    global entry_name, entry_age, entry_disease
    entry_name, entry_age, entry_disease = tk.Entry(root), tk.Entry(root), tk.Entry(root)
    entry_name.grid(row=1, column=1)
    entry_age.grid(row=2, column=1)
    entry_disease.grid(row=3, column=1)

    tk.Button(root, text="Add Patient", command=add_patient).grid(row=4, column=0, columnspan=2)

   
    tk.Label(root, text="Add Appointment").grid(row=5, column=0, columnspan=2)
    tk.Label(root, text="Patient ID").grid(row=6, column=0)
    tk.Label(root, text="Doctor").grid(row=7, column=0)
    tk.Label(root, text="Date").grid(row=8, column=0)
    tk.Label(root, text="Notes").grid(row=9, column=0)

    global entry_pid, entry_doctor, entry_date, entry_notes
    entry_pid, entry_doctor, entry_date, entry_notes = tk.Entry(root), tk.Entry(root), tk.Entry(root), tk.Entry(root)
    entry_pid.grid(row=6, column=1)
    entry_doctor.grid(row=7, column=1)
    entry_date.grid(row=8, column=1)
    entry_notes.grid(row=9, column=1)

    tk.Button(root, text="Add Appointment", command=add_appointment).grid(row=10, column=0, columnspan=2)


    tk.Label(root, text="Billing").grid(row=11, column=0, columnspan=2)
    tk.Label(root, text="Patient ID").grid(row=12, column=0)
    tk.Label(root, text="Amount").grid(row=13, column=0)
    tk.Label(root, text="Medicines").grid(row=14, column=0)

    global entry_bpid, entry_amount, entry_meds
    entry_bpid, entry_amount, entry_meds = tk.Entry(root), tk.Entry(root), tk.Entry(root)
    entry_bpid.grid(row=12, column=1)
    entry_amount.grid(row=13, column=1)
    entry_meds.grid(row=14, column=1)

    tk.Button(root, text="Generate Bill", command=generate_bill).grid(row=15, column=0, columnspan=2)

  
    tk.Label(root, text="Regex Search (Name/Disease)").grid(row=16, column=0)
    global entry_search
    entry_search = tk.Entry(root)
    entry_search.grid(row=16, column=1)
    tk.Button(root, text="Search", command=search_patient).grid(row=17, column=0, columnspan=2)

    root.mainloop()

# ---------------- Main Program ----------------
init_db()

login_win = tk.Tk()
login_win.title("MediTrack Login")

tk.Label(login_win, text="Username").grid(row=0, column=0)
tk.Label(login_win, text="Password").grid(row=1, column=0)

entry_user = tk.Entry(login_win)
entry_pass = tk.Entry(login_win, show="*")
entry_user.grid(row=0, column=1)
entry_pass.grid(row=1, column=1)

tk.Button(login_win, text="Login", command=login).grid(row=2, column=0, columnspan=2)

login_win.mainloop()