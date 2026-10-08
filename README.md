# 🐾 Smart Collar System - Integrated Backend, AI & Cloud Database

Backend service and AI integration pipeline for the QR Code Based Smart Collar System for Street Dogs.

---

## 🏗️ System Architecture Overview

`
   [ React Citizen / Admin Frontend ]
                  │
                  ▼ (REST APIs)
   [ FastAPI Backend Server ] (Port 8001)
         │                    │
         │                    ▼ (HTTP / Multipart)
         │         [ PyTorch AI Server ] (Port 8000)
         │         • Breed Classifier (EfficientNet-B0)
         │         • Bark Emotion Classifier (Spectrograms)
         │         • IMU Movement Anomaly (1D-CNN)
         ▼
[ Supabase PostgreSQL Cloud Database ]
  • dogs, alerts, incident_reports, vet_records, admin_users, trail_points
`

---

## 👥 Setup Instructions for Team Members

Follow these steps to run the complete backend system locally on your machine connected to the shared live Supabase cloud database:

### 1. Configure Environment Variables (.env)
1. Create a .env file from the template:
   `cmd
   copy .env.example .env
   `
2. Open .env and replace YOUR_PASSWORD_HERE with the shared Supabase project password.
   *(Contact Aarya for the password — do not commit real credentials).*

### 2. Install Required Python Dependencies
`cmd
pip install -r requirements.txt
pip install psycopg2-binary requests
`

### 3. Run the Backend Server
`cmd
python -m uvicorn main:app --port 8001 --reload
`
- Interactive Swagger API Documentation: [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)
- Public OpenAPI spec: [http://127.0.0.1:8001/openapi.json](http://127.0.0.1:8001/openapi.json)

---

## 🤖 AI Models Server Setup (dog-ai-server)

The AI models run as an independent microservice on port 8000.

1. Navigate to the AI server repository:
   `cmd
   cd dog-ai-server
   `
2. Start the AI service:
   `cmd
   python -m uvicorn ai_server:app --port 8000 --reload
   `
- AI Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

*Note: If the AI server is offline, the backend automatically uses intelligent fallback simulation so the application never crashes.*

---

## 🗄️ Shared Supabase PostgreSQL Database

- **Host:** AWS Asia-Pacific Mumbai (ws-0-ap-south-1.pooler.supabase.com)
- **Preloaded Data:** 7 stray dogs (Sheru, Moti, Tyson, Rocky, etc.), real alert telemetry, vet records, and admin credentials.
- All team members connect to this same database instance so test data and incidents sync live across all machines and the frontend.

### Default Admin Credentials (Seeded):
- **Super Admin:** dmin@amc.gov.in / dmin123
- **Veterinary Doctor:** et@amc.gov.in / et123

---

## 🔒 Security Notice
- The .env file containing actual database passwords is strictly ignored by .gitignore.
- Never commit database credentials or private keys to version control.
