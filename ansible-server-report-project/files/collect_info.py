import json
import csv
import subprocess
import socket
from datetime import datetime

# Load command map
with open('/tmp/server_report/command_map.json') as f:
    commands = json.load(f)

hostname = socket.gethostname()
filename = f"/tmp/server_report/server_report_{hostname}.csv"

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Metric', 'Output'])

    for key, cmd in commands.items():
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
            output = result.decode('utf-8').strip().replace('\n', ' | ')
        except Exception:
            output = 'Command Failed'
        writer.writerow([key, output])
