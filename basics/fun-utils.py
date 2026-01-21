import os 

# command= "df -h"
# command= "date"

# print(os.system(command))

def runCommand(command):
    print(os.system(command))

runCommand("free -h")
runCommand("date")
runCommand("uptime")
