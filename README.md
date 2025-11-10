🧮 Module 13 – FastAPI Calculator App with JWT Authentication

This project is a FastAPI web app that lets users register, log in securely using JWT authentication, and perform basic arithmetic operations (addition, subtraction, multiplication, and division).
It’s built with FastAPI, PostgreSQL, Docker, and includes automated testing via Pytest and Playwright.

🐳 Docker Hub Image

Docker image available at:
👉 https://hub.docker.com/repository/docker/arhamidrees63/module13

📂 GitHub Repository

Source code repository:
👉 https://github.com/arhamidrees63/assignment13

🚀 How to Run This Project

You can run the project in two ways — via Docker or directly with FastAPI.

🐳 Option 1: Run with Docker (Recommended)
1️⃣ Clone the repository
git clone git@github.com:arhamidrees63/assignment13.git
cd assignment13

2️⃣ Build and start all containers
docker-compose up --build


This will automatically start:

FastAPI backend on http://localhost:8000

pgAdmin on http://localhost:5050

PostgreSQL database in the background

3️⃣ Open the app

Once running, visit:

Swagger API Docs: http://localhost:8000/docs

Frontend Login Page: http://localhost:8000/login

Frontend Register Page: http://localhost:8000/register

pgAdmin (Database GUI): http://localhost:5050

4️⃣ Stop the containers
docker-compose down

💻 Option 2: Run Locally (Without Docker)

If you prefer to run it directly on your system:

1️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the FastAPI app
uvicorn app.main:app --reload


The app will run at:
➡️ http://127.0.0.1:8000/docs

🧪 Run Tests
✅ Run all Pytest tests
pytest

✅ Run only End-to-End (E2E) tests
pytest tests/e2e -v

✅ Run Playwright tests (Frontend)

Make sure the app is running before you execute:

npx playwright test


To pull and run it manually:

docker pull arhamidrees63/module13:latest
docker run -p 8000:8000 arhamidrees63/module13:latest


🧠 Reflection

During this project, I learned how to combine FastAPI, PostgreSQL, and JWT authentication within a Docker environment.
Initially, I struggled with a few issues such as Redis compatibility and environment variables for testing.
After updating imports and adjusting configuration, the app passed all 100 Pytest tests successfully.

The biggest learning experience was setting up CI/CD pipelines and testing user flows with Playwright.
This module helped me understand how authentication, containerization, and testing connect together in real-world web applications.