import subprocess

command1 = subprocess.Popen(['vncviewer', '192.168.196.134:5900'])
command2 = subprocess.Popen(['vncviewer', '192.168.196.134:5901'])


print command1
print command2
