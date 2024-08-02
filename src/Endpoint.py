
class Endpoint(object):
 def __init__(self, host: str|None = None, port: int|None = None) -> None:
  super().__init__()
  self._host: str|None = host.strip() if host is not None else None
  self._port: int|None = port

 def has_host(self) -> bool:
  return self._host is not None

 def get_host(self) -> str|None:
  return self._host

 def has_port(self) -> bool:
  return self._port is not None

 def get_port(self) -> int|None:
  return self._port
 
 def __hash__(self) -> int:
  return hash(str(self))

 def __eq__(self, other: object) -> bool:
  if type(other) == __class__:
   return self._host == other._host and self._port == other._port
  elif type(other) == str:
   return __class__.fromstring(other) == self
  elif type(other) == tuple[str, int]:
   return __class__(other[0], other[1]) == self
  raise ValueError("other object is not comparable")
 
 def __ne__(self, other: object) -> bool:
  return not self.__eq__(other)

 def __str__(self) -> str:
  return ("%s%s%s" % (
   self._host if self._host is not None else "",
   ":" if self._port is not None else "",
   str(self._port) if self._port is not None else ""))
 
 def totuple(self) -> tuple[str, int]:
  return (self._host, self._port)

 @classmethod
 def fromstring(cls, s: str, defaultport: int|None = None):
  parts = s.strip().split(":", 2)
  host = parts[0] if len(parts) > 1 else None
  port = int(parts[1]) if len(parts) > 1 else defaultport
  return __class__(host, port)
