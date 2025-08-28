# Enterprise Network Monitoring MVP Roadmap

This roadmap provides a **12-week (3 months)** structured plan to
design, build, and test the MVP of the **Customizable Open Source
Network Monitoring System with ML-based Device Priority**.

------------------------------------------------------------------------

## ✅ Weekly Task Breakdown

### **Month 1 -- Foundation Setup**

#### Week 1: Environment & Research

-   [ ] Research existing network monitoring tools (Wireshark, Nagios,
    Zabbix, ntopng).
-   [ ] Document pros/cons for each.
-   [ ] Define MVP core features:
    -   Custom protocol handling\
    -   Device priority system (with ML ranking)\
    -   Dashboard for monitoring\
-   [ ] Set up GitHub repo & project structure.

#### Week 2: System Design & Architecture

-   [ ] Define overall architecture (frontend + backend + database).\
-   [ ] Draft system workflow diagrams.\
-   [ ] Specify data points to capture (latency, packet loss, device
    usage).\
-   [ ] Choose ML approach for priority (classification or regression).

#### Week 3: Protocol Handling Module (Baseline)

-   [ ] Research how to implement custom protocol layers.\
-   [ ] Define packet capture mechanism (e.g., raw sockets, libpcap).\
-   [ ] Write protocol specifications (text only, no code).\
-   [ ] Plan testing scenarios for packets from multiple devices.

#### Week 4: Device Data Collection & Storage

-   [ ] Define database schema for storing device/network data.\
-   [ ] Identify parameters to log (device ID, bandwidth, latency,
    uptime).\
-   [ ] Plan historical storage for ML model training.\
-   [ ] Map how raw network data → structured storage.

------------------------------------------------------------------------

### **Month 2 -- Core Features**

#### Week 5: ML-Based Device Priority (Design)

-   [ ] Research ML models for ranking devices (Decision Trees, Random
    Forests).\
-   [ ] Define input features (usage frequency, bandwidth, errors,
    latency).\
-   [ ] Define output label: "priority score".\
-   [ ] Plan evaluation metrics (accuracy, ranking consistency).

#### Week 6: ML Training Dataset Preparation

-   [ ] Prepare synthetic dataset (historical usage patterns).\
-   [ ] Map data preprocessing steps.\
-   [ ] Document scaling/normalization strategies.\
-   [ ] Write guidelines for labeling devices.

#### Week 7: Dashboard Planning

-   [ ] Research UI frameworks (React, Grafana, Streamlit).\
-   [ ] Define dashboard KPIs:
    -   Device list & status\
    -   Priority rank visualization\
    -   Network health metrics\
-   [ ] Draft wireframes (text explanation only).\
-   [ ] Define filtering & search features.

#### Week 8: Integration Plan

-   [ ] Define workflow: Packet Capture → Database → ML Model →
    Dashboard.\
-   [ ] Specify APIs required (device data, priority score retrieval).\
-   [ ] Write integration testing scenarios.\
-   [ ] Create fallback logic if ML model fails.

------------------------------------------------------------------------

### **Month 3 -- Testing & Delivery**

#### Week 9: Testing Protocol Module

-   [ ] Run simulated traffic tests.\
-   [ ] Check packet parsing accuracy.\
-   [ ] Document edge cases (corrupt packets, high load).\
-   [ ] Prepare benchmark comparison.

#### Week 10: ML Model Testing

-   [ ] Validate ML model on synthetic data.\
-   [ ] Compare different models (Decision Tree vs. Random Forest).\
-   [ ] Record accuracy and stability.\
-   [ ] Document retraining strategy.

#### Week 11: Dashboard Mock Testing

-   [ ] Create mock dashboards with sample data.\
-   [ ] Test device filtering and priority ranking.\
-   [ ] Collect feedback from 2--3 users.\
-   [ ] Refine dashboard KPIs.

#### Week 12: Final Review & Delivery

-   [ ] Conduct end-to-end testing (Protocol → Storage → ML →
    Dashboard).\
-   [ ] Document limitations.\
-   [ ] Create future roadmap (alerts, anomaly detection, automation).\
-   [ ] Prepare MVP presentation.

------------------------------------------------------------------------

## 📋 Step-by-Step Guide

1.  **Start small:** Each week builds on the previous.\
2.  **Research first, then design:** Never implement without clarity.\
3.  **Document everything:** MVP should have clear text-based system
    design docs.\
4.  **Focus on ML integration:** Historical data → priority scoring.\
5.  **Dashboard last:** Only after backend + ML pipeline are clear.


