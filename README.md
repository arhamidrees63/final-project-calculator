🧮 FastAPI Calculator Application

A full-stack calculator application built with FastAPI, PostgreSQL, and SQLAlchemy, supporting authenticated users, persistent calculation history, and full CRUD operations.
The project includes unit tests, integration tests, end-to-end API tests, and UI tests.

🐳 Docker Hub Image

This project is available as a Docker image on Docker Hub:

🔗 Docker Hub Repository:
https://hub.docker.com/r/arhamidrees63/final-project-fastapi-calculator

Pull Image
docker pull arhamidrees63/final-project-fastapi-calculator:latest

Run Container
docker run -d \
  -p 8000:8000 \
  -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/fastapi_db \
  arhamidrees63/final-project-fastapi-calculator:latest


Access the application at:

http://127.0.0.1:8000

🚀 Features
🔢 Calculator Operations

Addition

Subtraction

Multiplication

Division (with division-by-zero protection)

Supports multiple inputs (e.g. [10, 3, 2])

Results are stored in the database per user

👤 User Authentication

User registration & login

JWT-based authentication

Secure password hashing

Protected calculator endpoints

🗂 Calculation Management

Create calculations

List user calculations

Retrieve calculation by ID

Update calculation inputs

Delete calculations

Each calculation stores:

Type

Inputs

Result

Created & updated timestamps

🖥 Web Dashboard

Web UI available at:

http://127.0.0.1:8000/dashboard


Displays calculation history for logged-in users

🛠 Tech Stack
Layer	Technology
Backend	FastAPI
Database	PostgreSQL
ORM	SQLAlchemy
Auth	JWT (OAuth2 Password Flow)
Testing	Pytest
UI Testing	Playwright
Server	Uvicorn
Language	Python 3.12
📂 Project Structure
app/
├── auth/               # Authentication & JWT logic
├── core/               # App configuration
├── database.py         # Database connection
├── database_init.py    # DB initialization
├── models/             # SQLAlchemy models
│   ├── user.py
│   └── calculation.py
├── operations/         # Calculator operations
├── schemas/            # Pydantic schemas
├── main.py             # FastAPI app entry point
tests/
├── unit/               # Unit tests (calculator logic)
├── integration/        # DB + schema tests
├── e2e/                # End-to-end API tests
└── conftest.py         # Test setup & fixtures

⚙️ Environment Setup
1️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start PostgreSQL (Docker recommended)
docker run --name pg-fastapi \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=fastapi_db \
  -p 5432:5432 \
  -d postgres:16

4️⃣ Set environment variable
export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fastapi_db"

▶️ Running the Application
uvicorn app.main:app --reload


API Docs:

http://127.0.0.1:8000/docs


Dashboard UI:

http://127.0.0.1:8000/dashboard

🧪 Running Tests
Set test database URL
export TEST_DATABASE_URL="postgresql://postgres:postgres@localhost:5432/fastapi_db"

Run all tests
pytest

Run with coverage
pytest --cov=app --cov-report=html


Coverage report will be generated in:

htmlcov/index.html

✅ Test Coverage Includes

Unit tests for calculator operations

Schema validation tests

Database integration tests

Authentication tests

End-to-end API tests

UI tests using Playwright

🔐 Security Notes

Passwords are hashed before storage

JWT tokens are required for protected routes

Users can only access their own calculations

📌 Notes for Grading / Review

Follows clean architecture

Separation of concerns (models, schemas, operations)

Comprehensive test coverage

Database-backed persistence

Production-style authentication flow

👨‍💻 Author

Muhammad Arham
Final Project – FastAPI Calculator Application