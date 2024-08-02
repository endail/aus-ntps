import ntp.packet

class NtpDetail(object):

 def __init__(self, packet: ntp.packet.SyncPacket) -> None:
  super().__init__()
  self._packet: ntp.packet.SyncPacket = packet

 def version(self) -> int:
  return self._packet.version()

 def ip(self) -> str:
  return self._packet.resolved

 def stratum(self) -> int:
  return self._packet.stratum

 def leap(self) -> str:
  return self._packet.leap()
