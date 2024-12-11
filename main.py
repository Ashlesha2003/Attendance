from add_student import add_student_data
from train_model import train_face_recognizer
from take_attendance import take_attendance
from view_attendance import view_attendance

def main():
    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. View Attendance")
        print("3. Take Attendance")
        print("4. Train Model Manually")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student_data()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            take_attendance()
        elif choice == '4':
            recognizer, names = train_face_recognizer()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
