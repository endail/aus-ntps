from .NtpDiscoveryService import NtpDiscoveryService
from .Endpoint import Endpoint
import concurrent.futures
import dns.name
import dns.resolver
import dns.exception

class NtpDnsProbeDiscoveryService(NtpDiscoveryService):

 DEFAULT_NTP_PORT: int = 123
 DEFAULT_TIMEOUT: float = 5
 DEFAULT_THREAD_COUNT: int = 8

 DEFAULT_NAMES: set[str] = set([
  "ntp",
  "ntp0",
  "ntp1",
  "ntp2",
  "ntp3",
  "ntp4",
  "time",
  "time0",
  "time1",
  "time2",
  "time3",
  "time4",
  "clock",
  "ns",
  "ns0",
  "ns1",
  "ns2",
  "ns3",
  "ns4",
  "tick",
  "tock",
  "tic",
  "toc",
  "chime",
  "chronos"
 ])

 def __init__(
  self,
  domain: dns.name.Name,
  timeout: float|None = DEFAULT_TIMEOUT,
  threads: int = DEFAULT_THREAD_COUNT,
  names: set[str] = DEFAULT_NAMES) -> None:
   super().__init__()
   self._domain: dns.name.Name = domain
   self._timeout: float|None = timeout
   self._threads: int = threads
   self._names: set[str] = names

 @classmethod
 def _get_host_thread(cls, q: dns.name.Name, timeout: float|None) -> Endpoint:
   print("Trying host {0}...".format(q.to_unicode()))
   resp = dns.resolver.resolve(q, lifetime=timeout)
   return Endpoint(str(resp.qname).rstrip(".*"), cls.DEFAULT_NTP_PORT)

 @classmethod
 def get_unique_names(cls, names: set[str]) -> set[str]:
  return cls.DEFAULT_NAMES.difference(names)

 def set_names(self, names: set[str]) -> None:
  self._names = names

 def get_endpoints(self) -> set[Endpoint]:

  endpoints: set[Endpoint] = set()
  print("Querying names {}...".format(self._names))

  with concurrent.futures.ThreadPoolExecutor(max_workers=self._threads) as exe:

   futures: list[concurrent.futures.Future] = []

   for name in map(lambda n: dns.name.from_unicode(n, self._domain), self._names):
    futures.append(exe.submit(self._get_host_thread, name, self._timeout))

   for future in concurrent.futures.as_completed(futures):
    try:
     endpoints.add(future.result())
    except (dns.resolver.NXDOMAIN,
             dns.resolver.NoNameservers,
             dns.resolver.NoAnswer,
             dns.exception.Timeout) as err:
              print(err)
              pass

   return endpoints
