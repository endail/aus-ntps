import json
import glob
import subprocess

def resolvedns(endpoint):
  return subprocess.run(
    ["nslookup", "-querytype=A", "-retry=0", "-timeout=3", endpoint],
    capture_output=True,
    text=True).returncode == 0

def ntpdig(endpoint):
  print("ntpdigging " + endpoint)
  result = subprocess.run(
    ["ntpdig", "-j", "-t 5", endpoint],
    capture_output=True,
    text=True,
    timeout=5)
  print(result.stdout)
  return json.loads(result.stdout)


results = []

for file in glob.glob("src/*.json"):
  with open(file) as f: data = json.load(f)
  listresult = { "name": data["name"], "description": data["description"], "servers": [] }
  
  for server in data["servers"]:
    srvresult = { "name": server["name"], "endpoints": [] }
    
    for endpoint in server["endpoints"]:
      eptresult = { "endpoint": endpoint, "dns": False, "ntp": None }
      
      if resolvedns(endpoint):
        eptresult["dns"] = True
        
        try:
          dig = ntpdig(endpoint)
          print(dig)
          eptresult["ntp"] = {
            "stratum": dig["stratum"],
            "ip": dig["ip"]
          }
        except subprocess.TimeoutExpired:
          print("ntpdig timed out for " + endpoint)
        except json.JSONDecodeError:
          print("failed to parse json for " + endpoint)
          
      srvresult["endpoints"].append(eptresult)
    listresult["servers"].append(srvresult)
  results.append(listresult)






with open("README.md", "w") as readme:
  readme.write(open("README-header.md", "r").read())

  # sort by list name
  results.sort(key=lambda l: l["name"])

  readme.write("## Table of Contents\n")
  for list in results:
    readme.write("- [" + list["name"] + "](#" + list["name"] + ")\n") 
  
  for list in results:
    readme.write("## " + list["name"] + "\n")

    # sort by server name
    list["servers"].sort(key=lambda s: s["name"])
    
    for srv in list["servers"]:
      readme.write("### " + srv["name"] + "\n")
      readme.write("| Endpoint                           | DNS? | IP               | Stratum |\n")
      readme.write("| :--------------------------------- | ---: | :--------------- | ------: |\n")
      
      # sort by endpoint
      srv["endpoints"].sort(key=lambda e: e["endpoint"])
      
      for ept in srv["endpoints"]:
        readme.write("|" + ept["endpoint"])
        readme.write("|" + "Y" if ept["dns"] else "N")
        if ept["ntp"] is not None:
          readme.write("|" + ept["ntp"]["ip"])
          readme.write("|" + str(ept["ntp"]["stratum"]))
        else:
          readme.write("|||\n")
            
      readme.write("\n")
    readme.write("\n")
    
  #print("List name: " + list["name"])
  #print("List description: " + list["description"])
  #print("")
  #for srv in list["servers"]:
  #  print("\tServer name: " + srv["name"])
  #  for ept in srv["endpoints"]:
  #    print("\t\t" + ept["endpoint"])
  #    print("\t\t\tResolved?: " + "Yes" if ept["dns"] else "No")
  #    if ept["ntp"] is not None:
  #      print("\t\t\tIP: " + ept["ntp"]["ip"])
  #      print("\t\t\tStratum: " + str(ept["ntp"]["stratum"]))
  #    else:
  #      print("\t\t\tNTP details unavailable")
  #    print("")
  #  print("")
  #print("")

print("DONE!")
  
