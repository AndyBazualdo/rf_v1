import subprocess

command1 = subprocess.Popen(['vncviewer', 'localhost:5900'])
command2 = subprocess.Popen(['vncviewer', 'localhost:5901'])
