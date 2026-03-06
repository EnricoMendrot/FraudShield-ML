# FraudShield ML

**FraudShield ML** is a professional, end-to-end fraud detection system that bridges the gap between Machine Learning research and real-world production applications. It features a high-performance **FastAPI** backend and a premium **Glassmorphism** dashboard for real-time transaction analysis.

---

## Key Features

### Machine Learning Engine
- **Algorithm**: Random Forest Classifier optimized for highly imbalanced data.
- **Preprocessing**: Implements `RobustScaler` and `SMOTE` (Synthetic Minority Over-sampling Technique) for class balancing.
- **Custom Threshold**: fine-tuned to **0.6** to ensure high-precision detection of fraudulent activities.
- **Data Source**: Trained on the world-renowned [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

### Professional API (Backend)
- **FastAPI**: Asynchronous, high-performance Python framework.
- **Security**: Robust authentication system using **Password Hashing** (Passlib/Bcrypt).
- **CORS Support**: Configured for seamless communication with frontend dashboards.
- **Pydantic Schemas**: Strict data validation for all 30 transaction features.

### Intelligent Dashboard (Frontend)
- **Modern UI**: Sleek **Dark Mode** design with **Glassmorphism** aesthetics.
- **Real-Time Simulation**: "Simulate Transaction" feature that pre-fills the dashboard with real samples from the processed dataset.
- **Interactive Results**: Instant visual feedback (Safe vs. Fraudulent) with calculated probability.

---

## Project Structure

```text
FraudShield-ML/
├── api/                # FastAPI Application
│   ├── main.py         # App entry point & CORS
│   ├── auth_routes.py  # User authentication
│   ├── predict.py      # ML Inference logic
│   └── schemas.py      # Pydantic data models
├── frontend/           # Web Interface
│   ├── templates/      # HTML (index.html)
│   └── src/            # Static assets (style.css, script.js)
├── src/                # ML Pipeline
│   ├── preprocessing.py# Data cleaning & Scaling
│   └── train.py        # Model training & Smote
├── models/             # Serialized .pkl artifacts
├── data/               # Raw and Processed datasets
└── notebooks/          # Exploratory Data Analysis (EDA)
```

---

## Getting Started

### Requirements
- Python 3.9+
- Virtual Environment (recommended)

### Installation
```powershell
# Clone the repository
git clone https://github.com/EnricoMendrot/FraudShield-ML.git
cd FraudShield-ML

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the API
```powershell
uvicorn api.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`. You can access the interactive documentation (Swagger) at `/docs`.

### 4. Running the Frontend
Simply open `frontend/templates/index.html` in your browser or use the **VS Code Live Server** extension for the best experience.

---

##  API Endpoints (Brief)

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/register` | Register new users |
| `POST` | `/auth/login` | Authenticate and receive token |
| `POST` | `/predict/new` | High-speed fraud inference (30 features) |
| `GET` | `/predict/history` | Retrieve prediction logs |

---

## Technologies Used

- **Python**: Core logic.
- **Scikit-Learn**: Machine Learning algorithms.
- **FastAPI**: Backend infrastructure.
- **Pydantic**: Data validation.
- **Pandas/Numpy**: Data manipulation.
- **HTML5/CSS3/JS**: Premium frontend dashboard.

---

##  License
Distributed under the MIT License. See `LICENSE` for more information.

---
Developed by [Enrico Mendrot](https://github.com/EnricoMendrot) - *Making transactions safer with Artificial Intelligence.*
