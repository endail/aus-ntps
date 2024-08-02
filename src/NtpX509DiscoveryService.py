import dns.inet
import dns.name
from .NtpDiscoveryService import NtpDiscoveryService
from .Endpoint import Endpoint
from OpenSSL import SSL, crypto
import re
import socket
import dns

class NtpX509DiscoveryService(NtpDiscoveryService):

 DEFAULT_NTP_PORT: int = 123
 DEFAULT_TIMEOUT: int = 5
 DEFAULT_ENDPOINT_LIMIT: int|None = None

 def __init__(
   self,
   endpoint: Endpoint,
   timeout: int|None = DEFAULT_TIMEOUT,
   endpoint_limit: int|None = DEFAULT_ENDPOINT_LIMIT,
   subdomains_only: bool = True) -> None:
    super().__init__()
    self._endpoint: Endpoint = endpoint
    self._timeout: int|None = timeout
    self._endpoint_limit: int|None = endpoint_limit
    self._subdomains_only: bool = subdomains_only

 def set_endpoint_limit(self, limit: int|None):
  self._endpoint_limit = limit

 @classmethod
 def get_certificate(cls, endpoint: Endpoint, hostname: str, timeout: int|None = 5) -> crypto.X509:

  if endpoint.get_host() == None:
   raise ValueError("Endpoint has no host", str(endpoint), hostname)

  if hostname == None or hostname.isspace():
   raise ValueError("Hostname is not set", str(endpoint), hostname)

  ctx = SSL.Context(SSL.TLS_CLIENT_METHOD)
  ctx.set_min_proto_version(SSL.SSL3_VERSION)
  ctx.set_max_proto_version(SSL.TLS1_3_VERSION)

  if timeout is not None:
   ctx.set_timeout(timeout)

  con = SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
  con.set_tlsext_host_name(bytes(hostname, "utf-8"))

  try:
   con.connect(endpoint.totuple())
   con.do_handshake()
   return con.get_peer_certificate()
  except (socket.gaierror, SSL.Error) as err:
   print("==========================")
   print("Socket or SSL/TLS Error")
   print(err)
   print("Endpoint: {}".format(endpoint))
   print("Hostname: {}".format(hostname))
   print("Re-raising error...")
   print("==========================")
   # rethrow so we can handle connection shutdown
   raise err
  finally:
   try: con.shutdown()
   except: pass

 @classmethod
 def get_subject_alt_names(cls, cert: crypto.X509) -> set[str]|None:
  # eg. IP Address:127.0.0.1, IP Address:192.168.1.1, DNS:host.internal, DNS:host2.internal, DNS:ntp.internal
  for i in range(cert.get_extension_count()):
   ext = cert.get_extension(i)
   if ext.get_short_name().decode().strip().lower() == "subjectaltname":
    names = str(ext).strip()
    return set(re.findall(r"(?:(?:IP Address)|(?:DNS)):([^,$]+)", names, re.IGNORECASE))
  return None

 def get_endpoints(self) -> set[Endpoint]:

  try:
   cert = self.get_certificate(self._endpoint, self._endpoint.get_host(), self._timeout)
  except (socket.gaierror, SSL.Error) as err:
   print("Failed to obtain X509 certificate for {}".format(self._endpoint))
   print(err)
   return set()

  hosts = self.get_subject_alt_names(cert)

  if hosts is None:
   return set()

  print("X509 certificate hosts from {} are {}...".format(self._endpoint, hosts))

  # some filtering
  hosts = filter(lambda h: h is not None, hosts)
  hosts = map(lambda h: h.strip() , hosts)
  hosts = filter(lambda h: not h.isspace(), hosts)

  # remove wildcard domains
  hosts = filter(lambda h: not h.startswith("*."), hosts)

  # unique
  hosts = set(hosts)

  # create the endpoints
  endpoints = map(lambda d: Endpoint(d, __class__.DEFAULT_NTP_PORT), hosts)

  if self._endpoint_limit is not None:
   endpoints = set(list(endpoints)[:self._endpoint_limit])

  if self._subdomains_only:
   the_domain = dns.name.from_unicode(self._endpoint.get_host())
   # some endpoints may be ip addresses
   names = filter(lambda e: not dns.inet.is_address(e.get_host()), endpoints)
   names_and_endpoints = map(lambda e: (dns.name.from_unicode(e.get_host()), e), names)
   names_and_endpoints = filter(lambda ne: ne[0].is_subdomain(the_domain), names_and_endpoints)
   endpoints = map(lambda ne: ne[1], names_and_endpoints)
   endpoints = set(endpoints)

  print("X509 certificate hosts for {} converted to endpoints are {}".format(
   self._endpoint, list(map(lambda e: str(e), endpoints))))

  return endpoints
