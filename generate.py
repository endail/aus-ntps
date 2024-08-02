from src.NtpDiscovery import NtpDiscovery, NtpLookupCollection
import random
from datetime import datetime, timezone

coll = NtpLookupCollection.fromfile("data/lookups.json")
coll._data = random.sample(coll._data, 1)
coll.validate()
disc = NtpDiscovery(coll)
report = disc.run()

with open("README.md", "w") as readme:
 readme.write(open("README-header.md", "r").read())
 readme.write("\n")
 readme.write(report.get_markdown())
 readme.write("Data last updated {}\n".format(datetime.now(timezone.utc)))
