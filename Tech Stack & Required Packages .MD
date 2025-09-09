# 📌 Tech Stack & Required Packages  

## 🎨 UI Layer  
- **Framework:** [Streamlit](https://streamlit.io/)  
  - Package: `streamlit`  
  - Purpose: Build interactive dashboards & live monitoring UI (for CCTV feed, alerts, logs).  

---

## ⚙️ Backend (API + Business Logic)  
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)  
  - Package: `fastapi`  
  - Server: `uvicorn` (for running FastAPI server)  
  - Purpose: Expose REST APIs for face recognition, database access, and alerts.  

---

## 🤖 AI/ML Components  
- **Face Detection & Recognition:**  
  - `face_recognition` → Easy face detection/recognition library.  
  - `DeepFace` → Advanced recognition + emotion, age, gender detection.  
  - `opencv-python` → (OpenCV) for video frame processing, image preprocessing, object tracking.  

- **Neural Networks / Deep Learning (if needed for custom models):**  
  - `tensorflow` or `torch` → For training custom models (optional).  
  - `scikit-learn` → For ML algorithms (SVM, clustering, anomaly detection).  
  - `numpy`, `pandas` → Data preprocessing and analysis.  

---

## 🗄️ Database Layer  
- **Database:** [Supabase](https://supabase.com/) (PostgreSQL-based)  
  - Python Client: `supabase-py`  
  - Purpose: Store persons info, logs, alerts, and camera metadata.  

---

## 📦 Deployment & Containerization  
- **Docker**  
  - Tools: `docker`, `docker-compose`  
  - Purpose: Containerize app for portability.  

- **Cloud Deployment:**  
  - [Streamlit Cloud](https://streamlit.io/cloud) → Deploy UI directly.

---

## 🛠️ Supporting Tools & Libraries  
- **Logging & Monitoring:**  
  - `loguru` or built-in `logging` (to track activities).  

- **API Testing:**  
  - [Postman](https://www.postman.com/) or `httpx` (Python) for API calls.  

- **Notifications:**  
  - `smtplib` (emails) or `twilio` (SMS/WhatsApp alerts).  

- **Other Utilities:**  
  - `python-dotenv` → Manage environment variables (DB keys, API keys).  
  - `requests` → API requests handling.  

---

✅ This list ensures **end-to-end functionality**:  
- Capture video → detect faces → recognize → log in DB → show in Streamlit → send alerts → deploy with Docker.  
