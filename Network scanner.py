import subprocess
import nmap



network = "192.168.1."
ip_address_up = []
ip_address_down = []
for ping in range(1, 255):
    ip_address = network + str(ping)
    res = subprocess.call(["ping", "-n", "2", "-w", "0.5", ip_address],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
    if res == 0:
        ip_address_up.append(ip_address)
    else:
        ip_address_down.append(ip_address)

print("******* ONLINE IP ADDRESSES *******")
for ip in ip_address_up:
    print(f"IP: {ip}")

print("******* UNRESPONSIVE IP ADDRESSES *******")
for ip in ip_address_down:
    print(f"IP: {ip}")


scanner = nmap.PortScanner()
scanner.scan("192.168.1.0/24", arguments= "-v")
hosts = scanner.all_hosts()
print("Starting scan...")

for host in hosts:
    print(f"HOST: {host}, STATE: {scanner[host].state()}")

    for protocol in scanner[host].all_protocols():
        print(f"PROTOCOL: {protocol}")
        ports = scanner[host][protocol].keys()
        print("PORTS FOUND:")
        for ports in ports:
            print(f"{ports}", end=", ")

        print()

print("\n...Scan Complete")
