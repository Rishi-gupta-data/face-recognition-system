# 📌 Task – Frontend Development (Streamlit)
**Assigned To:** [Developer Name]

**Timeline:** 5 Days

---

## **Objective**
Build the Streamlit user interface for the security system, allowing for live monitoring, person management, and viewing event logs/alerts.

---

## **Tasks & Deliverables**

### **Day 1 – Project Setup & Live Feed**
- Set up the basic Streamlit project structure (`app.py`).
- Create the main dashboard layout.
- Integrate the live webcam feed and display the real-time recognition output (bounding boxes, names, mesh).

### **Day 2 – Person Management**
- Design a UI form to register a new person (name, ID, etc.).
- Implement functionality to let an admin upload a photo or use the webcam to capture an image for the new person.
- Connect the form to the backend to store the new person's data in the database.

### **Day 3 – Logs & Alerts View**
- Create a separate page or section to display event logs from the database.
- Implement a table view for the logs with search and filter capabilities (e.g., by person, date, camera).
- Highlight alerts for "Unknown" persons, for example, by using color-coding.

### **Day 4 – Backend Integration**
- Ensure all UI components are correctly calling the FastAPI backend endpoints (e.g., `/verify`, `/logs`, `/capture`).
- Handle and display responses and errors from the backend in a user-friendly way.

### **Day 5 – Styling & Final Touches**
- Polish the layout and styling of the dashboard for better usability and a clean look.
- Add clear instructions, labels, and titles for all UI components.
- Perform final end-to-end testing from the user interface.

---

## **Output**
- A fully functional Streamlit application (`app.py`).
- A user-friendly dashboard for interacting with the security system.
