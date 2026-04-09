#  Flask DevOps Automation App

##  Overview

This project demonstrates a **complete DevOps workflow** using a Flask application integrated with:

* Python scripting for automation
* Docker containerization
* CI/CD pipeline using GitHub Actions
* Kubernetes deployment (local)

The application allows execution of automation scripts via API endpoints, simulating real-world DevOps tasks.

---

##  Objectives

* Automate tasks using Python scripts
* Containerize applications using Docker
* Implement CI/CD pipeline
* Understand Kubernetes deployment basics
* Build a fully local DevOps project (no cloud required)

---

##  Tech Stack

* **Backend:** Python (Flask)
* **Scripting:** Python
* **CI/CD:** GitHub Actions
* **Containerization:** Docker
* **Orchestration:** Kubernetes (Minikube/KIND)
* **Version Control:** Git & GitHub

---

##  Project Structure

```bash
flask-devops-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── k8s-deployment.yaml
├── scripts/
│   ├── cleanup_logs.py
│   ├── fetch_github.py
│   └── send_report.py
├── logs/
├── screenshots/
└── .github/
    └── workflows/
        └── ci-cd.yaml
```

---

##  Application Endpoints

| Endpoint               | Description           |
| ---------------------- | --------------------- |
| `/`                    | App status            |
| `/health`              | Health check          |
| `/info`                | App details           |
| `/run_script/<script>` | Execute Python script |

---

##  Running the Application

###  Build Docker Image

```bash
docker build -t flask-app .
```

###  Run Container

```bash
docker run -p 5200:5200 flask-app
```

###  Access in Browser

* http://localhost:5200
* http://localhost:5200/health
* http://localhost:5200/info
* http://localhost:5200/run_script/cleanup_logs

---

##  Docker Details

* Uses lightweight Python image
* Runs Flask app with Gunicorn
* Exposes port **5200**
* Ensures consistent environment across systems

---

## 🔁 CI/CD Pipeline

###  Location:

`.github/workflows/ci-cd.yaml`

###  Workflow Steps:

1. Checkout code
2. Build Docker image
3. Run container
4. Test `/health` endpoint

###  Trigger:

* On every push to `main` branch

---

## Kubernetes Deployment (Local)

###  Apply deployment

```bash
kubectl apply -f k8s-deployment.yaml
```

###  Verify

```bash
kubectl get pods
kubectl get svc
```

* Runs container inside a pod
* Exposes service using NodePort

---

##  Python Automation Scripts

###  cleanup_logs.py

* Deletes log files older than 7 days

###  fetch_github.py

* Fetches latest commits from GitHub

###  send_report.py

* Generates daily report file

---

## 📸 Screenshots

###  Application Running

<img width="1165" height="656" alt="Overview" src="[https://github.com/user-attachments/assets/7154b7f2-db0a-445f-9d82-648a2f755e3f](https://github.com/VSUBASHRAJ/CI-CD-Pipeline-for-Flask-Application/blob/main/flask-devops-app/Screenshots/Application%20Running.png)" />

###  Health Check

!(flask-devops-app/screenshots/health.png)

###  Script Execution

![Script](screenshots/script.png)

###  Docker Container

![Docker](screenshots/docker.png)

###  CI/CD Pipeline

![Pipeline](screenshots/pipeline.png)

###  Kubernetes Deployment

![Kubernetes](screenshots/k8s.png)

---

## 📊 Problem Solved

###  Before:

* Manual task execution
* Environment inconsistencies
* No automation

###  After:

* Automated workflows using Python
* Containerized environment with Docker
* Continuous integration using CI/CD
* Scalable deployment using Kubernetes

---

##  Key Features

* REST API-based automation
* Dockerized application
* CI/CD pipeline integration
* Kubernetes deployment support
* Real-world DevOps workflow simulation

---

##  Future Enhancements

* Add monitoring (Prometheus, Grafana)
* Implement logging system
* Integrate cloud deployment (AWS/GCP)
* Add authentication

---

##  Learning Outcomes

* CI/CD pipeline implementation
* Docker containerization
* Kubernetes basics
* Python scripting for automation
* DevOps workflow understanding

---

##  Author

**Subashraj Vadivel**
📧 [subashrajv95@gmail.com](mailto:subashrajv95@gmail.com)
🔗 GitHub: https://github.com/VSUBASHRAJ
🔗 LinkedIn: https://www.linkedin.com/in/v-subash-raj/
