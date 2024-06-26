import json
import glob
import subprocess

for file in glob.glob("src/*.json"):

  f = open(file)
  data = json.load(f)
  f.close()

  print(data["description"])
  
  for server in data["servers"]:
    print(server["name"])

    for endpoint in server["endpoints"]:
      print("Checking " + endpoint + "...")

      try:
        result = subprocess.run(["nslookup", endpoint, "1.1.1.1"], capture_output=True, text=True, timeout=5)
        print("DNS: " + "OK" if result.returncode == 0 else "Fail")
      except subprocess.TimeoutExpired:
        print("Timeout")
        
      if result.returncode != 0:
        continue

      try:
        result = subprocess.run(["ntpdig", "-j", "-t 5", endpoint], capture_output=True, text=True, timeout=5)
        print("ntpdig success?: " + "Yes" if result.returncode == 0 else "No")
      except subprocess.TimeoutExpired:
        print("Timeout")
      
      if result.returncode != 0:
        continue
        
      ntpout = json.loads(result.stdout)
      print("Host: %s, IP: %s, Stratum: %s" % (ntpout["host"], ntpout["ip"], ntpout["stratum"]))
        
