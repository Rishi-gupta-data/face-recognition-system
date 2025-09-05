# 📄 Software Requirement Specification (SRS)
## Project: CCTV-based Face Recognition Security Guard System
### Version: 1.0  
### Author: Rishi Gupta  
### Date: 2025-09-05  

---

## 1. Introduction  

### 1.1 Purpose  
The purpose of this project is to build an **AI-powered security guard system** using CCTV (or webcam for prototype). The system will:  
- Recognize faces in **live video streams** or **recorded CCTV footage**.  
- Maintain a **database of registered individuals** (Name, ID, Course, etc.).  
- Detect suspicious activities (e.g., glass breaking, vandalism, unauthorized entry).  
- Allow **manual photo input** to search for an individual in past recordings.  

### 1.2 Scope  
This project will help educational institutions, offices, and residential areas improve security by automatically identifying people and logging activities.  
- **Users**: Security guards, administrators.  
- **System Functions**:  
  - Live face recognition.  
  - Offline search from CCTV recordings.  
  - Database management of individuals.  
  - Suspicious activity detection & alert system.  

---

## 2. STAR Analysis  

### Situation  
Security guards manually monitor CCTV feeds, making it inefficient to identify suspects or unusual behavior.  

### Task  
Automate face recognition, suspicious activity detection, and searching through recorded video.  

### Action  
- Implement OpenCV + Deep Learning for face recognition.  
- Store metadata (FaceID, Name, Course, Time, Location).  
- Integrate with a simple dashboard for search and alerts.  

### Result  
- Reduced workload for guards.  
- Faster identification of suspects.  
- Enhanced security and better logging of activities.  

---

## 3. Functional Requirements  

1. **Face Recognition**  
   - Detect faces in live video feed.  
   - Match faces against the database.  
   - Store logs with timestamp and location.  

2. **Recorded Video Search**  
   - Input photo and search across stored recordings.  
   - Extract frames and identify matching individuals.  

3. **Database Management**  
   - Add, update, and delete individuals (Name, ID, Course, etc.).  
   - Store attendance/activity logs.  

4. **Activity Detection**  
   - Identify suspicious activities like vandalism or unauthorized access.  
   - Trigger alert (sound/email notification).  

---

## 4. Non-Functional Requirements  

- **Performance**: Must process live video with ≤ 1-second delay.  
- **Accuracy**: Face recognition accuracy ≥ 90%.  
- **Scalability**: Support multiple CCTV feeds.  
- **Security**: Data encryption and role-based access control.  
- **Usability**: Simple dashboard for non-technical users.  

---

## 5. System Flow  

### 5.1 High-Level Flowchart  

```mermaid
flowchart TD
    A[Start CCTV Feed] --> B{Face Detected?}
    B -->|Yes| C[Extract Face Features]
    B -->|No| A
    C --> D{Match Found in DB?}
    D -->|Yes| E[Log Entry with Name & ID]
    D -->|No| F[Unknown Person Alert]
    E --> G[Check for Suspicious Activity]
    F --> G
    G -->|Yes| H[Trigger Alarm & Notify Security]
    G -->|No| A


---

6. Use Case Diagram

usecaseDiagram
actor Admin
actor Security

Admin --> (Add/Update Person in DB)
Security --> (Monitor Live CCTV)
Security --> (Search Recorded Video)
Security --> (Get Alerts)

system "Face Recognition Security" {
  (Face Recognition)
  (Database Management)
  (Suspicious Activity Detection)
  (Recorded Video Search)
}


---

7. Database Schema

Tables

Persons

PersonID (PK)

Name

Course

ID_No

Photo


Logs

LogID (PK)

PersonID (FK)

Timestamp

CameraID

Status (Known/Unknown)


Cameras

CameraID (PK)

Location




---

8. System Architecture

flowchart LR
    User --> Dashboard
    Dashboard --> Backend[Flask/Django Backend]
    Backend --> DB[(PostgreSQL/MySQL)]
    Backend --> AI[Face Recognition Engine]
    AI --> CCTV[CCTV/Recorded Video]


---

9. Constraints

Requires GPU for real-time processing.

CCTV footage storage must be sufficient.

Internet required for cloud backup/remote alerts.



---

10. Future Enhancements

Integration with biometric systems.

Multi-camera synchronization.

Mobile app for alerts.

Crime prediction analytics.



---

11. Glossary

CCTV: Closed-circuit television.

FaceID: Unique representation of a face.

Suspicious Activity: Any unusual behavior like breaking objects, forced entry, etc.



---

12. Conclusion

This project leverages AI + CCTV to automate the role of a security guard. It ensures efficient monitoring, real-time alerts, and quick identification of individuals, improving overall security.





create .md code and madd more explanation and detailing in it

Perfect Rishi 🚀—you’ve already built a fantastic **SRS draft**.  
What I’ll do now is:  

1. Convert it into a **properly formatted `.md` (Markdown) document**.  
2. Add **more explanation, detailing, and technical clarity** so that it can directly act as project documentation (useful for research papers, GitHub repos, or reports).  

Here’s the detailed **SRS in Markdown code**:

***

```markdown
# 📄 Software Requirement Specification (SRS)
## Project: CCTV-based Face Recognition Security Guard System
### Version: 1.0  
### Author: Rishi Gupta  
### Date: 2025-09-05  

---

## 1. Introduction  

### 1.1 Purpose  
The purpose of this project is to build an **AI-powered security guard system** using CCTV (or webcam for prototype). The system will:  
- Recognize faces in **live video streams** or **recorded CCTV footage**.  
- Maintain a **database of registered individuals** (Name, ID, Course, etc.).  
- Detect suspicious activities (e.g., glass breaking, vandalism, unauthorized entry).  
- Allow **manual photo input** to search for an individual in past recordings.  

This project aims to **reduce manual workload** of security guards and ensure **faster, more accurate monitoring**.  

---

### 1.2 Scope  
This system is designed for **educational institutes, offices, and residential communities** where security is crucial.  

**Users:**  
- Security Guards (operational monitoring).  
- Administrators (database & system management).  

**System Features:**  
- Face recognition with logging.  
- Search capability across past CCTV feeds.  
- Dynamic database of individuals.  
- Suspicious activity detection with alerts.  

---

## 2. STAR Analysis  

### Situation  
Security guards manually monitor CCTV feeds for suspicious activities and identification, which is inefficient and error-prone.  

### Task  
Build a system that automates **face detection, identification, suspicious activity detection, and recorded video search**.  

### Action  
- Use **OpenCV + Deep Learning (CNN / FaceNet / Dlib)** for face recognition.  
- Store metadata such as **FaceID, Name, ID, Time, Camera Location**.  
- Develop an **interactive dashboard** for monitoring and searching.  
- Implement alerting mechanism (sound alarms, email/SMS notifications).  

### Result  
- **Reduced human dependency** on 24/7 monitoring.  
- **Instant alerts** for unauthorized access.  
- **Faster investigation** of past events.  
- **Improved security** with automated logging and AI-powered analysis.  

---

## 3. Functional Requirements  

1. **Face Recognition**  
   - Detect faces in live CCTV feed.  
   - Match faces with database (Known/Unknown).  
   - Store logs with timestamp, camera location, and identification status.  

2. **Recorded Video Search**  
   - Allow input of a photo to search across stored recordings.  
   - Extract frames & detect matching persons.  
   - Generate report of occurrences with time & camera ID.  

3. **Database Management**  
   - Admin can **Add/Update/Delete persons** with details (Name, ID, Course, Photo).  
   - Maintain data integrity.  
   - Manage attendance/activity logs for analysis.  

4. **Suspicious Activity Detection**  
   - AI model trained for detecting actions like:  
     - Breaking glass, vandalism.  
     - Unauthorized entry at night.  
     - Loitering in restricted areas.  
   - Alerts security via **alarm sound + email/SMS notification**.  

---

## 4. Non-Functional Requirements  

- **Performance**: Live video feed must be processed with ≤ 1-second delay.  
- **Accuracy**: Face recognition accuracy ≥ 90%, activity detection ≥ 85%.  
- **Scalability**: Must handle multiple CCTV streams simultaneously.  
- **Reliability**: System uptime ≥ 99%.  
- **Security**: Encrypted databases, role-based authentication.  
- **Usability**: User-friendly dashboard with minimal training required.  

---

## 5. System Flow  

### 5.1 High-Level Flowchart  

```
flowchart TD
    A[Start CCTV Feed] --> B{Face Detected?}
    B -->|Yes| C[Extract Face Features]
    B -->|No| A
    C --> D{Match Found in DB?}
    D -->|Yes| E[Log Entry with Name & ID]
    D -->|No| F[Unknown Person Alert]
    E --> G[Check for Suspicious Activity]
    F --> G
    G -->|Yes| H[Trigger Alarm & Notify Security]
    G -->|No| A
```

---

## 6. Use Case Diagram  

```
usecaseDiagram
actor Admin
actor Security

Admin --> (Add/Update Person in DB)
Security --> (Monitor Live CCTV)
Security --> (Search Recorded Video)
Security --> (Receive Alerts)

system "Face Recognition Security" {
  (Face Recognition)
  (Database Management)
  (Suspicious Activity Detection)
  (Recorded Video Search)
}
```

---

## 7. Database Schema  

### **Persons Table**  
- PersonID (PK)  
- Name  
- Course  
- ID_No  
- Photo  

### **Logs Table**  
- LogID (PK)  
- PersonID (FK)  
- Timestamp  
- CameraID  
- Status (Known/Unknown)  

### **Cameras Table**  
- CameraID (PK)  
- Location  

---

## 8. System Architecture  

```
flowchart LR
    User --> Dashboard
    Dashboard --> Backend[Flask/Django Backend]
    Backend --> DB[(PostgreSQL/MySQL)]
    Backend --> AI[Face Recognition Engine]
    AI --> CCTV[CCTV/Recorded Video]
    Backend --> Alerts[Notification Service]
```

---

## 9. Constraints  

- Requires **GPU acceleration** for real-time face recognition.  
- CCTV footage storage must be large enough to keep 30+ days of video.  
- Internet connectivity needed for **cloud backups & remote alerts**.  

---

## 10. Future Enhancements  

- Integration with **biometric fingerprint/RFID systems**.  
- **Mobile app** for instant security alerts.  
- **Multi-camera person tracking** across locations.  
- Predictive analytics for **crime hotspot detection**.  
- Integration with government ID databases.  

---

## 11. Glossary  

- **CCTV**: Closed-circuit television; surveillance system with cameras.  
- **FaceID**: Unique vector representation of a facial image.  
- **Suspicious Activity**: Unusual behavior (breaking glass, forced entry, etc.).  
- **Dashboard**: Web interface for monitoring feed and managing data.  

---

## 12. Conclusion  

This system leverages **AI + CCTV** to act as a **digital security guard**.  
It reduces manual monitoring, increases **response speed**, and improves **overall security infrastructure**.  

By automating face recognition, activity detection, and alerts, it ensures **proactive security management** in educational institutions, corporate offices, and residential societies.  

```

***

