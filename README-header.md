# aus-ntps

A collection of Australian NTP servers

Each table contains the following information:

- **Endpoint**: the hostname (or IP address) and port number of the NTP server being queried
- **IP Address**: the IP address of the host
- **Version**: the NTP version of the NTP server
- **Stratum**: the reported [stratum value](https://en.wikipedia.org/wiki/Network_Time_Protocol#Clock_strata) of the NTP server
- **Leap**: the reported leap indictor of the NTP server

An endpoint may have zero or more IP address, version, stratum, and leap combinations. An endpoint with no entries indicates that a DNS record exists for the host, but that no NTP server exists or it was otherwise inaccessible by the Python script. For example, Aussie Broadband's NTP servers [only respond to customers](https://www.aussiebroadband.com.au/help-centre/internet/ntp-settings/). You may find it useful to test these endpoints yourself for this reason, particularly if the subdomain name of the endpoint begins with `ntp`, `time`, or one of the other [predefined names](src/NtpDnsProbeDiscoveryService.py#L14-L40). Further details about the information above can be obtained [here](https://docs.ntpsec.org/latest/ntpdig.html).

You should use the endpoint when configuring an NTP client or server. For example:

```conf
# /etc/ntpsec/ntp.conf
...
server tic.ntp.telstra.net iburst
```

## Useful Resources

- If you are looking for the Australian Government's NTP servers, please be aware they are only available to [registered users](https://www.industry.gov.au/national-measurement-institute/physical-measurement-services/time-and-frequency-services).

- Some ISPs may drop NTP traffic if the [outbound source port is port 123](https://docstore.mik.ua/orelly/networking_2ndEd/fire/ch22_05.htm) (well known NTP port number) and restrict access to some predefined ISP-controlled NTP servers. You may be able to bypass this restriction by altering the source port. One method is to add the [following iptables rule](https://superuser.com/a/1380558) to your router.

```shell
iptables -t nat -I POSTROUTING -p udp -m udp --sport 123 -j MASQUERADE --to-ports 49152-65535
```

## Servers
