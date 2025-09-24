# 📌 Task – Database Development
**Assigned To:** [Aayush]

**Timeline:** 4 Days  

---

## **Objective**
Set up and manage the backend database for the Face Recognition Security System using **Supabase (PostgreSQL)**.  

---

## **Tasks & Deliverables**

### **Day 1 – DB Setup & Connection**
- Create Supabase project & PostgreSQL database.
- Create tables: `Persons`, `Logs`, `Cameras`.
- Connect Supabase with Python using `supabase-py`.
- Test DB connection and CRUD operations.

### **Day 2 – Persons Table**
- Implement functions:
  - `add_person(name, id_no, course, photo)`  
  - `update_person(person_id, details)`  
  - `delete_person(person_id)`  
  - `get_person_by_id(person_id)`  
- Test insertion & retrieval of sample data.

### **Day 3 – Logs & Cameras Tables**
- Implement logging functions:
  - `log_event(person_id, camera_id, status)`  
  - `fetch_logs(filters)` (time, person, camera)
- Create camera table & manage metadata:
  - `add_camera(location)`, `get_camera(camera_id)`

### **Day 4 – Testing & Documentation**
- Run end-to-end tests: insert person → log → fetch logs.
- Document **DB schema**, functions, and sample queries in `DB_DOCS.md`.

---

## **Output**
- Fully functional database in Supabase.  
- Python scripts for database operations.  
- Documentation for future integration with backend & AI modules.
