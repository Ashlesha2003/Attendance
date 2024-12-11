import csv
import os

ATTENDANCE_FILE = "attendance.csv"

def view_attendance():
    print("\nViewing attendance...")
    
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found.")
        return

    with open(ATTENDANCE_FILE, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name: {row[0]}, Roll: {row[1]}, Date: {row[2]}, Time: {row[3]}")
            