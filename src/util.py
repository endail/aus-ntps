import dns.ipv4
import ntp.packet
from .ntpdig import queryhost as ntpsec_ntpdig

class util:

 @classmethod
 def is_ipv4_addr(cls, s: str) -> bool:
  try:
   dns.ipv4.inet_aton(s)
   return True
  except: return False

 @classmethod
 def ntpdig(cls, host: str, port: int = 123, timeout: int = 5) -> list[ntp.packet.SyncPacket]:
   # raises socket.gaierror
   #{'session': None, 'li_vn_mode': 36, '_Packet__extension': b'', 'status': 0, 'stratum': 3, 'poll': 3, 'precision': -24, 'root_delay': 1572, 'root_dispersion': 723, 'refid': 2851995649, 'reference_timestamp': 16873840357934835397, 'origin_timestamp': 16873840871369750528, 'receive_timestamp': 16873840872128219282, 'transmit_timestamp': 16873840872128333256, 'extfields': [], 'mac': '', 'hostname': 'ntp2.anu.edu.au', 'resolved': '150.203.22.28', 'received': 16873840871486769152, 'trusted': True, 'rescaled': False}
   return ntpsec_ntpdig(host, True, timeout, port)
