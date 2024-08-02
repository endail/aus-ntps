from .Endpoint import Endpoint
from .NtpLookupCollection import NtpLookupCollection
from .NtpDiscoveryReport import NtpDiscoveryReport
from .NtpX509DiscoveryService import NtpX509DiscoveryService
from .NtpSrvDiscoveryService import NtpSrvDiscoveryService
from .NtpDnsProbeDiscoveryService import NtpDnsProbeDiscoveryService
from .NtpDetail import NtpDetail
from .util import util
import concurrent.futures
import ntp.packet
import dns.inet
import dns.ipv4
import dns.name

class NtpDiscovery(object):

 class _GetNtpResult(object):
  def __init__(self, name: str, endpoint: Endpoint) -> None:
   super().__init__()
   self.name: str = name
   self.endpoint: Endpoint = endpoint
   self.ntps: list[NtpDetail]|None = None

 def __init__(self, lookups: NtpLookupCollection) -> None:
  super().__init__()
  self._lookups = lookups

 @classmethod
 def _get_ntp_thread_func(cls, name: str, endpoint: Endpoint) -> _GetNtpResult:
  result: __class__._GetNtpResult = __class__._GetNtpResult(name, endpoint)
  print("Trying NTP {}...".format(endpoint))
  # TODO: add timeout param?
  packets: list[ntp.packet.SyncPacket] = util.ntpdig(endpoint.get_host(), endpoint.get_port(), 5)
  result.ntps = list(map(lambda p: NtpDetail(p), packets))
  return result
 
 @classmethod
 def _do_dns_domain_probe(cls, domain: dns.name.Name, current_endpoints: set[Endpoint]) -> set[Endpoint]:

  converted_names = filter(lambda e: e.has_host(), current_endpoints)
  converted_names = filter(lambda e: not dns.inet.is_address(e.get_host()), converted_names)
  converted_names = map(lambda e: dns.name.from_unicode(e.get_host()), converted_names)

  # is n a subdomain of var domain?
  subdomains = filter(lambda n: n.is_subdomain(domain), converted_names)
  new_names = set(map(lambda s: s.derelativize(domain).to_unicode(True), subdomains))

  print(list(new_names))
  unique_names = NtpDnsProbeDiscoveryService.get_unique_names(new_names)
  print(list(unique_names))

  srv = NtpDnsProbeDiscoveryService(domain)
  srv.set_names(unique_names)

  return srv.get_endpoints()

 def run(self) -> NtpDiscoveryReport:

 # For each entry in the lookup collection...
 #
 # 1. Collect a list of endpoints to query
 #  1a. Add predefined endpoints to list
 #  1b. Run a DNS SRV discovery on a given domain and add each result
 #      to the list
 #  1c. Run an X509 discovery on each certificate endpoint and add each
 #      result to the list
 #  1d. Run a DNS common name probe on each domain and add each result
 #      to the list
 #
 # 2. Perform an NTP query on each endpoint in the list and add the result
 #    to a new list
 #
 # 3. Return a report
 #

  # { "Google": [ time.google.com:123, etc... ] }
  endpoints_to_query: dict[str, set[Endpoint]] = {}

  for lookup in self._lookups:

   lookup_endpoints: set[Endpoint] = set()

   if lookup.has_endpoints():
    lookup_endpoints |= lookup.get_endpoints()

   if lookup.has_cert_endpoint():
    lookup_endpoints |= NtpX509DiscoveryService(lookup.get_cert_endpoint()).get_endpoints()

   if lookup.has_domains():
    for domain in lookup.get_domains():
     lookup_endpoints |= NtpSrvDiscoveryService(domain).get_endpoints()
     lookup_endpoints |= __class__._do_dns_domain_probe(domain, lookup_endpoints)

    endpoints_to_query[lookup.get_name()] = lookup_endpoints

  report: NtpDiscoveryReport = NtpDiscoveryReport()

  with concurrent.futures.ThreadPoolExecutor(max_workers=16) as exe:
   futures: list[concurrent.futures.Future] = []

   for name, endpoints in endpoints_to_query.items():
    for endpoint in endpoints:
     futures.append(exe.submit(__class__._get_ntp_thread_func, name, endpoint))

   for future in concurrent.futures.as_completed(futures):
    try:
     result = future.result()
    except ntp.packet.SyncException as err:
     print(err)
     continue

    report.append_multiple(result.name, result.endpoint, result.ntps)

   return report
