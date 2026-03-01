# Multi-Agent AI Academic & Career Intelligence System

## 🚀 Project Overview
This is a scalable, multi-agent AI application designed to provide personalized academic and career guidance. It uses a **Multi-Agent Orchestrator** to run four specialized AI agents in parallel, ensuring high performance and modularity.

### 🤖 The Agents
1. **Academic Agent:** Analyzes GPA and academic consistency.
2. **Career Agent:** Uses Gemini AI to suggest career paths based on interests.
3. **Skill Gap Agent:** Identifies missing technical skills.
4. **Resume Agent:** Provides feedback on resume content.

---

## 📋 User Stories (Requirement #1)
- **US1:** As a student, I want to submit my academic profile so I can receive structured career advice.
- **US2:** As a developer, I want the system to process agents in parallel (using asyncio) to ensure the application is scalable.
- **US3:** As a user, I want a web interface to easily interact with the AI agents.
- **US4:** As a DevOps engineer, I want a CI/CD pipeline to automate the building and deployment of the Docker image.

---

## 🛠️ Technology Stack
- **Backend:** FastAPI (Python)
- **AI Models:** Google Gemini Pro
- **DevOps:** Docker, GitHub Actions, Jenkins
- **Frontend:** HTML5, JavaScript (Fetch API)

---

## 🏗️ CI/CD Pipeline Stages (Requirement #9, #10, #11)
The project uses GitHub Actions with a 3-stage pipeline:
1. **Stage 1: Clone** - Fetches the latest code from the repository.
2. **Stage 2: Build** - Installs Python dependencies and validates the environment.
3. **Stage 3: Docker Build & Push** - Packages the app into a Docker image and pushes it to a public repository on DockerHub.

---

## 🐳 How to Run (Requirement #13, #14)
The Docker image is publicly available on DockerHub.

### 1. Pull the Image
```bash
docker pull your-dockerhub-username/multi-agent-ai:latest

----
## 📖 User Manual (Added by Desigaa)

### 1. Accessing the Dashboard
Go to `http://16.171.3.230:8000` in your web browser.

### 2. Entering Data
- **Name:** Enter your full name.
- **GPA:** Enter your score (e.g., 3.8).
- **Skills:** Type skills separated by commas (e.g., Python, SQL).
- **Interests:** List your career goals.

### 3. Understanding Results
- **Academic Agent:** Validates if your GPA meets industry standards.
- **Career Recommendations:** Uses AI to predict your best career path.
- **Skill Gap:** Tells you exactly what technologies to learn next.

---
## 📖 Usage Instructions (Contributed by Desigaa)
1. **Launch**: Ensure the Docker container is running on Port 8000.
2. **Input**: Enter student GPA (0.0 - 4.0), technical skills, and career interests.
3. **Analyze**: Click 'Run Multi-Agent Analysis' to trigger the parallel AI agents.
4. **Review**: Check the dashboard for segmented insights from the Academic, Career, Skill-Gap, and Resume agents.