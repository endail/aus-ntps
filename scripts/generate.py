import json
import glob
import subprocess

def resolvedns(endpoint):
  return subprocess.run(
    ["nslookup", "-querytype=A", "-retry=0", "-timeout=3", endpoint],
    capture_output=True,
    text=True).returncode == 0

def ntpdig(endpoint):
  result = subprocess.run(
    ["ntpdig", "-j", "-t 5", endpoint],
    capture_output=True,
    text=True,
    timeout=5)
  return json.loads(result.stdout)


results = []

for file in glob.glob("src/*.json"):
  with open(file) as f: data = json.load(f)
  listresult = { name: data["name"], description: data["description"], servers: [] }
  
  for server in data["servers"]:
    srvresult = { name: server["name"], endpoints: [] }
    
    for endpoint in server["endpoints"]:
      eptresult = { endpoint: endpoint, dns: False, ntp: None }
      
      if resolvedns(endpoint):
        eptresult.dns = True
        
        try:
          dig = ntpdig(endpoint)
          eptresult.ntp.stratum = dig.stratum
          eptresult.ntp.ip = dig.ip
        except:
          print("ntpdig failed for " + endpoint)
      
      srvresult.endpoints.append(eptresult)
    listresult.servers.append(srvresult)
  results.append(srvresult)
  

# print results
for list in results:
  print("List name: " + list.name)
  print("List description: " + list.description)
  print()
  for(srv in list.endpoints):
    print("\tServer name: " + srv.name)
    for(ept in srv.endpoints):
      print("\t\t" + ept.endpoint)
      print("\t\t\t" + ept.dns)
      print("\t\t\t" + ept.ip)
      print("\t\t\t" + ept.stratum)
      print()
    print()
  print()

print("DONE!")
  
