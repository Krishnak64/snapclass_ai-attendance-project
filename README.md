# 🚀 SnapClass AI — Smart Attendance System

SnapClass AI is an intelligent AI-powered attendance management system that automates classroom attendance using **Face Recognition**, **Voice AI**, and **QR Technology**.

The project is designed to reduce manual effort, eliminate proxy attendance, and provide a faster and smarter attendance experience for educational institutions.

---

## 🌐 Live Demo

🔗 Live Project:
https://snapclass-ai-attendance-landing-pag.vercel.app/

---

## ✨ Features

* 🎭 Face Recognition Attendance
* 🎙️ Voice-Based Attendance Detection
* 📱 QR Code Attendance System
* 📊 Real-Time Attendance Tracking
* 🧠 AI-Powered Student Identification
* ☁️ Cloud Database Integration
* 📥 Attendance Record Management
* ⚡ Fast and Automated Workflow

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML/CSS
* JavaScript

### Backend

* Python
* Flask

### AI / ML

* OpenCV
* Face Recognition
* Speech Recognition
* Machine Learning Models

### Database & Cloud

* Supabase
* Firebase

### Deployment

*deploy landing page on Vercel and main project on streamlit

---

## 📂 Project Structure

```bash id="wo6klt"
snapclass/
│
├── .streamlit/
│   └── secrets.toml
│
├── src/
│   │
│   ├── components/
│   │   ├── dialog_add_photo.py
│   │   ├── dialog_attendance_results.py
│   │   ├── dialog_auto_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── dialog_enroll.py
│   │   ├── dialog_share_subject.py
│   │   ├── dialog_voice_attendance.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   └── subject_card.py
│   │
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── pipelines/
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   │
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   └── ui/
│       └── base_layout.py
│
├── venv/
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```


---

🏗️ System Architecture Flow: 

                    ┌─────────────────────┐
                    │   Streamlit UI      │
                    │ (Admin Dashboard)    │
                    └─────────┬───────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼

┌──────────────┐   ┌──────────────────┐   ┌──────────────────┐
│ Face Module   │   │ Voice Module     │   │ QR Module        │
│ dlib + ML     │   │ librosa + AI     │   │ segno generator  │
│ face vectors  │   │ speaker ID       │   │                  │
└──────┬───────┘   └────────┬─────────┘   └────────┬─────────┘
       │                    │                      │
       └────────────┬───────┴──────────────┬──────┘
                    ▼                      ▼
        ┌────────────────────────────────────────┐
        │     AI Matching Engine (scikit-learn)  │
        │   Face + Voice + QR Identity Fusion    │
        └──────────────────┬─────────────────────┘
                           ▼
        ┌────────────────────────────────────────┐
        │        Backend (Supabase Cloud)        │
        │       Users | Attendance | Logs        │
        └────────────────────────────────────────┘

                           ▼
        ┌────────────────────────────────────────┐
        │   Security Layer (bcrypt authentication)│
        └────────────────────────────────────────┘

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Krishnak64/snapclass_ai-attendance-project.git
```

### 2️⃣ Move into Project Folder

```bash
cd snapclass_ai-attendance-project
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run Project

```bash
streamlit run app.py
```

---

## 📸 Screenshots

<img width="1919" height="884" alt="Screenshot 2026-05-27 011508" src="https://github.com/user-attachments/assets/ec27ec43-e536-4909-94de-e0ebc64a06e6" />


<img width="1917" height="884" alt="Screenshot 2026-05-27 004956" src="https://github.com/user-attachments/assets/f2c3e6af-eb57-4cb0-8cf9-f912b7a78156" />

<img width="1919" height="880" alt="Screenshot 2026-05-27 005428" src="https://github.com/user-attachments/assets/ebc3be21-2a73-419e-bcd2-4f55b491dc40" />

<img width="1919" height="880" alt="Screenshot 2026-05-27 004747" src="https://github.com/user-attachments/assets/f5fab2cf-90d0-45e9-a233-e7dd47aca702" />

<img width="1919" height="881" alt="Screenshot 2026-05-27 004337" src="https://github.com/user-attachments/assets/096db69f-75a9-4868-bdd6-bb2a8a71eebf" />

<img width="1919" height="881" alt="Screenshot 2026-05-27 003938" src="https://github.com/user-attachments/assets/58c2ce6c-7c2e-4552-b991-9216c48e7b01" />

<img width="1919" height="880" alt="Screenshot 2026-05-27 003829" src="https://github.com/user-attachments/assets/fe6fd3e1-be39-443a-a78e-195bfbd00c6f" />

<img width="1916" height="873" alt="Screenshot 2026-05-27 003604" src="https://github.com/user-attachments/assets/13672bec-09ff-4442-a39d-abf06769b3b4" />

<img width="1919" height="878" alt="Screenshot 2026-05-27 003452" src="https://github.com/user-attachments/assets/b13222a4-25b8-41ed-ac66-38895f913528" />






Example:

* Dashboard
* Face Recognition Module
* Voice Attendance Module
* QR Attendance Screen

---

## 🎯 Future Improvements

* Mobile App Integration
* Advanced Analytics Dashboard
* Multi-Classroom Support
* AI Attendance Reports
* Anti-Spoofing Face Detection

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository and submit pull requests.

---

## 📧 Contact

👤 Krishna Kumar

* GitHub: https://github.com/Krishnak64
* LinkedIn: https://www.linkedin.com/

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
