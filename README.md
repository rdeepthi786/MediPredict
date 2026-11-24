# MediPredict — Multi-Disease Prediction System with Confidence Score & AI Health Assistant

MediPredict is a production-grade clinical decision-support web application. It integrates machine-learning models for multiple chronic and acute conditions (Diabetes, Cardiovascular Disease, Chronic Kidney Disease, and General Symptom Multi-Disease Classifier) with model confidence scores, SHAP (SHapley Additive exPlanations) feature attribution, an AI Health Assistant powered by Gemini 3.8 Flash, browser voice symptom input, text-to-speech audio guidance, and downloadable PDF clinical reports.

---

## 🏛️ System Architecture

```text
                       ┌──────────────────────────────────────────────────────────┐
                       │           React SPA Frontend (Vite + Tailwind)           │
                       │  - Dynamic Clinical Forms with Normal Range Validation   │
                       │  - Web Speech Recognition (Voice Input)                  │
                       │  - SpeechSynthesis (Text-to-Speech Guidance)             │
                       │  - SHAP Horizontal Attribution Bar Visualizer            │
                       │  - Light & Dark Healthcare Theme Modes                   │
                       └────────────────────────────┬─────────────────────────────┘
                                                    │ REST API (Bearer JWT)
                                                    ▼
                       ┌──────────────────────────────────────────────────────────┐
                       │        Application Backend (Node.js Express / TS)        │
                       │  - SQLite Database Persistence (Users, Predictions, Chat)│
                       │  - Password Hashing (bcrypt) & JWT Session Security      │
                       │  - Medical Knowledge Registry (Diseases, Precautions)    │
                       │  - Gemini 3.8 Flash AI Assistant with Medical Guardrails │
                       │  - PDF Report Generation Engine                          │
                       └────────────────────────────┬─────────────────────────────┘
                                                    │
                                                    ▼
                       ┌──────────────────────────────────────────────────────────┐
                       │             Verified ML Models & Adapters                │
                       │  1. Diabetes: Pima Indian Logistic / XGBoost Classifier  │
                       │  2. Heart Disease: Cleveland UCI 13-Feature Ensemble     │
                       │  3. Chronic Kidney Disease: UCI 12-Feature Renal Model   │
                       │  4. Symptom Matrix: Bayesian Multi-Label Classifier      │
                       │  5. SHAP Marginal Log-Odds Attribution Engine            │
                       └──────────────────────────────────────────────────────────┘
```

---

## 📋 Features

1. **Multi-Disease Prediction**:
   - **Diabetes Mellitus**: Evaluates Glucose, BMI, Age, Insulin, Blood Pressure, Skin Thickness, and Pedigree score.
   - **Cardiovascular / Heart Disease**: Evaluates Age, Sex, Chest Pain Type (cp), Resting BP, Cholesterol, Resting ECG, Max Heart Rate, ST Depression (oldpeak), and Fluoroscopy vessels.
   - **Chronic Kidney Disease (CKD)**: Evaluates Serum Creatinine, Urine Albumin, Specific Gravity, Hemoglobin, Blood Urea, and Hypertension.
   - **General Multi-Disease Symptom Classifier**: Cross-analyzes 14 acute/subacute presenting symptoms against 41 conditions (Dengue, Malaria, Typhoid, Pneumonia, Jaundice, etc.).
2. **Confidence Score & Risk Indicator**:
   - Mathematical probability calibration (`0% - 100%`) reflecting exact model decision boundary distance.
   - Objective risk categorization: Low, Moderate, and High Risk.
3. **SHAP (Explainable AI)**:
   - Identifies which clinical features drove risk up (positive contribution) versus which markers provided protective reduction (negative contribution).
   - Clear visual bar chart with baseline averages and patient values.
4. **AI Health Assistant (Gemini 3.8 Flash)**:
   - Server-side integration using `@google/genai`.
   - Context-aware conversation retaining patient's active prediction, lab values, and risk level.
   - Strict clinical guardrails with emergency symptom detection and automatic offline guidance fallback.
5. **Voice Symptom Input**:
   - Uses browser Web Speech API (`SpeechRecognition`).
   - Allows users to speak symptoms, review/edit the recognized transcript, and automatically map symptoms.
6. **Text-to-Speech (TTS)**:
   - Uses browser SpeechSynthesis for auditory reading of prediction results, precautions, and AI assistant responses.
7. **Downloadable PDF Health Report**:
   - Generates official clinical report containing patient details, test metrics, confidence score, risk indicator, SHAP explanation, precautions, and doctor discussion checklist.
8. **Prediction History & Authentication**:
   - User registration and login with bcrypt password hashing and JWT authentication.
   - History table with search, disease filtering, and direct report downloads.

---

## 💻 Local Windows VS Code Development Setup

### Prerequisites
- [Node.js](https://nodejs.org/) (version 18 or higher)
- [Python](https://www.python.org/) (version 3.10 or higher)
- [Git](https://git-scm.com/)

### Step 1: Clone the Repository
```powershell
git clone <repository-url>
cd medipredict
```

### Step 2: Running the Full-Stack Application (Node.js & Express)
The repository is equipped with a unified full-stack server running Express and Vite middlewares:

```powershell
# 1. Install dependencies
npm install

# 2. Copy environment template
Copy-Item .env.example .env

# 3. Start the dev server
npm run dev
```
The application will be live at `http://localhost:3000`.

### Step 3 (Optional): Running the Python FastAPI ML Server
If you wish to run the standalone Python ML server:

```powershell
# 1. Navigate to backend
cd backend

# 2. Create Python virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install requirements
pip install -r requirements.txt

# 4. Start FastAPI server
python main.py
```
FastAPI documentation will be available at `http://localhost:8000/docs`.

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:
```env
# Optional: Google Gemini API Key for AI Health Assistant
GEMINI_API_KEY=your_gemini_api_key_here

# JWT Secret for session authentication
JWT_SECRET=medipredict_clinical_jwt_secret_key_2026

# Server Port (default: 3000)
PORT=3000
```

---