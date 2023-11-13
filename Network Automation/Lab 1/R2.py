import telnetlib

ip_add = "192.168.6.38"
username = "cisco"
password = "cisco"

re = telnetlib.Telnet(ip_add)

re.read_until(b"Username: ")
re.write(username.encode('ascii') + b"\n")

re.read_until(b"Password: ")
re.write(password.encode('ascii') + b"\n")

re.write(b"configure terminal\n")
re.write(b"hostname Router-Cisco2\n")
re.write(b"int lo10\n")
re.write(b"ip address 11.11.11.2 255.255.255.255\n")
re.write(b"end\n")
re.write(b"exit\n")

print(re.read_all().decode('ascii'))


