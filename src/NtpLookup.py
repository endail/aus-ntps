import dns.name
from .Endpoint import Endpoint

class NtpLookup(object):

 DEFAULT_HTTPS_PORT: int = 443
 DEFAULT_NTP_PORT: int = 123

 def __init__(self, data: dict) -> None:
  super().__init__()
  self._data: dict = data

 def __str__(self) -> str:
  return self.get_name() if self.has_name() else None

 def has_name(self) -> bool:
  return "name" in self._data and type(self._data["name"]) == str

 def get_name(self) -> str:
  return self._data["name"]

 def has_categories(self) -> bool:
  return "categories" in self._data and type(self._data["categories"]) == list

 def get_categories(self) -> set[str]:
  return set(map(lambda c: c.strip().lower().lstrip("#"), self._data["categories"]))

 def has_cert_endpoint(self) -> bool:
  return "cert" in self._data and type(self._data["cert"]) == str

 def get_cert_endpoint(self) -> Endpoint|None:
  return Endpoint.fromstring(self._data["cert"], defaultport=__class__.DEFAULT_HTTPS_PORT)

 def has_domains(self) -> bool:
  return "domains" in self._data and type(self._data["domains"]) == list

 def get_domains(self) -> set[dns.name.Name]:
  return set(map(lambda d: dns.name.from_unicode(d["name"]), self._data["domains"]))

 def has_endpoints(self) -> bool:
  return "endpoints" in self._data and type(self._data["endpoints"]) == list

 def get_endpoints(self) -> set[Endpoint]:
  return set(map(lambda e: Endpoint.fromstring(e["host"], defaultport=__class__.DEFAULT_NTP_PORT), self._data["endpoints"]))
