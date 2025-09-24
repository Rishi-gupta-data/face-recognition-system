# 📅 Weekly Task Plan – Face Recognition Security System  


---

##  Task 1 – Week 1  
### **Face Capture**  
Goal: Build the foundation for face input into the system.  

- [X] Webcam Integration (`OpenCV`)  
- [X] Mesh for Face (landmarks with `dlib` / `face_recognition`)  
- [X] Face Data Input (20–30 images per person)  
- [X] Convert Face Data into Mesh/Embeddings (`face_recognition` / DeepFace)  

**Output:** `face_capture.py` – captures faces & extracts embeddings.  

---

##  Task 2 – Week 2  
### **Database & Data Storage Setup (Supabase)**  

- [ ] Create tables: Persons, Logs, Cameras  
- [ ] Connect Supabase with Python (`supabase-py`)  
- [ ] Implement `add_person()`, `get_person_by_id()`, `log_event()`  
- [ ] Test DB inserts & fetches  

**Output:** DB schema + Python DB functions.  

---

##  Task 3 – Week 3  
### **Face Recognition & Matching**  

- [X] Extract embeddings from webcam frames  
- [X] Compare embeddings with DB-stored vectors  
- [X] Implement threshold-based match (<0.6 distance = Match)  
- [X] Output **Known Person / Unknown Person**  

**Output:** `recognizer.py` – recognition working with >85% accuracy.  

---

##  Task 4 – Week 4  
### **Alerts & Logging**  

- [ ] Log "Known" persons  
- [ ] Log "Unknown" persons  
- [ ] Trigger alerts (sound/Streamlit notification)  
- [ ] Optional: Motion detection with OpenCV  

**Output:** Alerts + logs stored in DB with timestamp.  

---

##  Task 5 – Week 5  
### **Backend (FastAPI)**  

- [ ] Setup FastAPI project structure  
- [ ] Create `POST /capture` (store embeddings)  
- [ ] Create `POST /verify` (match face with DB)  
- [ ] Create `GET /logs` (fetch logs)  
- [ ] Create `GET /alerts` (real-time alerts)  

**Output:** RESTful API server (`main.py`).  

---

##  Task 6 – Week 6  
### **UI Development (Streamlit)**  

- [ ] Build Dashboard Home (live webcam feed + recognition status)  
- [ ] Person Management (upload photo & register new person)  
- [ ] Logs/Alerts View (table + search filters)  
- [ ] Display alerts in red if unknown detected  

**Output:** Streamlit app (`app.py`).  

---

##  Task 7 – Week 7  
### **Integration & Testing**  

- [ ] Connect Streamlit ↔ FastAPI ↔ Supabase ↔ AI models  
- [ ] Run end-to-end test (capture → match → alert → log)  
- [ ] Containerize project with `Dockerfile`  
- [ ] Test recognition speed + accuracy  

**Output:** Full working system in Docker.  

---

##  Task 8 – Week 8  
### **Final Deployment & Documentation**  

- [ ] Deploy via Streamlit Cloud or Docker Hub  
- [ ] Write `README.md` (setup + usage)  
- [ ] Write `WEEKLY_TASKS.md` (progress log)  
- [ ] Write `API_DOCS.md` (API usage examples)  
- [ ] Final Demo & Bug Fixing  

**Output:** Running system + documentation.  

---
