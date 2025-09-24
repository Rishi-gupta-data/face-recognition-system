import os
import numpy as np
import pickle
import face_recognition

class FaceRecognizer:
    def __init__(self, embeddings_path='../../Data/embeddings'):
        self.embeddings_path = embeddings_path
        self.known_faces = self.load_known_faces()

    def load_known_faces(self):
        known_faces = {}
        # Adjust path to be absolute from the project root
        abs_embeddings_path = os.path.abspath(os.path.join(os.path.dirname(__file__), self.embeddings_path))

        if not os.path.exists(abs_embeddings_path):
            os.makedirs(abs_embeddings_path)
            return known_faces

        for filename in os.listdir(abs_embeddings_path):
            if filename.endswith(".pkl"):
                person_name = os.path.splitext(filename)[0]
                file_path = os.path.join(abs_embeddings_path, filename)
                with open(file_path, 'rb') as f:
                    embeddings = pickle.load(f)
                    known_faces[person_name] = embeddings
        print(f"[*] Loaded {len(known_faces)} known individuals.")
        return known_faces

    def add_face(self, person_name, embedding):
        if person_name not in self.known_faces:
            self.known_faces[person_name] = []
        self.known_faces[person_name].append(embedding)
        self._save_embeddings(person_name)
        print(f"[*] Added embedding for {person_name}.")

    def _save_embeddings(self, person_name):
        # Adjust path to be absolute from the project root
        abs_embeddings_path = os.path.abspath(os.path.join(os.path.dirname(__file__), self.embeddings_path))
        file_path = os.path.join(abs_embeddings_path, f"{person_name}.pkl")
        with open(file_path, 'wb') as f:
            pickle.dump(self.known_faces[person_name], f)

    def recognize_face(self, face_embedding, threshold=0.6):
        if not self.known_faces:
            return "Unknown"

        # Create arrays of known face encodings and their names
        known_face_encodings = []
        known_face_names = []
        for name, embeddings_list in self.known_faces.items():
            for embedding in embeddings_list:
                known_face_encodings.append(embedding)
                known_face_names.append(name)

        if not known_face_encodings:
            return "Unknown"

        # See how far apart the test embedding is from the known embeddings
        face_distances = face_recognition.face_distance(known_face_encodings, face_embedding)
        
        best_match_index = np.argmin(face_distances)
        min_distance = face_distances[best_match_index]

        if min_distance < threshold:
            return known_face_names[best_match_index]
        else:
            return "Unknown"

if __name__ == "__main__":
    # Example usage:
    recognizer = FaceRecognizer()
    print(f"Known faces: {recognizer.known_faces.keys()}")

    # Simulate adding a new face
    # face_recognition model produces 128-d embeddings
    # dummy_embedding = np.random.rand(128).tolist()
    # recognizer.add_face("TestPerson", dummy_embedding)
    # print(f"Known faces after adding: {recognizer.known_faces.keys()}")

    # Simulate recognizing a face
    # if recognizer.known_faces.get("TestPerson"):
    #     test_embedding = recognizer.known_faces["TestPerson"][0]
    #     recognized = recognizer.recognize_face(test_embedding)
    #     print(f"Recognized: {recognized}")