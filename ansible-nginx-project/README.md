# 🚀 Ansible Nginx Project

This is a simple yet powerful **Ansible project** that automatically sets up an **Nginx web server** and deploys a custom HTML page to it. It's a great starting point for those who are learning **Ansible for DevOps and Cloud Automation**.

---

## 📁 Project Structure

ansible-nginx-project/
├── inventory.ini # Inventory file listing the target hosts
├── playbook.yml # Main Ansible playbook to install and configure Nginx
└── files/
└── index.html # The HTML page that will be deployed to the server


---

## 📌 What This Project Does

- Installs **Nginx** on the target host
- Ensures the Nginx service is enabled and running
- Replaces the default `index.html` with a custom HTML page
- Demonstrates the power of **Ansible automation** in a practical way

---

## 🛠️ Requirements

- **Ansible** installed on your control machine
- Access to a **Linux-based target server** (Ubuntu, CentOS, etc.)
- SSH access with a private key or password
- Python installed on the remote server

---

## 📂 `inventory.ini` Example

```ini
[web]
your_server_ip ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa


Replace your_server_ip and ansible_user as per your target host configuration.

🌐 After Deployment
Once the playbook finishes, open your browser and go to:

http://your_server_ip
