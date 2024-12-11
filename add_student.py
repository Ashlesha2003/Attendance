import cv2
import os
import csv

DATA_DIR = "student_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

STUDENT_DATA_FILE = "students.csv"

def add_student_data():
    print("\nAdding new student data...")
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    name = input("Enter name of the student: ")
    roll_number = input("Enter roll number of the student: ")
    
    new_student_data = [name, roll_number, ""]

    print("Capturing images... Please look at the camera.")
    
    images = []
    for i in range(30):
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face_region = gray[y:y+h, x:x+w]
            images.append(face_region)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Capturing Image", frame)
        
        if len(images) >= 30:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    student_image_path = os.path.join(DATA_DIR, f"{name}_{roll_number}.jpg")
    cv2.imwrite(student_image_path, images[0])
    
    new_student_data[2] = student_image_path
    with open(STUDENT_DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_student_data)
    
    print(f"Student data saved for {name}.")