# Hostname; IP; Latency(ms); Status
nodes = [
"Srv-Web-01;192.168.1.10;15;UP",
"Srv-DB-01;192.168.1.20;450;UP",
"Srv-Backup;10.0.0.5;0;DOWN",
"Workstation-A;192.168.1.105;5;UP",
"Srv-Proxy-01;172.16.0.1;10;up",
"Srv-Mail;10.0.0.10;120;UP",
"Router-Core;192.168.1.1;2;UP",
"Srv-Dev-01;192.168.2.50;500;UP",
"Printer-Main;192.168.1.200;0;down",
"Srv-Log;10.0.0.15;105;UP"
]
ip_part = input("Ievadi IP adreses daļu:")
print("Serveri šaja tikla:")
for node in nodes:
    hostname = node.split(";")[0]
    ip = node.split(";")[1]
    if ip.startswith(ip_part):
        print(hostname)