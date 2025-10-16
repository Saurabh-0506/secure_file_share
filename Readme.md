📁 Secure File Sharing System (FastAPI) A secure backend system that allows:

📤 Ops Users to upload files (.pptx, .docx, .xlsx)

📥 Client Users to register, verify email, login, list, and securely download files

🚀 Tech Stack Backend Framework: FastAPI (Python)

Auth: JWT + Role-Based Access Control

Database: In-memory (can switch to PostgreSQL)

Email: Token-based verification (SMTP optional)

File Handling: Uploads + secure encrypted download links

📦 Features 🔐 Authentication JWT token-based login

Separate roles for ops and client

🧑‍💼 Ops Users Login

Upload .pptx, .docx, .xlsx files

🧑‍💻 Client Users Signup (returns email verification URL)

Email Verification

Login (JWT)

List uploaded files

Generate secure download links

Download files via secure token

📂 Project Structure bash Copy Edit secure_file_share/ │ ├── app/ │ ├── routes/ │ │ ├── ops_routes.py │ │ └── client_routes.py │ ├── auth/ │ │ └── auth_handler.py │ ├── utils/ │ ├── email/ │ └── database.py │ ├── uploaded_files/ # Files uploaded by ops ├── main.py # Entry point ├── .env # Environment variables ├── .gitignore ├── requirements.txt # Dependencies ├── Dockerfile # (Optional) Docker support └── README.md 💻 How to Clone and Run 📥 Step 1: Clone the Repository bash Copy Edit git clone https://github.com/Saurabh-0506/secure-file-share.git cd secure-file-share 🧪 Step 2: Create Virtual Environment (Optional but Recommended) bash Copy Edit python -m venv venv source venv/bin/activate # On Windows use: venv\Scripts\activate 📦 Step 3: Install Dependencies bash Copy Edit pip install -r requirements.txt 🔐 Step 4: Configure Environment Variables Create a .env file and add:

env Copy Edit SECRET_KEY=your_jwt_secret_key ALGORITHM=HS256 ACCESS_TOKEN_EXPIRE_MINUTES=30 For email verification (optional):

env Copy Edit SMTP_SERVER=smtp.example.com SMTP_PORT=587 SMTP_USERNAME=your_email@example.com SMTP_PASSWORD=your_password ▶️ Step 5: Run the FastAPI Server bash Copy Edit uvicorn main:app --reload 📂 Step 6: Access the API Docs Open your browser and go to:

arduino Copy Edit http://127.0.0.1:8000/docs 🐳 Docker (Optional) bash Copy Edit docker build -t secure-file-share . docker run -d -p 8000:8000 secure-file-share 📬 Email Verification (Optional) If SMTP is configured in .env, the app will send a verification email upon signup.

Otherwise, it will return the token-based URL directly in the response for testing.

🙋 Author Saurabh Gond 📧 Email: gondsaurabh722@gmail.com 🔗 GitHub: Saurabh-0506