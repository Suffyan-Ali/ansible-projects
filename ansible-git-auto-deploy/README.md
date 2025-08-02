#  Git Auto Deploy with Ansible

This project sets up a **Git-based automatic deployment system** using **Ansible**, **Nginx**, and **Git hooks**. It allows developers to push code to a remote Git repository and automatically deploy it to a live web server perfect for static websites and rapid development workflows.

---

## 📦 Project Overview

With this setup:

- You push your code to a **remote bare Git repo** hosted on the target server.
- A **post-receive Git hook** automatically checks out the latest commit to a deploy directory.
- **Nginx** serves the content from the deployed directory.
- **Ansible** automates the entire setup process.

---

## 📁 Project Structure

git-auto-deploy/
├── inventory.ini 
├── playbook.yml 
├── files/
│ ├── post-receive 
│ └── index.html 
└── README.md 


---

## ⚙️ Technologies Used

- **Ansible**: Automation and provisioning
- **Git**: Version control and hook mechanism
- **Nginx**: Web server to serve deployed code
- **Linux (Ubuntu)**: Tested on Ubuntu 20.04/22.04

---

## 🛠️ Requirements

- A control machine with **Ansible** installed
- A **Linux-based target server** with SSH access
- Git installed on both local and remote machines
- Python installed on the remote server


