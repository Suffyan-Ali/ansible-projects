# 🧠 Ansible Playbook Deep Dive

This is  **Ansible Playbook Deep Dive** repository!  
This project is created to complete understanding of Ansible Playbooks from every practical angle.  
Whether you are new to Ansible or want to deepen your knowledge, this repository is for you.

---

## 📘 What is an Ansible Playbook?

An **Ansible Playbook** is a YAML file that defines tasks to be executed on remote systems. It is the core component of Ansible used for configuration management, automation, and orchestration.

Playbooks let you:

- Install and configure software
- Manage files and users
- Start/stop services
- Automate repetitive tasks
- Deploy applications
- And much more…



---

## ✅ Key Concepts Covered

### 1. 🏁 Basic Playbook Syntax
- YAML structure
- Tasks and modules
- Hosts and user declaration
- Privilege escalation (`become`)

### 2. 🛠 Variables
- Global, group, and host variables
- Variable files (`group_vars`, `host_vars`)
- Inline variables and facts

### 3. 🔁 Loops
- `loop` and `with_items`
- Looping over lists and dictionaries

### 4. 🧠 Conditionals
- `when` statements
- Conditional execution using facts/variables

### 5. 📣 Handlers
- Define tasks triggered by notifications
- Useful for service restarts and config reloads

### 6. 🏷 Tags
- Run specific tasks using `--tags`

### 7. 🔐 Ansible Vault
- Encrypt sensitive data (passwords, tokens)
- Use `ansible-vault` for secret management

---

##  Try These Playbooks

| Playbook                        | Description                                  |
|--------------------------------|----------------------------------------------|
| `basic-playbook.yml`           | A basic Hello World playbook                 |
| `playbook-with-vars.yml`       | Demonstrates how to use variables            |
| `playbook-with-conditionals.yml` | Runs tasks based on conditions              |
| `playbook-with-loops.yml`      | Loops through package installs or users      |
| `playbook-with-handlers.yml`   | Demonstrates handlers and notifications      |

---

##  Sample Inventory

```ini
[webservers]
192.168.1.100 ansible_user=ubuntu

[dbservers]
192.168.1.101 ansible_user=ubuntu


