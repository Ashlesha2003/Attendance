import cv2
import os
import csv
import numpy as np
import pickle

STUDENT_DATA_FILE = "students.csv"

def train_face_recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []
    names = {}
    label_counter = 0

    with open(STUDENT_DATA_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            name = row[0]
            image_path = row[2]
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                continue

            faces.append(image)
            labels.append(label_counter)
            names[label_counter] = name
            label_counter += 1
    
    if len(faces) > 0:
        recognizer.train(faces, np.array(labels))
        recognizer.save('trainer.yml')

        with open('names.pkl', 'wb') as f:
            pickle.dump(names, f)

        print("Model trained and saved as trainer.yml")
    else:
        print("No student images found to train the model.")
    
    return recognizer, names