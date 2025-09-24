# embeddings_face_recognition.py
import face_recognition
import os
import numpy as np
import pickle

def build_embeddings(dataset_path="face_dataset", output_path="embeddings.pkl"):
    known_encodings = []
    known_names = []

    for person_name in os.listdir(dataset_path):
        person_dir = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_dir):
            continue

        for file in os.listdir(person_dir):
            img_path = os.path.join(person_dir, file)
            image = face_recognition.load_image_file(img_path)

            # Detect face + encode
            encodings = face_recognition.face_encodings(image)
            if len(encodings) > 0:
                known_encodings.append(encodings[0])
                known_names.append(person_name)

    # Save encodings
    data = {"encodings": known_encodings, "names": known_names}
    with open(output_path, "wb") as f:
        pickle.dump(data, f)

    print(f"[INFO] Saved embeddings to {output_path}")


if __name__ == "__main__":
    build_embeddings()
Option B – Use DeepFace (supports multiple models)
python
Copy code
# embeddings_deepface.py
from deepface import DeepFace
import os
import pickle

def build_embeddings(dataset_path="face_dataset", output_path="deepface_embeddings.pkl"):
    embeddings = []
    labels = []

    for person_name in os.listdir(dataset_path):
        person_dir = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_dir):
            continue

        for file in os.listdir(person_dir):
            img_path = os.path.join(person_dir, file)
            try:
                embedding_obj = DeepFace.represent(img_path, model_name="Facenet", enforce_detection=False)
                embeddings.append(embedding_obj[0]["embedding"])
                labels.append(person_name)
            except Exception as e:
                print(f"Error {e} on {img_path}")

    # Save embeddings
    data = {"embeddings": embeddings, "labels": labels}
    with open(output_path, "wb") as f:
        pickle.dump(data, f)

    print(f"[INFO] Saved DeepFace embeddings to {output_path}")


if __name__ == "__main__":
    build_embeddings()