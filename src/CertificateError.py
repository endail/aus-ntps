from .NtpDiscoveryError import NtpDiscoveryError

class CertificateError(NtpDiscoveryError):
 def __init__(self, message, *args) -> None:
  super().__init__(message, args)
