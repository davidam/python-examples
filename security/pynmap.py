import nmap
nm = nmap.PortScanner()
results = nm.scan('127.0.0.1', '22,25,80,443')
print(nm.csv())
