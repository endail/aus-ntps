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

### 1platform

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`virtualplatform.com.au:123`|||||
|`www.virtualplatform.com.au:123`|||||

### 5G Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`5gnetworks.au:123`|||||

### 7News

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`7news.com.au:123`|||||

### ABC

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.abc.net.au:123`|||||
|`ns2.abc.net.au:123`|||||

### AC3

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ac3.com.au:123`|||||
|`ns1.ac3.com.au:123`|||||
|`ns3.ac3.com.au:123`|||||
|`test.ac3.com.au:123`|||||
|`www.ac3.com.au:123`|||||

### ACT Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.act.gov.au:123`|||||

### APCS

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.apcs.com.au:123`|||||
||210.79.26.105|4|s3|no-leap|
|`ns2.apcs.com.au:123`|||||
|`ns3.apcs.com.au:123`|||||

### ASE IT Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.aseit.com.au:123`|||||
|`ns2.aseit.com.au:123`|||||
|`time.aseit.com.au:123`|||||

### AUSGRID

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.ausgrid.com.au:123`|||||
|`ns2.ausgrid.com.au:123`|||||
|`ns3.ausgrid.com.au:123`|||||

### AVCOMM

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`avcomm.com.au:123`|||||
|`www.avcomm.com.au:123`|||||

### Acurus Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`acurus.com.au:123`|||||

### Amazon Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.amazon.com.au:123`|||||

### Arrow Energy

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.arrowenergy.com.au:123`|||||

### Aurizon

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`admin.aurizon.com.au:123`|||||
|`aurizon.com.au:123`|||||
|`www.aurizon.com.au:123`|||||

### Aus IT Services

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.aus-it.com.au:123`|||||
||103.48.208.254|4|s3|no-leap|

### Aussie Broadband

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp-adl.aussiebroadband.com.au:123`|||||
|`ntp-bne.aussiebroadband.com.au:123`|||||
|`ntp-mel.aussiebroadband.com.au:123`|||||
|`ntp-per.aussiebroadband.com.au:123`|||||
|`ntp-syd.aussiebroadband.com.au:123`|||||
|`ntp.aussiebroadband.com.au:123`|||||

### Australain Competition & Consumer Commission

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.accc.gov.au:123`|||||

### Australasian Legal Information Institute

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`austlii.edu.au:123`|||||
|`ns3.austlii.edu.au:123`|||||
|`ntp.austlii.edu.au:123`|||||

### Australia Online

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.australiaonline.net.au:123`|||||
|`time.australiaonline.net.au:123`|||||

### Australia Post

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`api.auspost.com.au:123`|||||
|`auspost.com.au:123`|||||
|`developers.auspost.com.au:123`|||||
|`digitalapi.auspost.com.au:123`|||||
|`id-static.auspost.com.au:123`|||||
|`id.auspost.com.au:123`|||||
|`m.auspost.com.au:123`|||||
|`solutions-static.auspost.com.au:123`|||||
|`solutions.auspost.com.au:123`|||||
|`static.auspost.com.au:123`|||||
|`stories.auspost.com.au:123`|||||
|`www.auspost.com.au:123`|||||

### Australian Catholic University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.acu.edu.au:123`|||||
|`ns0.acu.edu.au:123`|||||
|`ns2.acu.edu.au:123`|||||
|`www.acu.edu.au:123`|||||

### Australian National University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chronos.anu.edu.au:123`|||||
|`ns.anu.edu.au:123`|||||
||150.203.1.10|4|s3|no-leap|
|`ns1.anu.edu.au:123`|||||
||150.203.1.10|4|s3|no-leap|
|`ns2.anu.edu.au:123`|||||
||150.203.22.28|4|s3|no-leap|
|`ns3.anu.edu.au:123`|||||
|`ns4.anu.edu.au:123`|||||
|`ntp.anu.edu.au:123`|||||
||150.203.1.10|4|s3|no-leap|
|`ntp1.anu.edu.au:123`|||||
||150.203.1.10|4|s3|no-leap|
|`ntp2.anu.edu.au:123`|||||
||150.203.22.28|4|s3|no-leap|
|`time.anu.edu.au:123`|||||

### Australian Securities & Investments Commission

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`asic.gov.au:123`|||||
|`ns1.asic.gov.au:123`|||||
|`ns2.asic.gov.au:123`|||||

### Australian Taxation Office

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.ato.gov.au:123`|||||
|`www.ato.gov.au:123`|||||

### Avondale University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.avondale.edu.au:123`|||||
|`ns1.avondale.edu.au:123`|||||

### Bandwidth Holdings

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`bwholdings.com.au:123`|||||
|`www.bwholdings.com.au:123`|||||

### Beyond Blue

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.beyondblue.org.au:123`|||||

### BitWave Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`bitwave.com.au:123`|||||
|`ntp.bitwave.com.au:123`|||||
||103.198.24.6|4|s1|no-leap|
|`www.bitwave.com.au:123`|||||

### BluePackets

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.bluepackets.com.au:123`|||||
|`ns2.bluepackets.com.au:123`|||||
|`ns3.bluepackets.com.au:123`|||||
|`www.bluepackets.com.au:123`|||||

### Bond University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`bond.edu.au:123`|||||
|`ntp.bond.edu.au:123`|||||

### Brennan IT

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.brennanit.com.au:123`|||||
|`ns2.brennanit.com.au:123`|||||

### Broadband Solutions

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`broadbandsolutions.com.au:123`|||||
|`www.broadbandsolutions.com.au:123`|||||

### CEnet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`cenet.catholic.edu.au:123`|||||
|`ns1.cenet.catholic.edu.au:123`|||||
|`ns2.cenet.catholic.edu.au:123`|||||
|`ns3.cenet.catholic.edu.au:123`|||||
|`ns4.cenet.catholic.edu.au:123`|||||

### CNT Corp

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.cntcorp.com.au:123`|||||

### CQ University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`cq.edu.au:123`|||||

### CSIRO

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.csiro.au:123`|||||
|`ns2.csiro.au:123`|||||
|`ns3.csiro.au:123`|||||
|`www.csiro.au:123`|||||

### CWNet Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`cwnet.com.au:123`|||||

### Canary Technology Solutions

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.canaryit.com.au:123`|||||

### Capti Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`capti.com.au:123`|||||
|`www.capti.com.au:123`|||||

### Caznet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`caznet.com.au:123`|||||
|`www.caznet.com.au:123`|||||

### Charles Darwin University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.cdu.edu.au:123`|||||
|`ns2.cdu.edu.au:123`|||||
|`ntp.cdu.edu.au:123`|||||
|`ntp1.cdu.edu.au:123`|||||
|`ntp2.cdu.edu.au:123`|||||
|`ntp3.cdu.edu.au:123`|||||
|`time.cdu.edu.au:123`|||||

### Charles Sturt University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.csu.edu.au:123`|||||
|`ntp.csu.edu.au:123`|||||
|`www.csu.edu.au:123`|||||

### Christie Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`christienetworks.com.au:123`|||||

### City Communications

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`citycomms.com.au:123`|||||

### Clearstream Broadband

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`clearstream.com.au:123`|||||
|`ns1.clearstream.com.au:123`|||||
|`ns2.clearstream.com.au:123`|||||
|`ns3.clearstream.com.au:123`|||||

### Cloud Servers Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.cloudserversaustralia.com.au:123`|||||

### Cloud365 Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`cloud365.com.au:123`|||||

### Coates Hire

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.coates.com.au:123`|||||

### CommSol

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`commsol.net.au:123`|||||

### Comvergence

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.comvergence.com.au:123`|||||
|`ns2.comvergence.com.au:123`|||||
|`ns3.comvergence.com.au:123`|||||
|`ntp.comvergence.com.au:123`|||||
|`time.comvergence.com.au:123`|||||

### Conexim Australia Pty Ltd

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.conexim.com.au:123`|||||
||203.124.190.53|4|s3|no-leap|
|`ns1.conexim.com.au:123`|||||
||203.124.190.53|4|s3|no-leap|
|`ns2.conexim.com.au:123`|||||
|`ns3.conexim.com.au:123`|||||
|`time.conexim.com.au:123`|||||

### Connect Tel Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.connecttel.com.au:123`|||||

### Connected Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.connectedoz.com.au:123`|||||
|`ns2.connectedoz.com.au:123`|||||
|`www.connectedoz.com.au:123`|||||

### ConnektNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`connektnet.com.au:123`|||||
|`www.connektnet.com.au:123`|||||

### CorpCloud

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.corpcloud.com.au:123`|||||

### Crucial Paradigm (Australia)

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.crucial.com.au:123`|||||
|`ns2.crucial.com.au:123`|||||
|`ns3.crucial.com.au:123`|||||
|`ns4.crucial.com.au:123`|||||

### Cynergic

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`cynergic.com.au:123`|||||
|`ns1.cynergic.com.au:123`|||||
|`ns2.cynergic.com.au:123`|||||
||203.55.18.5|4|s2|no-leap|
|`ns3.cynergic.com.au:123`|||||
||203.55.18.5|4|s0|unsync|
|`ntp.cynergic.com.au:123`|||||
|`www.cynergic.com.au:123`|||||

### DC West

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`dcwest.net.au:123`|||||
|`ns1.dcwest.net.au:123`|||||
|`ns2.dcwest.net.au:123`|||||
|`ns3.dcwest.net.au:123`|||||
|`www.mailprotect.dcwest.net.au:123`|||||
|`www.old.dcwest.net.au:123`|||||

### Daraco IT Services

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.daraco.com.au:123`|||||
|`ns2.daraco.com.au:123`|||||
|`ns3.daraco.com.au:123`|||||
|`ns4.daraco.com.au:123`|||||

### Data Centre as a Service

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`dcaas.com.au:123`|||||
|`ns1.dcaas.com.au:123`|||||

### Data Express

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.dataexpress.net.au:123`|||||

### Deakin University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.deakin.edu.au:123`|||||
|`ns1.deakin.edu.au:123`|||||
||128.184.218.53|4|s3|no-leap|
|`ns2.deakin.edu.au:123`|||||
||128.184.34.53|4|s3|no-leap|

### Dedicated Servers

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.dedicatedservers.net.au:123`|||||
||162.159.200.1|4|s3|no-leap|
||159.196.3.239|4|s1|no-leap|
||103.76.40.123|4|s3|no-leap|
||162.159.200.123|4|s3|no-leap|

### Delion

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.delion.com.au:123`|||||
|`ns1.delion.com.au:123`|||||
|`ns2.delion.com.au:123`|||||
|`ns3.delion.com.au:123`|||||
|`ntp1.delion.com.au:123`|||||
|`ntp2.delion.com.au:123`|||||
|`www.delion.com.au:123`|||||

### Department of Climate Change, Energy, the Environment and Water

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.dcceew.gov.au:123`|||||

### Department of Foreign Affairs and Trade

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.dfat.gov.au:123`|||||

### Department of Health and Aged Care

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.health.gov.au:123`|||||

### Department of Home Affairs

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`tic.homeaffairs.gov.au:123`|||||
|`toc.homeaffairs.gov.au:123`|||||
|`www.homeaffairs.gov.au:123`|||||

### Dicker Data

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.dickerdata.com.au:123`|||||

### Digital Pacific Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.digitalpacific.com.au:123`|||||
|`ns2.digitalpacific.com.au:123`|||||
|`ns3.digitalpacific.com.au:123`|||||
|`ntp.digitalpacific.com.au:123`|||||
|`www.digitalpacific.com.au:123`|||||

### ECN Internet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.ecn.net.au:123`|||||
||203.22.70.2|4|s2|no-leap|

### Edith Cowan University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.ecu.edu.au:123`|||||
|`ns2.ecu.edu.au:123`|||||
|`ntp.ecu.edu.au:123`|||||
|`ntp1.ecu.edu.au:123`|||||
|`ntp2.ecu.edu.au:123`|||||
|`www.ecu.edu.au:123`|||||

### Enablis

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.enablis.com.au:123`|||||
|`ns2.enablis.com.au:123`|||||
|`www.enablis.com.au:123`|||||

### Encoo Communications

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.encoo.com.au:123`|||||

### EscapeNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.esc.net.au:123`|||||
|`ns1.esc.net.au:123`|||||
|`ns2.esc.net.au:123`|||||
|`ns3.esc.net.au:123`|||||
|`ns4.esc.net.au:123`|||||
|`ntp.esc.net.au:123`|||||
|`tic.esc.net.au:123`|||||
||123.136.34.45|4|s3|no-leap|
|`toc.esc.net.au:123`|||||
||123.136.34.46|4|s3|no-leap|

### Ethan Group

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ethan.global:123`|||||
|`www.ethan.global:123`|||||

### Eventbrite

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.eventbrite.com.au:123`|||||
|`chronos.eventbrite.com.au:123`|||||
|`clock.eventbrite.com.au:123`|||||
|`ns.eventbrite.com.au:123`|||||
|`ns0.eventbrite.com.au:123`|||||
|`ns1.eventbrite.com.au:123`|||||
|`ns2.eventbrite.com.au:123`|||||
|`ns3.eventbrite.com.au:123`|||||
|`ns4.eventbrite.com.au:123`|||||
|`ntp.eventbrite.com.au:123`|||||
|`ntp0.eventbrite.com.au:123`|||||
|`ntp1.eventbrite.com.au:123`|||||
|`ntp2.eventbrite.com.au:123`|||||
|`ntp3.eventbrite.com.au:123`|||||
|`ntp4.eventbrite.com.au:123`|||||
|`tic.eventbrite.com.au:123`|||||
|`tick.eventbrite.com.au:123`|||||
|`time.eventbrite.com.au:123`|||||
|`time0.eventbrite.com.au:123`|||||
|`time1.eventbrite.com.au:123`|||||
|`time2.eventbrite.com.au:123`|||||
|`time3.eventbrite.com.au:123`|||||
|`time4.eventbrite.com.au:123`|||||
|`toc.eventbrite.com.au:123`|||||
|`tock.eventbrite.com.au:123`|||||

### Exetel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`clock.exetel.com.au:123`|||||
||220.233.0.50|4|s2|no-leap|
|`ns1.exetel.com.au:123`|||||
||220.233.0.1|4|s2|no-leap|
|`ns2.exetel.com.au:123`|||||
||220.233.0.2|4|s2|no-leap|
|`ns3.exetel.com.au:123`|||||
|`www.exetel.com.au:123`|||||

### Falcore

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`falcore.com.au:123`|||||

### Federation University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`arts.federation.edu.au:123`|||||
|`experts.federation.edu.au:123`|||||
|`federation.edu.au:123`|||||
|`internal.federation.edu.au:123`|||||
|`pogallery.federation.edu.au:123`|||||
|`servicedesk.federation.edu.au:123`|||||
|`staff.federation.edu.au:123`|||||
|`time.federation.edu.au:123`|||||
|`www.federation.edu.au:123`|||||

### FetchTV

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`0.fetchtv.pool.ntp.org:123`|||||
||147.182.158.78|4|s2|no-leap|
||216.240.36.24|4|s2|no-leap|
||45.63.54.13|4|s2|no-leap|
||44.190.5.123|4|s2|no-leap|
|`ntp.fetchtv.com.au:123`|||||
||159.89.45.132|4|s2|no-leap|
||96.60.160.227|4|s1|no-leap|
||172.233.153.85|4|s3|no-leap|
||23.141.40.123|4|s2|no-leap|
|`www.fetchtv.com.au:123`|||||

### FireNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`firenet.com.au:123`|||||
|`ntp.firenet.com.au:123`|||||
|`www.firenet.com.au:123`|||||

### FirstFocus

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.firstfocus.com.au:123`|||||
|`ns1.firstfocus.com.au:123`|||||
|`ns3.firstfocus.com.au:123`|||||
|`www.firstfocus.com.au:123`|||||

### Flintel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`flintel.com.au:123`|||||
|`www.flintel.com.au:123`|||||

### Gizmodo

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.gizmodo.com.au:123`|||||

### GoHosting

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`gohosting.com.au:123`|||||
|`ns1.gohosting.com.au:123`|||||
|`ns2.gohosting.com.au:123`|||||
|`ns3.gohosting.com.au:123`|||||
|`time.gohosting.com.au:123`|||||
||103.11.147.150|4|s3|no-leap|

### Griffith University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.griffith.edu.au:123`|||||
||132.234.1.1|4|s3|no-leap|
|`www.griffith.edu.au:123`|||||

### Healthdirect Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.healthdirect.gov.au:123`|||||

### Heritage Bank

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.heritage.com.au:123`|||||
|`ns2.heritage.com.au:123`|||||
|`ns3.heritage.com.au:123`|||||
|`www.heritage.com.au:123`|||||

### Host Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`hostnetworks.com.au:123`|||||
|`ns1.hostnetworks.com.au:123`|||||
|`ns2.hostnetworks.com.au:123`|||||
|`ns3.hostnetworks.com.au:123`|||||
|`ns4.hostnetworks.com.au:123`|||||

### Host Tel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`hosttel.com.au:123`|||||
|`ns0.hosttel.com.au:123`|||||
||203.30.45.224|4|s0|unsync|
|`ns1.hosttel.com.au:123`|||||
|`ns2.hosttel.com.au:123`|||||
|`ns4.hosttel.com.au:123`|||||
|`ntp.hosttel.com.au:123`|||||
||203.30.45.224|4|s0|unsync|
|`www.hosttel.com.au:123`|||||

### Host Universal

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`hostuniversal.com.au:123`|||||
|`ns1.hostuniversal.com.au:123`|||||
|`ns2.hostuniversal.com.au:123`|||||

### HostedNetwork

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.hostednetwork.com.au:123`|||||
||182.160.152.162|4|s2|no-leap|
|`ns2.hostednetwork.com.au:123`|||||
|`ns3.hostednetwork.com.au:123`|||||
||182.160.152.162|4|s2|no-leap|
|`ns4.hostednetwork.com.au:123`|||||

### Hunter Water

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.hunterwater.com.au:123`|||||
|`ns2.hunterwater.com.au:123`|||||

### ICTouch

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.ictouch.com.au:123`|||||

### IP Exchange

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ipexchange.com.au:123`|||||
|`ns1.ipexchange.com.au:123`|||||
|`ns2.ipexchange.com.au:123`|||||
|`ns3.ipexchange.com.au:123`|||||
||103.230.156.166|4|s2|no-leap|

### IPNG

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ipng.com.au:123`|||||
|`www.ipng.com.au:123`|||||

### IPTelco

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`iptelco.com.au:123`|||||
|`ns1.iptelco.com.au:123`|||||
|`ns2.iptelco.com.au:123`|||||

### Infinite Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.infinite.net.au:123`|||||
|`ns2.infinite.net.au:123`|||||
|`ns3.infinite.net.au:123`|||||
|`ns4.infinite.net.au:123`|||||
|`ntp.infinite.net.au:123`|||||
||119.15.111.2|4|s3|no-leap|
||119.15.111.1|4|s3|no-leap|
||175.106.7.2|4|s3|no-leap|
||175.106.7.1|4|s3|no-leap|
|`www.infinite.net.au:123`|||||

### Interconnect Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.rbe.net.au:123`|||||
|`ns1.rbe.net.au:123`|||||
|`ns2.rbe.net.au:123`|||||
|`ns3.rbe.net.au:123`|||||
|`ns4.rbe.net.au:123`|||||
|`ntp.rbe.net.au:123`|||||
||192.231.203.132|4|s2|no-leap|

### Internet Association of Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.waia.asn.au:123`|||||
|`ns2.waia.asn.au:123`|||||
|`ntp.internet.asn.au:123`|||||
|`ntp.waia.asn.au:123`|||||

### Internode

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.on.net:123`|||||
|`ns2.on.net:123`|||||
||192.231.203.2|4|s3|no-leap|
|`ns3.on.net:123`|||||
|`ns4.on.net:123`|||||
|`ntp.internode.on.net:123`|||||
||192.231.203.132|4|s2|no-leap|
|`ntp.on.net:123`|||||
||192.231.203.132|4|s2|no-leap|

### James Cook University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.jcu.edu.au:123`|||||
|`ns1.jcu.edu.au:123`|||||
|`ns2.jcu.edu.au:123`|||||
|`ns3.jcu.edu.au:123`|||||
|`ns4.jcu.edu.au:123`|||||
|`ntp.jcu.edu.au:123`|||||
|`ntp1.jcu.edu.au:123`|||||
|`ntp2.jcu.edu.au:123`|||||
|`www.jcu.edu.au:123`|||||

### John Holland

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`api.johnholland.com.au:123`|||||
|`johnholland.com.au:123`|||||
|`www.johnholland.com.au:123`|||||

### KERNWIFI

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.kernwifi.com.au:123`|||||
|`ns2.kernwifi.com.au:123`|||||
|`ntp.kernwifi.com.au:123`|||||
||180.150.8.191|4|s1|no-leap|
||162.159.200.1|4|s3|no-leap|
||162.159.200.123|4|s3|no-leap|
||159.196.44.158|4|s2|no-leap|
|`ntp2.kernwifi.com.au:123`|||||
||159.196.44.158|4|s2|no-leap|
||180.150.8.191|4|s1|no-leap|
||162.159.200.1|4|s3|no-leap|
||162.159.200.123|4|s3|no-leap|

### LaTrobe University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`apex.latrobe.edu.au:123`|||||
|`ns0.latrobe.edu.au:123`|||||
|`ns1.latrobe.edu.au:123`|||||
|`ns2.latrobe.edu.au:123`|||||
|`ns3.latrobe.edu.au:123`|||||
|`ntp.latrobe.edu.au:123`|||||
|`ntp1.latrobe.edu.au:123`|||||
|`ntp2.latrobe.edu.au:123`|||||
|`ntp3.latrobe.edu.au:123`|||||
|`ntp4.latrobe.edu.au:123`|||||
|`www.latrobe.edu.au:123`|||||

### Latrobe Community Health Service

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.lchs.com.au:123`|||||
|`ns1.lchs.com.au:123`|||||
|`ns2.lchs.com.au:123`|||||
|`ns3.lchs.com.au:123`|||||
|`ns4.lchs.com.au:123`|||||
|`www.lchs.com.au:123`|||||

### Launtel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chronos.launtel.net.au:123`|||||
|`freeipa.launtel.net.au:123`|||||

### Leaptel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`leaptel.com.au:123`|||||
|`www.leaptel.com.au:123`|||||

### Lebara

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.lebara.com.au:123`|||||
|`chronos.lebara.com.au:123`|||||
|`clock.lebara.com.au:123`|||||
|`ns.lebara.com.au:123`|||||
|`ns0.lebara.com.au:123`|||||
|`ns1.lebara.com.au:123`|||||
|`ns2.lebara.com.au:123`|||||
|`ns3.lebara.com.au:123`|||||
|`ns4.lebara.com.au:123`|||||
|`ntp.lebara.com.au:123`|||||
|`ntp0.lebara.com.au:123`|||||
|`ntp1.lebara.com.au:123`|||||
|`ntp2.lebara.com.au:123`|||||
|`ntp3.lebara.com.au:123`|||||
|`ntp4.lebara.com.au:123`|||||
|`tic.lebara.com.au:123`|||||
|`tick.lebara.com.au:123`|||||
|`time.lebara.com.au:123`|||||
|`time0.lebara.com.au:123`|||||
|`time1.lebara.com.au:123`|||||
|`time2.lebara.com.au:123`|||||
|`time3.lebara.com.au:123`|||||
|`time4.lebara.com.au:123`|||||
|`toc.lebara.com.au:123`|||||
|`tock.lebara.com.au:123`|||||

### Lumity Technology Solutions

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`lumity.com.au:123`|||||

### ME Bank

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.mebank.com.au:123`|||||

### Macquarie University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.mq.edu.au:123`|||||
|`ntp1.mq.edu.au:123`|||||
|`ntp2.mq.edu.au:123`|||||
|`ntp3.mq.edu.au:123`|||||
|`ntp4.mq.edu.au:123`|||||
|`time.mq.edu.au:123`|||||
|`www.mq.edu.au:123`|||||

### Mammoth Cloud

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.mammoth.com.au:123`|||||
|`ns2.mammoth.com.au:123`|||||

### MarchNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`marchnet.com.au:123`|||||
|`www.marchnet.com.au:123`|||||

### Mater

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.mater.org.au:123`|||||

### Melbourne ISP

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`melbourneisp.com:123`|||||
|`www.au.melbourneisp.com:123`|||||
|`www.dev.melbourneisp.com:123`|||||
|`www.speedtest.melbourneisp.com:123`|||||

### Monash University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.monash.edu.au:123`|||||
|`ns1.monash.edu.au:123`|||||
|`ns2.monash.edu.au:123`|||||
|`ns3.monash.edu.au:123`|||||
|`ns4.monash.edu.au:123`|||||
|`ntp.monash.edu.au:123`|||||
|`ntp1.monash.edu.au:123`|||||
|`ntp1.net.monash.edu.au:123`|||||
||130.194.1.123|4|s1|no-leap|
|`ntp2.monash.edu.au:123`|||||
|`ntp2.net.monash.edu.au:123`|||||
||130.194.7.123|4|s1|no-leap|
|`ntp3.net.monash.edu.au:123`|||||
|`time.monash.edu.au:123`|||||
|`www.monash.edu.au:123`|||||

### Murdoch University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.murdoch.edu.au:123`|||||
|`ns2.murdoch.edu.au:123`|||||
|`ns3.murdoch.edu.au:123`|||||
|`ns4.murdoch.edu.au:123`|||||
|`ntp.murdoch.edu.au:123`|||||
|`www.murdoch.edu.au:123`|||||

### MyNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp1.mynet.au:123`|||||
|`ntp2.mynet.au:123`|||||
|`www.mynet.au:123`|||||

### NAB Investment Holdings

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`nabih.com.au:123`|||||
|`www.nabih.com.au:123`|||||

### NEC

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.nec.com.au:123`|||||
|`ns2.nec.com.au:123`|||||

### National Library of Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.nla.gov.au:123`|||||
|`ns2.nla.gov.au:123`|||||
|`ns3.nla.gov.au:123`|||||
|`ntp.nla.gov.au:123`|||||
|`ntp1.nla.gov.au:123`|||||
|`www.nla.gov.au:123`|||||

### New South Wales Department of Education

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`education.nsw.gov.au:123`|||||

### New South Wales Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.nsw.gov.au:123`|||||

### Newcastle Connect

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`newcastleconnect.com.au:123`|||||
|`ns1.newcastleconnect.com.au:123`|||||
||103.175.34.1|4|s0|unsync|
|`ns2.newcastleconnect.com.au:123`|||||
|`ntp1.newcastleconnect.com.au:123`|||||
||162.159.200.1|4|s3|no-leap|
||162.159.200.123|4|s3|no-leap|
||159.196.44.158|4|s2|no-leap|
||180.150.8.191|4|s1|no-leap|
|`www.connect.newcastleconnect.com.au:123`|||||
|`www.newcastleconnectcom.newcastleconnect.com.au:123`|||||
|`www.newcastleconnectnet.newcastleconnect.com.au:123`|||||
|`www.newcastlehunterconnect.newcastleconnect.com.au:123`|||||

### Nexon

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`nexon.com.au:123`|||||
|`ns1.nexon.com.au:123`|||||
|`ns2.nexon.com.au:123`|||||
|`ns3.nexon.com.au:123`|||||
|`ntp.nexon.com.au:123`|||||
||210.215.6.3|4|s2|no-leap|
|`ntp2.nexon.com.au:123`|||||

### Northern Territory Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.nt.gov.au:123`|||||
|`ns2.nt.gov.au:123`|||||
|`nt.gov.au:123`|||||

### OCCOM

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`occom.com.au:123`|||||
|`www.occom.com.au:123`|||||

### Office of the Australian Information Commissioner

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.oaic.gov.au:123`|||||

### On Q Communications

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`onq.com.au:123`|||||

### OntheNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.onthenet.com.au:123`|||||
|`ns1.onthenet.com.au:123`|||||
|`ns2.onthenet.com.au:123`|||||
|`ntp.onthenet.com.au:123`|||||
|`ntp1.onthenet.com.au:123`|||||

### Optitel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.optitel.com.au:123`|||||

### Optus

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.optusnet.com.au:123`|||||
|`ns1.optus.com.au:123`|||||
|`ns1.optus.net:123`|||||
|`ns1.optusnet.com.au:123`|||||
|`ns2.mel.optus.net:123`|||||
|`ns2.optus.net:123`|||||
|`ns2.optusnet.com.au:123`|||||
|`ns3.optus.net:123`|||||
|`ns3.optusnet.com.au:123`|||||
|`ns4.optus.net:123`|||||
|`ns4.optusnet.com.au:123`|||||
|`ntp.optus.net:123`|||||
||211.31.132.130|4|s2|no-leap|
|`ntp.optusnet.com.au:123`|||||
||211.29.132.139|4|s2|no-leap|
||211.31.132.131|4|s2|no-leap|
|`time.optus.net:123`|||||
||211.31.132.131|4|s2|no-leap|
||211.31.132.130|4|s2|no-leap|
|`time.optusnet.com.au:123`|||||
||211.31.132.130|4|s2|no-leap|
||211.31.132.131|4|s2|no-leap|
||211.29.132.139|4|s2|no-leap|
|`www.optus.com.au:123`|||||

### OvertheWire

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.overthewire.com.au:123`|||||
|`ns2.overthewire.com.au:123`|||||
|`ns3.overthewire.com.au:123`|||||
|`ns4.overthewire.com.au:123`|||||
|`ntp.overthewire.com.au:123`|||||
|`overthewire.com.au:123`|||||
|`www.overthewire.com.au:123`|||||

### Ozot

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ozot.com.au:123`|||||

### Parliament of Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.aph.gov.au:123`|||||
|`ns2.aph.gov.au:123`|||||
|`ns3.aph.gov.au:123`|||||
|`ns4.aph.gov.au:123`|||||
|`www.aph.gov.au:123`|||||

### Pentanet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`pentanet.com.au:123`|||||

### Pivit

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.pivit.com.au:123`|||||
|`ns2.pivit.com.au:123`|||||
|`ns3.pivit.com.au:123`|||||
|`ns4.pivit.com.au:123`|||||
|`pivit.com.au:123`|||||
|`www.pivit.com.au:123`|||||

### Premier Technology Solutions

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.premiertech.com.au:123`|||||
|`ns2.premiertech.com.au:123`|||||
|`ns3.premiertech.com.au:123`|||||
|`ns4.premiertech.com.au:123`|||||
|`www.premiertech.com.au:123`|||||

### Prodigy Communications

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.prodigy.com.au:123`|||||
|`time.prodigy.com.au:123`|||||
|`www.prodigy.com.au:123`|||||

### QCS Group

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`qcsgroup.au:123`|||||

### Queensland Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.qld.gov.au:123`|||||

### Queensland Rail

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.queenslandrail.com.au:123`|||||

### Queensland University of Technology

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.qut.edu.au:123`|||||
|`ns2.qut.edu.au:123`|||||
|`ns3.qut.edu.au:123`|||||
|`ns4.qut.edu.au:123`|||||
|`www.qut.edu.au:123`|||||

### R-Group International

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.r-group.com.au:123`|||||
|`ns3.r-group.com.au:123`|||||
|`r-group.com.au:123`|||||
|`time.r-group.com.au:123`|||||

### RACQ

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.racq.com.au:123`|||||

### RMIT University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`time.rmit.edu.au:123`|||||
||203.14.0.250|4|s2|no-leap|
||103.76.40.123|4|s3|no-leap|
||162.159.200.1|4|s3|no-leap|
||159.196.44.158|4|s2|no-leap|
|`www.rmit.edu.au:123`|||||

### Ramsay Health Care

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.ramsayhealth.com.au:123`|||||

### ReadiiTel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`readiitel.com.au:123`|||||
|`www.readiitel.com.au:123`|||||

### RemoteISP

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`remoteisp.com.au:123`|||||

### Reseau

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.reseau.com.au:123`|||||
|`ns2.reseau.com.au:123`|||||
|`ns3.reseau.com.au:123`|||||
|`reseau.com.au:123`|||||

### Reserve Bank of Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.rba.gov.au:123`|||||
|`ns2.rba.gov.au:123`|||||
|`ns3.rba.gov.au:123`|||||
|`ns4.rba.gov.au:123`|||||
|`www.rba.gov.au:123`|||||

### Rising Sun Pictures

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.rsp.com.au:123`|||||
|`ns2.rsp.com.au:123`|||||
||203.32.153.69|4|s3|no-leap|
|`ns3.rsp.com.au:123`|||||
|`www.rsp.com.au:123`|||||

### SBS

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.sbs.com.au:123`|||||
|`www.sbs.com.au:123`|||||

### SEEK

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.seek.com.au:123`|||||

### Screwloose IT Solutions

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.screwloose.com.au:123`|||||
|`chronos.screwloose.com.au:123`|||||
|`clock.screwloose.com.au:123`|||||
|`ns.screwloose.com.au:123`|||||
|`ns0.screwloose.com.au:123`|||||
|`ns1.screwloose.com.au:123`|||||
|`ns2.screwloose.com.au:123`|||||
|`ns3.screwloose.com.au:123`|||||
|`ns4.screwloose.com.au:123`|||||
|`ntp.screwloose.com.au:123`|||||
|`ntp0.screwloose.com.au:123`|||||
|`ntp1.screwloose.com.au:123`|||||
|`ntp2.screwloose.com.au:123`|||||
|`ntp3.screwloose.com.au:123`|||||
|`ntp4.screwloose.com.au:123`|||||
|`screwlooseit.com.au:123`|||||
|`tic.screwloose.com.au:123`|||||
|`tick.screwloose.com.au:123`|||||
|`time.screwloose.com.au:123`|||||
|`time0.screwloose.com.au:123`|||||
|`time1.screwloose.com.au:123`|||||
|`time2.screwloose.com.au:123`|||||
|`time3.screwloose.com.au:123`|||||
|`time4.screwloose.com.au:123`|||||
|`toc.screwloose.com.au:123`|||||
|`tock.screwloose.com.au:123`|||||
|`www.screwlooseit.com.au:123`|||||

### Sensor Dynamics

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`sensordynamics.com.au:123`|||||
|`www.sensordynamics.com.au:123`|||||

### Sentrian

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.sentrian.com.au:123`|||||

### Servers Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.serversaustralia.com.au:123`|||||
|`ns2.serversaustralia.com.au:123`|||||

### Shine Lawyers

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.shine.com.au:123`|||||

### Simm IT

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`simmit.com.au:123`|||||
|`www.simmit.com.au:123`|||||

### Sky News Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.skynews.com.au:123`|||||
|`www.skynews.com.au:123`|||||

### Skymesh

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.skymesh.net.au:123`|||||
|`ntp1.skymesh.net.au:123`|||||
|`ntp2.skymesh.net.au:123`|||||
|`ntp3.skymesh.net.au:123`|||||
|`www.skymesh.net.au:123`|||||

### Solution One

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.solution-one.com.au:123`|||||
|`ns2.solution-one.com.au:123`|||||
|`ns3.solution-one.com.au:123`|||||
|`ns4.solution-one.com.au:123`|||||
|`solution-one.com.au:123`|||||

### Somerville Group

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`store.somerville.com.au:123`|||||

### South Australia Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.sa.gov.au:123`|||||

### Southern Cross University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.scu.edu.au:123`|||||
|`www.scu.edu.au:123`|||||

### Southern Phone

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.southernphone.com.au:123`|||||
|`ns2.southernphone.com.au:123`|||||

### Spectrum Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.spectrum.com.au:123`|||||
|`ns2.spectrum.com.au:123`|||||
||203.14.108.10|4|s11|no-leap|
|`ns3.spectrum.com.au:123`|||||
|`ns4.spectrum.com.au:123`|||||
|`ntp.spectrum.com.au:123`|||||
||202.68.160.8|4|s3|no-leap|
|`spectrum.com.au:123`|||||
|`time.spectrum.com.au:123`|||||
||202.68.160.8|4|s3|no-leap|

### Spintel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`203.23.237.200:123`|||||
||203.23.237.200|4|s2|no-leap|
|`ns1.spintel.net.au:123`|||||
||203.29.65.3|4|s4|no-leap|
|`ns2.spintel.net.au:123`|||||
|`ns3.spintel.net.au:123`|||||

### Summit Internet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`summitinternet.com.au:123`|||||

### Suncorp

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.suncorp.com.au:123`|||||

### SwiftFiber

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.swiftfiber.com.au:123`|||||
|`chronos.swiftfiber.com.au:123`|||||
|`clock.swiftfiber.com.au:123`|||||
|`ns.swiftfiber.com.au:123`|||||
|`ns0.swiftfiber.com.au:123`|||||
|`ns1.swiftfiber.com.au:123`|||||
|`ns2.swiftfiber.com.au:123`|||||
|`ns3.swiftfiber.com.au:123`|||||
|`ns4.swiftfiber.com.au:123`|||||
|`ntp.swiftfiber.com.au:123`|||||
|`ntp0.swiftfiber.com.au:123`|||||
|`ntp1.swiftfiber.com.au:123`|||||
|`ntp2.swiftfiber.com.au:123`|||||
|`ntp3.swiftfiber.com.au:123`|||||
|`ntp4.swiftfiber.com.au:123`|||||
|`swiftfiber.com.au:123`|||||
|`tic.swiftfiber.com.au:123`|||||
|`tick.swiftfiber.com.au:123`|||||
|`time.swiftfiber.com.au:123`|||||
|`time0.swiftfiber.com.au:123`|||||
|`time1.swiftfiber.com.au:123`|||||
|`time2.swiftfiber.com.au:123`|||||
|`time3.swiftfiber.com.au:123`|||||
|`time4.swiftfiber.com.au:123`|||||
|`toc.swiftfiber.com.au:123`|||||
|`tock.swiftfiber.com.au:123`|||||

### Swinburne University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.swin.edu.au:123`|||||
|`ns2.swin.edu.au:123`|||||
|`ns3.swin.edu.au:123`|||||
|`ns4.swin.edu.au:123`|||||
|`ntp.swin.edu.au:123`|||||
||136.186.1.110|4|s2|no-leap|
|`ntp1.swin.edu.au:123`|||||
||136.186.1.45|4|s2|no-leap|
|`ntp2.swin.edu.au:123`|||||
||136.186.1.80|4|s2|no-leap|
|`ntp3.swin.edu.au:123`|||||
||136.186.1.114|4|s2|no-leap|
|`www.swinburne.edu.au:123`|||||

### Swoop

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.swoop.com.au:123`|||||
|`ns2.swoop.com.au:123`|||||
|`www.swoop.com.au:123`|||||

### Sydney Airport

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.sydneyairport.com.au:123`|||||

### TAFE NSW

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.tafensw.edu.au:123`|||||

### THe West Australian

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.thewest.com.au:123`|||||
|`ns2.thewest.com.au:123`|||||
|`thewest.com.au:123`|||||

### TI Systems

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`tisystems.com.au:123`|||||
||103.156.80.81|4|s2|no-leap|
|`www.tisystems.com.au:123`|||||
||103.156.80.81|4|s2|no-leap|

### TPG

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.tpg.com.au:123`|||||
|`ns2.tpg.com.au:123`|||||
|`ntp.tpg.com.au:123`|||||
||203.26.24.6|4|s2|no-leap|
||203.12.160.2|4|s2|no-leap|
|`ntp1.tpg.com.au:123`|||||
||203.12.160.2|4|s2|no-leap|
|`ntp2.tpg.com.au:123`|||||
||203.26.24.6|4|s2|no-leap|
|`www.tpg.com.au:123`|||||

### TPG Telecom

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.tpgtelecom.com.au:123`|||||

### Talk To You Soon

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ttys.com.au:123`|||||
|`www.ttys.com.au:123`|||||

### Tasmanian Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.tas.gov.au:123`|||||
|`ns2.tas.gov.au:123`|||||
|`ns3.tas.gov.au:123`|||||
|`tic.tas.gov.au:123`|||||
|`www.tas.gov.au:123`|||||

### Telair

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns2.telair.com.au:123`|||||
|`www.telair.com.au:123`|||||

### Telco in a Box

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.telcoinabox.com.au:123`|||||

### Telstra

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chronos.ntp.telstra.net:123`|||||
||203.14.0.250|4|s2|no-leap|
|`ns.telstra.com.au:123`|||||
|`ns2.telstra.com.au:123`|||||
|`ns3.telstra.com.au:123`|||||
|`tic.ntp.telstra.net:123`|||||
||203.14.0.250|4|s2|no-leap|
|`toc.ntp.telstra.net:123`|||||
||203.14.0.251|4|s2|no-leap|
|`www.telstra.com.au:123`|||||

### Terrerent

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`tesserent.com:123`|||||

### The Courier Mail

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.couriermail.com.au:123`|||||

### The Daily Telegraph

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.dailytelegraph.com.au:123`|||||

### The Missing Link

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.themissinglink.com.au:123`|||||

### Therapeutic Goods Administration

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.tga.gov.au:123`|||||

### Torrens University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.torrens.edu.au:123`|||||

### Transport for NSW

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.transport.nsw.gov.au:123`|||||
|`ns2.transport.nsw.gov.au:123`|||||
|`www.transport.nsw.gov.au:123`|||||

### URL Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`url.net.au:123`|||||

### United IP

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`mail.unitedip.net.au:123`|||||
|`unitedip.net.au:123`|||||
|`www.unitedip.net.au:123`|||||

### University of Adelaide

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.adelaide.edu.au:123`|||||
||129.127.40.3|4|s2|no-leap|
|`ns1.adelaide.edu.au:123`|||||
||129.127.43.4|4|s2|no-leap|
|`ns2.adelaide.edu.au:123`|||||
||129.127.41.3|4|s2|no-leap|
|`ntp.adelaide.edu.au:123`|||||
||129.127.40.3|4|s2|no-leap|
|`ntp1.adelaide.edu.au:123`|||||
||129.127.43.4|4|s2|no-leap|
|`ntp2.adelaide.edu.au:123`|||||
||129.127.41.3|4|s2|no-leap|

### University of Canberra

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.canberra.edu.au:123`|||||
|`ns1.canberra.edu.au:123`|||||
|`ns2.canberra.edu.au:123`|||||
|`ntp.canberra.edu.au:123`|||||
|`ntp1.canberra.edu.au:123`|||||
|`ntp2.canberra.edu.au:123`|||||
|`ntp3.canberra.edu.au:123`|||||
|`ntp4.canberra.edu.au:123`|||||
|`www.canberra.edu.au:123`|||||

### University of Divinity

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.divinity.edu.au:123`|||||
|`chronos.divinity.edu.au:123`|||||
|`clock.divinity.edu.au:123`|||||
|`divinity.edu.au:123`|||||
|`ns.divinity.edu.au:123`|||||
|`ns0.divinity.edu.au:123`|||||
|`ns1.divinity.edu.au:123`|||||
|`ns2.divinity.edu.au:123`|||||
|`ns3.divinity.edu.au:123`|||||
|`ns4.divinity.edu.au:123`|||||
|`ntp.divinity.edu.au:123`|||||
|`ntp0.divinity.edu.au:123`|||||
|`ntp1.divinity.edu.au:123`|||||
|`ntp2.divinity.edu.au:123`|||||
|`ntp3.divinity.edu.au:123`|||||
|`ntp4.divinity.edu.au:123`|||||
|`tic.divinity.edu.au:123`|||||
|`tick.divinity.edu.au:123`|||||
|`time.divinity.edu.au:123`|||||
|`time0.divinity.edu.au:123`|||||
|`time1.divinity.edu.au:123`|||||
|`time2.divinity.edu.au:123`|||||
|`time3.divinity.edu.au:123`|||||
|`time4.divinity.edu.au:123`|||||
|`toc.divinity.edu.au:123`|||||
|`tock.divinity.edu.au:123`|||||

### University of Melbourne

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.unimelb.edu.au:123`|||||
|`ns2.unimelb.edu.au:123`|||||
|`ntp.unimelb.edu.au:123`|||||
|`ntp1.unimelb.edu.au:123`|||||
|`ntp2.unimelb.edu.au:123`|||||

### University of New England

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.une.edu.au:123`|||||
|`ns1.une.edu.au:123`|||||
|`ns2.une.edu.au:123`|||||
|`ns3.une.edu.au:123`|||||
|`ntp.une.edu.au:123`|||||
||129.180.118.1|4|s1|no-leap|
||129.180.122.110|4|s1|no-leap|
|`ntp1.une.edu.au:123`|||||
||129.180.122.110|4|s1|no-leap|
|`ntp2.une.edu.au:123`|||||
||129.180.118.1|4|s1|no-leap|
|`tick.une.edu.au:123`|||||
||129.180.1.14|4|s1|no-leap|
|`tock.une.edu.au:123`|||||
||129.180.126.10|4|s1|no-leap|
|`www.une.edu.au:123`|||||

### University of New South Wales

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.unsw.edu.au:123`|||||
|`ns2.unsw.edu.au:123`|||||
|`ns3.unsw.edu.au:123`|||||
|`ntp.unsw.edu.au:123`|||||
|`ntp1.unsw.edu.au:123`|||||
|`ntp2.unsw.edu.au:123`|||||
|`ntp3.unsw.edu.au:123`|||||
|`www.unsw.edu.au:123`|||||

### University of Newcastle

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.newcastle.edu.au:123`|||||
|`ns1.newcastle.edu.au:123`|||||
|`ns2.newcastle.edu.au:123`|||||
|`ntp.newcastle.edu.au:123`|||||
|`time.newcastle.edu.au:123`|||||
|`www.newcastle.edu.au:123`|||||

### University of Notre Dame Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.notredame.edu.au:123`|||||

### University of Queensland

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.uq.edu.au:123`|||||
|`ntp1.uq.edu.au:123`|||||
|`ntp2.uq.edu.au:123`|||||
|`www.uq.edu.au:123`|||||

### University of South Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.unisa.edu.au:123`|||||
|`ns0.unisa.edu.au:123`|||||
|`ns1.unisa.edu.au:123`|||||
|`ns2.unisa.edu.au:123`|||||
|`www.unisa.edu.au:123`|||||

### University of Sydney

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.usyd.edu.au:123`|||||
|`ntp2.usyd.edu.au:123`|||||

### University of Tasmania

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.utas.edu.au:123`|||||
|`ns2.utas.edu.au:123`|||||
|`www.utas.edu.au:123`|||||

### University of Technology Sydney

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.uts.edu.au:123`|||||
|`ns1.uts.edu.au:123`|||||
|`ns2.uts.edu.au:123`|||||
|`ns3.uts.edu.au:123`|||||
|`ns4.uts.edu.au:123`|||||
|`time.uts.edu.au:123`|||||
|`www.uts.edu.au:123`|||||

### University of Western Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.uwa.edu.au:123`|||||
|`ns1.uwa.edu.au:123`|||||
|`ns2.uwa.edu.au:123`|||||
|`ns3.uwa.edu.au:123`|||||
|`time.uwa.edu.au:123`|||||
||130.95.128.36|4|s3|no-leap|

### University of Woolongong

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.uow.edu.au:123`|||||
|`www.uow.edu.au:123`|||||

### University of the Sunshine Coast

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.usc.edu.au:123`|||||
||203.57.184.172|4|s2|no-leap|
||203.29.107.141|4|s2|no-leap|
||203.57.184.173|4|s2|no-leap|
||203.29.107.140|4|s2|no-leap|
|`ntp1.usc.edu.au:123`|||||
||203.29.107.140|4|s2|no-leap|
|`ntp2.usc.edu.au:123`|||||
||203.29.107.141|4|s2|no-leap|
|`ntp3.usc.edu.au:123`|||||
||203.57.184.172|4|s2|no-leap|
|`ntp4.usc.edu.au:123`|||||
||203.57.184.173|4|s2|no-leap|
|`www.usc.edu.au:123`|||||

### VMvault

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`vmvault.com.au:123`|||||

### Valve Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`valvenetworks.com.au:123`|||||
|`www.valvenetworks.com.au:123`|||||

### Vernet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.vernet.com.au:123`|||||
|`ns2.vernet.com.au:123`|||||

### Victorian Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.vic.gov.au:123`|||||

### Vine Networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`vinenetworks.com.au:123`|||||

### Virtutel

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.virtutel.com.au:123`|||||
|`ns2.virtutel.com.au:123`|||||
|`time.virtutel.com.au:123`|||||
|`www.virtutel.com.au:123`|||||

### Vocus

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.vocus.network:123`|||||
|`ns2.vocus.network:123`|||||
|`ns3.vocus.com.au:123`|||||
|`ntp.vocus.com.au:123`|||||
|`ntp.vocus.network:123`|||||
||210.50.117.21|4|s2|no-leap|
||211.26.226.21|4|s2|no-leap|
||210.50.30.220|4|s2|no-leap|
||210.50.76.220|4|s2|no-leap|
|`www.vocus.com.au:123`|||||

### Vodafone Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.vodafone.com.au:123`|||||
|`ns2.vodafone.com.au:123`|||||
|`www.vodafone.com.au:123`|||||

### WJ Partners

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`wjpartners.com.au:123`|||||

### Wagner Corporation

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.wagnercorporation.com.au:123`|||||

### Web in a Box

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.webinabox.net.au:123`|||||
|`ns2.webinabox.net.au:123`|||||
|`ns3.webinabox.net.au:123`|||||
|`ns4.webinabox.net.au:123`|||||
|`ntp.webinabox.net.au:123`|||||
||110.173.224.100|4|s2|no-leap|

### WebVault

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.webvault.com.au:123`|||||
|`ns2.webvault.com.au:123`|||||
|`ns3.webvault.com.au:123`|||||
|`ntp.webvault.com.au:123`|||||
|`webvault.com.au:123`|||||
|`www.webvault.com.au:123`|||||

### Western Australia Government

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`tts.production.www.wa.gov.au:123`|||||
|`www.wa.gov.au:123`|||||

### Western Sydney University

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.uws.edu.au:123`|||||
|`ns.westernsydney.edu.au:123`|||||
|`ns1.uws.edu.au:123`|||||
|`ns1.westernsydney.edu.au:123`|||||
|`ns2.uws.edu.au:123`|||||
|`ns2.westernsydney.edu.au:123`|||||
|`ns3.uws.edu.au:123`|||||
|`ns3.westernsydney.edu.au:123`|||||
|`ns4.uws.edu.au:123`|||||
|`ns4.westernsydney.edu.au:123`|||||
|`ntp.uws.edu.au:123`|||||
|`ntp.westernsydney.edu.au:123`|||||
|`ntp1.uws.edu.au:123`|||||
|`ntp1.westernsydney.edu.au:123`|||||
|`ntp2.uws.edu.au:123`|||||
|`ntp2.westernsydney.edu.au:123`|||||
|`time.uws.edu.au:123`|||||
|`time.westernsydney.edu.au:123`|||||
|`www.westernsydney.edu.au:123`|||||

### Westpac

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.westpac.com.au:123`|||||

### Wireline

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.wireline.com.au:123`|||||
|`ns1.wireline.com.au:123`|||||
|`ns4.wireline.com.au:123`|||||
|`wireline.com.au:123`|||||

### XYZ Telecom

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.xyztelecom.com.au:123`|||||
|`ns1.xyztelecom.com.au:123`|||||
|`ntp.xyztelecom.com.au:123`|||||
|`www.xyztelecom.com.au:123`|||||

### Xenex Systems

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`xenexsystems.com.au:123`|||||

### YourDC

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.yourdc.com.au:123`|||||
|`yourdc.com.au:123`|||||

### ap-southeast-2.clearnet.pw

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ap-southeast-2.clearnet.pw:123`|||||
||194.195.249.28|4|s2|no-leap|

### business.gov.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`bga-slot.business.gov.au:123`|||||
|`bga.scm.business.gov.au:123`|||||
|`bgaauth-slot.business.gov.au:123`|||||
|`bgaauth.business.gov.au:123`|||||
|`bgaauth.scm.business.gov.au:123`|||||
|`bgasi-slot.business.gov.au:123`|||||
|`bgasi.business.gov.au:123`|||||
|`bgasi.scm.business.gov.au:123`|||||
|`business.gov.au:123`|||||
|`ecbauth.business.gov.au:123`|||||
|`employ-slot.business.gov.au:123`|||||
|`employ.business.gov.au:123`|||||
|`employ.scm.business.gov.au:123`|||||
|`www.business.gov.au:123`|||||

### connect.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns.mel.connect.com.au:123`|||||
||192.189.54.17|4|s2|no-leap|
|`ntp.connect.com.au:123`|||||
||192.189.54.17|4|s2|no-leap|
|`ntp.mel.connect.com.au:123`|||||
||192.189.54.17|4|s2|no-leap|
|`time.connect.com.au:123`|||||
|`time2.connect.com.au:123`|||||

### e-vision

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`e-vision.com.au:123`|||||
|`ns1.e-vision.com.au:123`|||||
|`ns2.e-vision.com.au:123`|||||
|`ns3.e-vision.com.au:123`|||||
|`ns4.e-vision.com.au:123`|||||
|`www.e-vision.com.au:123`|||||

### eBay Australia

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.ebay.com.au:123`|||||

### efex

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.efex.com.au:123`|||||
|`ns2.efex.com.au:123`|||||
|`ns3.efex.com.au:123`|||||
|`ns4.efex.com.au:123`|||||
|`www.efex.com.au:123`|||||

### fastrack technology

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.fastrack.technology:123`|||||

### felix mobile

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`felixmobile.com.au:123`|||||

### fibervision networks

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`fibervision.com.au:123`|||||

### fluccs

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.fluccs.com.au:123`|||||
|`ns1.fluccs.com.au:123`|||||
|`ns2.fluccs.com.au:123`|||||

### gigafy

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`gigafy.com.au:123`|||||
|`ntp.gigafy.com.au:123`|||||
|`ntp1.gigafy.com.au:123`|||||
|`ntp2.gigafy.com.au:123`|||||

### gigawave

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`gigawave.com.au:123`|||||
|`ns1.gigawave.com.au:123`|||||
|`ns2.gigawave.com.au:123`|||||
|`www.gigawave.com.au:123`|||||

### gippswifi

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.gippswifi.com.au:123`|||||
|`ns2.gippswifi.com.au:123`|||||
|`www.gippswifi.com.au:123`|||||

### gw.vk6hgr.echidna.id.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`gw.vk6hgr.echidna.id.au:123`|||||
||180.150.124.24|4|s2|no-leap|

### harbour isp

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.harbourisp.com.au:123`|||||
|`chronos.harbourisp.com.au:123`|||||
|`clock.harbourisp.com.au:123`|||||
|`harbourisp.com.au:123`|||||
|`my.harbourisp.com.au:123`|||||
|`ns.harbourisp.com.au:123`|||||
|`ns0.harbourisp.com.au:123`|||||
|`ns1.harbourisp.com.au:123`|||||
|`ns2.harbourisp.com.au:123`|||||
|`ns3.harbourisp.com.au:123`|||||
|`ns4.harbourisp.com.au:123`|||||
|`ntp.harbourisp.com.au:123`|||||
|`ntp0.harbourisp.com.au:123`|||||
|`ntp1.harbourisp.com.au:123`|||||
|`ntp2.harbourisp.com.au:123`|||||
|`ntp3.harbourisp.com.au:123`|||||
|`ntp4.harbourisp.com.au:123`|||||
|`tic.harbourisp.com.au:123`|||||
|`tick.harbourisp.com.au:123`|||||
|`time.harbourisp.com.au:123`|||||
|`time0.harbourisp.com.au:123`|||||
|`time1.harbourisp.com.au:123`|||||
|`time2.harbourisp.com.au:123`|||||
|`time3.harbourisp.com.au:123`|||||
|`time4.harbourisp.com.au:123`|||||
|`toc.harbourisp.com.au:123`|||||
|`tock.harbourisp.com.au:123`|||||
|`www.harbourisp.com.au:123`|||||

### hostaway

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.hostaway.net.au:123`|||||
|`ns2.hostaway.net.au:123`|||||
|`ns3.hostaway.net.au:123`|||||

### hyperwave

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.hyperwave.com.au:123`|||||
|`ns1.hyperwave.com.au:123`|||||
|`www.hyperwave.com.au:123`|||||

### iPrimus

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.iprimus.com.au:123`|||||
|`ns2.iprimus.com.au:123`|||||
|`ns3.iprimus.com.au:123`|||||
|`ns4.iprimus.com.au:123`|||||
|`ntp.iprimus.com.au:123`|||||
||210.50.76.220|4|s2|no-leap|
||211.26.226.21|4|s2|no-leap|
||210.50.30.220|4|s2|no-leap|
||210.50.117.21|4|s2|no-leap|
|`www.iprimus.com.au:123`|||||

### iQNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`iqnet.com.au:123`|||||
|`ns1.iqnet.com.au:123`|||||
|`ns2.iqnet.com.au:123`|||||
|`ns3.iqnet.com.au:123`|||||
|`ns4.iqnet.com.au:123`|||||

### iag

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.iag.com.au:123`|||||

### iiNet

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`chime.ii.net:123`|||||
|`ns.ii.net:123`|||||
|`ns.iinet.net.au:123`|||||
|`ns0.ii.net:123`|||||
|`ns0.iinet.net.au:123`|||||
|`ns1.ii.net:123`|||||
|`ns1.iinet.net.au:123`|||||
|`ns2.ii.net:123`|||||
|`ns2.iinet.net.au:123`|||||
|`ns3.ii.net:123`|||||
|`ns3.iinet.net.au:123`|||||
|`ntp.ii.net:123`|||||
||203.0.178.191|4|s3|no-leap|
|`ntp.iinet.net.au:123`|||||
||203.0.178.191|4|s3|no-leap|
|`ntp1.ii.net:123`|||||
||203.0.178.191|4|s3|no-leap|
|`ntp1.iinet.net.au:123`|||||
||203.0.178.191|4|s3|no-leap|
|`ntp2.ii.net:123`|||||
||203.0.178.191|4|s3|no-leap|
|`ntp2.iinet.net.au:123`|||||
||203.0.178.191|4|s3|no-leap|
|`time.ii.net:123`|||||
||203.0.178.191|4|s3|no-leap|
|`time.iinet.net.au:123`|||||
||203.0.178.191|4|s3|no-leap|
|`www.iinet.net.au:123`|||||

### interphone

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.interphone.com.au:123`|||||
|`ns2.interphone.com.au:123`|||||

### iperium

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.imperium.com.au:123`|||||

### iseek

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`iseek.com.au:123`|||||
|`ntp.iseek.com.au:123`|||||
|`ntp0.iseek.com.au:123`|||||
|`ntp1.iseek.com.au:123`|||||
|`ntp2.iseek.com.au:123`|||||
|`ntp3.iseek.com.au:123`|||||

### kinetix

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`kinetix.net.au:123`|||||

### lumea

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.lumea.com.au:123`|||||

### mansfield.id.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`mansfield.id.au:123`|||||
||110.232.114.22|4|s2|no-leap|

### mdg it

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.mdg-it.com.au:123`|||||
|`www.mdg-it.com.au:123`|||||

### mel.clearnet.pw

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`mel.clearnet.pw:123`|||||
||67.219.100.202|4|s2|no-leap|

### melbourne.kitten.im

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`melbourne.kitten.im:123`|||||
||67.219.111.127|4|s1|no-leap|

### net360

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`net360.com.au:123`|||||

### netier

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.netier.com.au:123`|||||

### news.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns0.news.com.au:123`|||||
|`ns1.news.com.au:123`|||||
|`ntp.news.com.au:123`|||||
|`ntp0.news.com.au:123`|||||
|`ntp1.news.com.au:123`|||||

### nexthop

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.nexthop.com.au:123`|||||

### ns1.git.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.git.au:123`|||||

### ntp-sydney.gombadi.com

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp-sydney.gombadi.com:123`|||||
||194.195.124.41|4|s2|no-leap|

### ntp.2000cn.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.2000cn.com.au:123`|||||
||103.51.68.133|4|s2|no-leap|

### ntp.mazzanet.net.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.mazzanet.net.au:123`|||||
||203.206.205.83|4|s2|no-leap|

### ntp.polyfoam.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp.polyfoam.com.au:123`|||||
||203.52.62.212|4|s1|no-leap|

### ntp1.ds.network

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ntp1.ds.network:123`|||||
||27.124.125.250|4|s2|no-leap|

### pauseq4vntp1.datamossa.io

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`pauseq4vntp1.datamossa.io:123`|||||
||103.76.40.123|4|s3|no-leap|

### pingco

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.pingco.com.au:123`|||||
|`ns2.pingco.com.au:123`|||||
|`pingco.com.au:123`|||||
|`www.pingco.com.au:123`|||||

### raisingchildren.net.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`raisingchildren.net.au:123`|||||

### real world technology solutions

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.rwts.com.au:123`|||||
|`ns2.rwts.com.au:123`|||||
|`rwts.com.au:123`|||||

### realestate.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.realestate.com.au:123`|||||

### smtp.juneks.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`smtp.juneks.com.au:123`|||||
||119.18.6.37|4|s1|no-leap|

### squarealpha

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`ns1.squarealpha.com.au:123`|||||
|`ns2.squarealpha.com.au:123`|||||
|`ns3.squarealpha.com.au:123`|||||
|`www.squarealpha.com.au:123`|||||

### svc4.eshorizon.net

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`svc4.eshorizon.net:123`|||||
||139.99.236.38|4|s3|no-leap|

### syd.clearnet.pw

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`syd.clearnet.pw:123`|||||
||139.180.160.82|4|s2|no-leap|

### syd4gps0.syd.ops.aspac.uu.net

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`syd4gps0.syd.ops.aspac.uu.net:123`|||||
||203.166.99.123|4|s1|no-leap|

### tello

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`time.tello.com.au:123`|||||

### time.9r.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`time.9r.com.au:123`|||||

### time.esec.com.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`time.esec.com.au:123`|||||

### time.tfmcloud.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`time.tfmcloud.au:123`|||||
||103.165.180.123|4|s2|no-leap|

### vk6hgr.echidna.id.au

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`vk6hgr.echidna.id.au:123`|||||
||180.150.124.24|4|s2|no-leap|

### yurika

| endpoint | ip address | version | stratum | leap |
| -------- | ---------- | ------- | ------- | ---- |
|`www.yurika.com.au:123`|||||

Data last updated 2024-08-02 15:49:08.191683+00:00
