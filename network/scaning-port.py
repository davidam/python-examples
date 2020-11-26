#  Copyright (C) 2020 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com> 
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com> 
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with python-examples; see the file LICENSE.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,


import socket

t_host = str(input("Enter the host to be scanned: "))   # Target Host, www.example.com
t_ip = socket.gethostbyname(t_host)     # Resolve t_host to IPv4 address

print(t_ip)      # Print the IP address

while 1:
	t_port = int(input("Enter the port: "))	   # Enter the port to be scanned
	
	try:
	    sock = socket.socket()			
	    res = sock.connect((t_ip, t_port))
	    print("Port {}: Open" .format(t_port))
	    sock.close()
	except:
		print("Port {}: Closed".format(t_port))
	
print("Port Scanning complete")
