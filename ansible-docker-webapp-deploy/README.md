#  Ansible Docker Web App Deployment

This project automates the deployment of a **Dockerized static web application** using **Ansible**. It's designed for DevOps learners and professionals who want to practice Infrastructure as Code (IaC), automated provisioning, and containerized deployments.

With a single command, this playbook:
- Installs Docker and Docker Compose
- Sets up a project directory
- Copies a sample HTML web page
- Launches it inside an **Nginx Docker container**

---

## 📌 Why This Project?

In real-world DevOps workflows, automation and containerization are key. This project simulates how modern teams:
- Use Ansible to provision servers
- Use Docker to containerize and deploy applications
- Ensure infrastructure is consistent and repeatable

---

## 🗂️ Project Structure

ansible-docker-webapp-deploy/
├── inventory.ini
├── playbook.yml
├── files/
│   ├── docker-compose.yml
│   └── app/
│       └── index.html
├── README.md


---

## ⚙️ What It Does (Step-by-Step)

1. Connects to your remote Linux server using SSH
2. Installs Docker and Docker Compose if not already installed
3. Creates a directory `/opt/webapp/` on the server
4. Copies:
   - A `docker-compose.yml` file to define the Nginx container
   - An `index.html` file that becomes the home page
5. Starts the container using Docker Compose

---

## 🛠️ Prerequisites

- Ubuntu/Debian-based remote Linux server
- SSH access to the server
- Ansible installed on your control machine (your laptop or local server)
- Docker and Docker Compose will be installed by the playbook

---



