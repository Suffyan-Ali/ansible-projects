
#  Ansible Copy & Fetch Module Project

This project showcases the real-world usage of **Ansible's `copy` and `fetch` modules** to automate:

- Deployment of files to remote Linux servers.
- Retrieval of logs and other files from remote servers.

It's ideal for DevOps engineers automating file operations across multiple nodes in production, staging, or development environments.

---

##  Use Case

In a typical enterprise setup:

- You need to **distribute configuration or notice files** to multiple Linux servers.
- You’re responsible for **centralizing logs or backups** from distributed systems for auditing or troubleshooting.

Using Ansible:
- The **`copy`** module lets you transfer files from the control node to managed nodes.
- The **`fetch`** module helps pull files from remote nodes to your control node.


---

##  Prerequisites

- Ansible installed on the control node
- SSH key-based access to managed hosts
- Linux-based servers (Ubuntu/CentOS/etc.)




