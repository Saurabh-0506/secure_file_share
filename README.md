# Secure File Sharing System

This is a backend project built using FastAPI for secure file sharing between Ops and Client users.

## Features

- JWT Auth
- File Upload (Ops only)
- Encrypted Download (Client only)
- Email Verification

  secure_file_System/README.md

  # 📁 Secure File Sharing System (FastAPI)

A secure backend system that allows:

- 📤 Ops Users to upload files (`.pptx`, `.docx`, `.xlsx`)
- 📥 Client Users to register, verify email, login, list, and securely download files

---

## 🚀 Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Auth:** JWT + Role-Based Access Control
- **Database:** In-memory (can switch to PostgreSQL)
- **Email:** Token-based verification (SMTP optional)
- **File Handling:** Uploads + secure encrypted download links

---

## 📦 Features

### 🔐 Authentication

- JWT token-based login
- Separate roles for `ops` and `client`

### 🧑‍💼 Ops Users

- Login
- Upload `.pptx`, `.docx`, `.xlsx` files

### 🧑‍💻 Client Users

- Signup (returns email verification URL)
- Email Verification
- Login (JWT)
- List uploaded files
- Generate secure download links
- Download files via secure token

---

## 📂 Project Structure

secure_file_share/
│
├── app/
│ ├── routes/
│ │ ├── ops_routes.py
│ │ └── client_routes.py
│ ├── auth/
│ │ └── auth_handler.py
│ ├── utils/
│ ├── email/
│ └── database.py
│
├── uploaded_files/ # Files uploaded by ops
├── main.py
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
