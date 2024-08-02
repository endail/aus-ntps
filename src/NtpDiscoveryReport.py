from .Endpoint import Endpoint
from .NtpDetail import NtpDetail

class NtpDiscoveryReport(object):

 def __init__(self) -> None:
  super().__init__()
  self._data: dict[str, dict[Endpoint, list[NtpDetail]]] = {}

 def __iter__(self) -> iter:
  return iter(self._data)

 def __len__(self) -> int:
  total = 0
  for _, endpoints in self._data.items():
   for _, ntps in endpoints.items():
    total += len(ntps)
  return total

 def set_keys(self, name: str, endpoint: Endpoint):
  if not name in self._data:
   self._data[name] = {}
  if not endpoint in self._data[name]:
   self._data[name][endpoint] = []

 def append(self, name: str, endpoint: Endpoint, ntp: NtpDetail):
  self.set_keys(name, endpoint)
  self._data[name][endpoint].append(ntp)

 def append_multiple(self, name: str, endpoint: Endpoint, ntps: list[NtpDetail]):
  self.set_keys(name, endpoint)
  for ntp in ntps:
   self.append(name, endpoint, ntp)

 def generate_markdown(self):
  for name, endpoint_dict in sorted(self._data.items()):
   for endpoint, ntps in sorted(endpoint_dict.items(), key=lambda item: str(item[0])):
    yield {
     "name": name,
     "endpoint": endpoint,
     "ntps": ntps
    }

 def get_markdown(self) -> str:
  buff: str = ""
  for name, endpoint_dict in sorted(self._data.items()):
   buff += "### {}\n\n".format(name)
   buff += "| endpoint | ip address | version | stratum | leap |\n"
   buff += "| -------- | ---------- | ------- | ------- | ---- |\n"
   for endpoint, ntps in sorted(endpoint_dict.items(), key=lambda item: str(item[0])):
    buff += "|`{}`|||||\n".format(endpoint)
    #buff += ("||||" if len(ntps) > 0 else "n/a|n/a|n/a|n/a|") + "\n"
    for ntp in ntps:
     buff += "||{}|{:d}|s{:d}|{}|\n".format(ntp.ip(), ntp.version(), ntp.stratum(), ntp.leap())
   buff += "\n"
  return buff
