from .Endpoint import Endpoint

class NtpDiscoveryService(object):

 def __init__(self) -> None:
  super().__init__()

 def get_endpoints(self) -> set[Endpoint]:
  pass
