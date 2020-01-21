import subprocess

command1 = subprocess.Popen(['vncviewer', '192.168.196.134:5900'])
command2 = subprocess.Popen(['vncviewer', '192.168.196.134:5901'])

output = command1.communicate()[0]
print output
output = command2.communicate()[0]
print output
