# Ansible Server Report Automation Project

This project automates the process of collecting daily server details like IP address, hostname, and storage information from multiple Linux servers and sends the generated report via email. It uses a combination of **Ansible** and **Python** to ensure a seamless and efficient workflow.

---

## 🛠️ Project Requirements

- Python 3.6+ installed on local and remote machines
- Ansible installed on the local control machine
- SSH access to remote Linux servers
- Python standard libraries on local system for email

---

## 📁 Project Structure

```
ansible-server-report-project/
├── inventory.ini ansible-server-report-project             # Ansible inventory file with server details
├── playbook.yml               # Main Ansible playbook for automation
├── files/
│   ├── command_map.json       # JSON file with Linux commands
│   └── collect_info.py        # Python script to collect server info
├── reports/                   # Folder to store fetched CSV reports
├── send_report.py             # Local Python script to email the latest report
└── README.md                  # Project documentation
```

---

## 📌 Workflow Overview

1. **Ansible playbook**:
   - Connects to each server
   - Copies `collect_info.py` and `command_map.json`
   - Executes the script remotely to gather server details
   - Generates a CSV report on each server
   - Fetches the report back to the `reports/` folder on the local machine

2. **send_report.py**:
   - Finds the most recent CSV report in `reports/`
   - Sends it as an email attachment to the manager

---

## 📂 inventory.ini Example

```ini
[servers]
192.168.1.101 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
192.168.1.102 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```

---

## ▶️ How to Run

1. Run the Ansible playbook:

```bash
ansible-playbook -i inventory.ini playbook.yml
```

2. Send the report via email:

```bash
python3 send_report.py
```

---

## 🧾 collect_info.py (Sample Overview)

- Reads `command_map.json`
- Executes each command using `subprocess`
- Writes output to a CSV file (`server_report_<hostname>.csv`)

---

## 🧾 command_map.json Example

```json
{
  "Hostname": "hostname",
  "IP Address": "hostname -I",
  "Disk Usage": "df -h"
}
```

---

## 📧 Email Script Configuration

Ensure you configure SMTP details inside `send_report.py`, such as:

- SMTP server (e.g., smtp.gmail.com)
- Port
- Sender email and password (use App Passwords if using Gmail)
- Recipient email address

---

## 📈 Benefits

- Saves daily manual work
- Ensures timely and error-free reporting
- Easy to extend with more server checks
- Helps in production-grade monitoring automation

---

## 👤 Author

**Suffyan Ali**  
Cloud & DevOps Enthusiast | Linux Automation | Infrastructure as Code

---

## 🤝 Contributions

Suggestions, improvements, and PRs are welcome!

---

Happy Automating with Ansible & Python! ⚙️
