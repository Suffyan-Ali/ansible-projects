#  Ansible Remote Output Collector

This project uses **Ansible** to collect **disk usage information (`df -h`)** from multiple remote Linux servers and saves the output locally on the **control node** for reporting and analysis.

---

##  Use Case

This solution is ideal for **system administrators** and **DevOps engineers** who need to:
- Collect remote command output from multiple servers
- Store the output in a structured and readable way
- Automate server health checks and inventory collection

---

## Prerequisites

- Ansible installed on the control node
- SSH access to target servers with key-based authentication
- Python installed on remote machines (default with most Linux distros)

