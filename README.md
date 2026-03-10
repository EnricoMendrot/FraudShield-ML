# FraudShield ML
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**FraudShield ML** is a professional, end-to-end fraud detection system that bridges the gap between Machine Learning research and real-world production applications. It features a high-performance **FastAPI** backend, a **SQLite** database with **Alembic** migrations, a full **CI/CD pipeline** via GitHub Actions, and a premium **Glassmorphism** dashboard for real-time transaction analysis.

---

## Key Features

### Machine Learning Engine
- **Algorithm**: Random Forest Classifier optimized for highly imbalanced data.
- **Preprocessing**: Implements `RobustScaler` and `SMOTE` (Synthetic Minority Over-sampling Technique) for class balancing.
- **Custom Threshold**: Fine-tuned to **0.6** to ensure high-precision detection of fraudulent activities.
- **Data Source**: Trained on the world-renowned [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).

### Professional API (Backend)
- **FastAPI**: Asynchronous, high-performance Python framework.
- **Security**: Robust authentication system using **Password Hashing** (Passlib/Bcrypt) with a dedicated `utils.py` and `dependencies.py` for JWT dependency injection.
- **Database**: **SQLAlchemy** ORM with **SQLite**, managed via **Alembic** migrations (`alembic.ini` + `migrations/`).
- **CORS Support**: Configured for seamless communication with frontend dashboards.
- **Pydantic Schemas**: Strict data validation for all 30 transaction features.

### DevOps & Code Quality
- **CI/CD**: Automated pipeline with **GitHub Actions** — runs linting and tests on every push and pull request.
- **Containerization**: Production-ready **Dockerfile** (`python:3.11-slim`) and **Docker Compose** for easy deployment.
- **Linting & Formatting**: **Ruff** configured via `pyproject.toml` (enforces PEP 8, isort, pyflakes, bugbear, pyupgrade).
- **Testing**: **Pytest** test suite covering authentication (`test_auth.py`) and prediction (`test_predict.py`) flows.
- **Makefile**: Convenience commands for common development tasks.

### Intelligent Dashboard (Frontend)
- **Modern UI**: Sleek **Dark Mode** design with **Glassmorphism** aesthetics.
- **Real-Time Simulation**: "Simulate Transaction" feature that pre-fills the dashboard with real samples from the processed dataset.
- **Interactive Results**: Instant visual feedback (Safe vs. Fraudulent) with calculated probability.

---

## Project Structure

```text
FraudShield-ML/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD pipeline
├── api/                    # FastAPI Application
│   ├── main.py             # App entry point & CORS
│   ├── auth_routes.py      # User authentication endpoints
│   ├── predict.py          # ML inference logic
│   ├── schemas.py          # Pydantic data models
│   ├── models.py           # SQLAlchemy ORM models
│   ├── database.py         # Database session setup
│   ├── dependencies.py     # JWT auth dependency injection
│   └── utils.py            # Password hashing helpers
├── frontend/               # Web Interface
│   ├── templates/          # HTML (index.html)
│   └── src/                # Static assets (style.css, script.js)
├── src/                    # ML Pipeline
│   ├── preprocessing.py    # Data cleaning & scaling
│   └── train.py            # Model training & SMOTE
├── tests/                  # Pytest test suite
│   ├── conftest.py         # Shared fixtures
│   ├── test_auth.py        # Authentication tests
│   └── test_predict.py     # Prediction endpoint tests
├── migrations/             # Alembic database migrations
├── models/                 # Serialized .pkl model artifacts
├── data/                   # Raw and processed datasets
├── notebooks/              # Exploratory Data Analysis (EDA)
├── monitoring/             # Application logs
├── Dockerfile              # Production container image
├── docker-compose.yml      # Multi-service orchestration
├── Makefile                # Developer convenience commands
├── pyproject.toml          # Project config & Ruff settings
└── requirements.txt        # Python dependencies
```

---

## Getting Started

### Requirements
- Python 3.11+
- Docker & Docker Compose (for containerized deployment)

### Option 1: Local Development

```powershell
# Clone the repository
git clone https://github.com/EnricoMendrot/FraudShield-ML.git
cd FraudShield-ML

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
make install
# or: pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start the API
uvicorn api.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs (Swagger UI) at `/docs`.

### Option 2: Docker (Recommended)

```powershell
# Build and run all services
make run
# or: docker compose up -d
```

### Running the Frontend
Open `frontend/templates/index.html` in your browser, or use the **VS Code Live Server** extension for the best experience.

---

## Makefile Commands

| Command | Description |
| :--- | :--- |
| `make install` | Install Python dependencies |
| `make run` | Start the application via Docker Compose |
| `make test` | Run the Pytest test suite |
| `make lint` | Check code quality with Ruff |
| `make format` | Auto-format code with Ruff |
| `make clean` | Remove `.pyc` and cache files |

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Authenticate and receive JWT token |
| `POST` | `/predict/new` | High-speed fraud inference (30 features) |
| `GET` | `/predict/history` | Retrieve prediction history logs |

---

## Technologies Used

| Category | Technologies |
| :--- | :--- |
| **ML** | Scikit-Learn, Pandas, NumPy, imbalanced-learn (SMOTE) |
| **Backend** | FastAPI, Pydantic, SQLAlchemy, Alembic, Passlib/Bcrypt |
| **DevOps** | Docker, GitHub Actions, Ruff, Pytest |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Runtime** | Python 3.11, Uvicorn |

---

## License
Distributed under the MIT License. See `LICENSE` for more information.

---
Developed by [Enrico Mendrot](https://github.com/EnricoMendrot) — *Making transactions safer with Artificial Intelligence.*
