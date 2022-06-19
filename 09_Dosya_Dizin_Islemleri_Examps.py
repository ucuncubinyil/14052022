import os

komut = "calc"

# os.system(komut)
os.system("hostname")
os.system("ipconfig")

import subprocess
batcmd="ipconfig"
result = subprocess.check_output(batcmd, shell=True)
print(result)