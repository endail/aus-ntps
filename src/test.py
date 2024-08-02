from NtpDiscovery import NtpDiscovery
from NtpLookupCollection import NtpLookupCollection
import random

coll = NtpLookupCollection.fromfile("data/lookups.json")
coll.validate()
coll._data = random.sample(coll._data, 50)
#coll._data = list(filter(lambda lc: lc.get_name() == "Hunter Water", coll._data))

print("Looking up {}".format(list(map(lambda l: l.get_name(), coll))))

disc = NtpDiscovery(coll)
report = disc.run()

for item in report.generate_markdown():
 print("{}: {} -> {}".format(item["name"], item["endpoint"], ", ".join(map(lambda n: n.ip(), item["ntps"]))))

with open("out.md", "w") as f:
 f.write(report.get_markdown())
