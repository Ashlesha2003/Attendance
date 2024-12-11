import cv2
import csv
import pickle
from datetime import datetime

ATTENDANCE_FILE = "attendance.csv"

def take_attendance():
    print("\nTaking attendance...")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')

    with open('names.pkl', 'rb') as f:
        names = pickle.load(f)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    print("Looking for faces...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces[:1]:
            face_region = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face_region)

            if confidence < 100:
                student_name = names[label]
                print(f"Recognized: {student_name}")

                with open(ATTENDANCE_FILE, mode="a", newline="") as file:
                    writer = csv.writer(file)
                    now = datetime.now()
                    date, time = now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")
                    writer.writerow([student_name, "N/A", date, time])
                print(f"Attendance marked for {student_name}")
                
                input("Press Enter to mark attendance for the next student...")

                return
            else:
                print("Face not recognized or not registered in the system.")
        
        cv2.imshow("Attendance Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()