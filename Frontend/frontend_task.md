# 📌 Task – Frontend Development
**Assigned To:** [Aashish]

**Timeline:** 10 Days  

---

## **Objective**
Build the **Streamlit dashboard** for the Face Recognition Security System. The UI will handle live feed, alerts, logs, and person management.

---

## **Tasks & Deliverables**

### **Days 1–2 – Dashboard Home**
- Integrate **live webcam feed**.
- Show **recognition status** (Known / Unknown) in real-time.
- Display **alerts** prominently (red for unknown persons).

### **Days 3–4 – Person Management**
- Upload new person’s photo & details (name, ID, course).
- Connect UI → FastAPI → Supabase to save person data.
- Edit or delete registered persons.

### **Days 5–6 – Logs & Alerts**
- Display logs in a **table** with filters:
  - Time range
  - Person
  - Camera location
- Highlight unknown or suspicious events.

### **Days 7–8 – Integration with Backend**
- Connect **Streamlit** with **FastAPI endpoints**:
  - `POST /capture`
  - `POST /verify`
  - `GET /logs`
  - `GET /alerts`
- Ensure **real-time updates** of recognition and alerts.

### **Days 9–10 – UI Polishing & Testing**
- Improve dashboard usability (layout, colors, indicators).
- Test **end-to-end workflow** with live feed + recognition + logs.
- Write **`FRONTEND_DOCS.md`** for setup & usage instructions.

---

## **Output**
- Fully functional **Streamlit dashboard** with:
  - Live feed
  - Alerts
  - Logs & search filters
  - Person management
- Documentation for deployment & integration.
