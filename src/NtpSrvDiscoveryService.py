from .Endpoint import Endpoint
from .NtpDiscoveryService import NtpDiscoveryService
import dns
import dns.exception
import dns.name
import dns.rdtypes.IN.SRV
import dns.resolver

class NtpSrvDiscoveryService(NtpDiscoveryService):

 SRV_SERVICE_NAME: str = "ntp"
 SRV_PROTO_NAME: str = "udp"
 DEFAULT_NTP_PORT: int = 123
 DEFAULT_TIMEOUT: float = 5
 DEFAULT_ENDPOINT_LIMIT: int|None = None

 def __init__(
  self,
  domain: dns.name.Name,
  timeout: float|None = DEFAULT_TIMEOUT,
  endpoint_limit: int|None = DEFAULT_ENDPOINT_LIMIT,
  subdomains_only: bool = True) -> None:
   super().__init__()
   self._domain: dns.name.Name = domain
   self._timeout: float|None = timeout
   self._endpoint_limit: int|None = endpoint_limit
   self._subdomains_only = subdomains_only

 def set_endpoint_limit(self, limit: int|None):
  self._endpoint_limit = limit

 @classmethod
 def get_records(cls, domain: dns.name.Name, timeout: float|None) -> list[dns.rdtypes.IN.SRV.SRV]:
  qname = dns.name.from_text("_{}._{}".format(cls.SRV_SERVICE_NAME, cls.SRV_PROTO_NAME), domain)
  result =  dns.resolver.resolve(qname, dns.rdatatype.SRV, lifetime=timeout)
  return list(result.rrset)

 def get_endpoints(self) -> set[Endpoint]:

  records: set[Endpoint] = set()

  try:
   records = self.get_records(self._domain, self._timeout)
  except (dns.resolver.NXDOMAIN,
          dns.resolver.NoNameservers,
          dns.resolver.NoAnswer,
          dns.exception.Timeout) as err:
           print("DNS SRV failed for {}".format(self._domain))
           print(err)
           return set()

  print("SRV DNS response for {} is {}".format(
    self._domain.to_unicode(), list(map(lambda r: r.target.to_unicode(), records))))

  if self._subdomains_only:
    records = filter(lambda r: r.target.is_subdomain(self._domain), records)

  # create endpoints
  endpoints = map(lambda r: Endpoint(r.target.to_unicode(True), r.port), records)

  # unique
  endpoints = set(endpoints)

  # limit
  if self._endpoint_limit is not None:
   endpoints = set(list(endpoints)[:self._endpoint_limit])

  return endpoints
